"""A production-grade tool for scraping Google Scholar using Scrapy.

This module provides a robust, thread-safe implementation for searching
Google Scholar using Scrapy. It handles common challenges like:
- Event loop conflicts with the main application
- Proper error propagation and logging
- Headless execution environment configuration
- Rate limiting and blocking detection

It also includes a SerpAPI fallback mechanism that activates automatically
if the primary Scrapy-based search fails, ensuring maximum reliability.
"""

import json
import logging
import os
import re
import tempfile
import threading
import traceback
from queue import Queue
from typing import Dict, List, Optional, Union
from urllib.parse import urlencode

import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Suppress noisy logs from libraries we don't control
logging.getLogger('scrapy').setLevel(logging.ERROR)
logging.getLogger('filelock').setLevel(logging.ERROR)
logging.getLogger('twisted').setLevel(logging.ERROR)


class ScholarSpider(scrapy.Spider):
    """A robust Scrapy spider for Google Scholar with comprehensive error handling."""
    name = "scholar_spider"

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 2,  # Be polite with requests
        'COOKIES_ENABLED': False,
        'RETRY_TIMES': 2,
        'RETRY_HTTP_CODES': [500, 502, 503, 504, 408, 429],
        'HTTPERROR_ALLOW_ALL': True,  # We'll handle HTTP errors in our code
        'LOG_LEVEL': 'ERROR',
        'TELNETCONSOLE_ENABLED': False,  # Disable telnet console for headless env
    }

    def __init__(self, query: str = "", year_from: Optional[int] = None, *args, **kwargs):
        super(ScholarSpider, self).__init__(*args, **kwargs)

        # Store parameters
        self.query = query
        self.year_from = year_from
        self.results = []
        self.errors = []
        self.paper_count = 0

        # Construct URL with parameters
        params = {'q': query, 'hl': 'en'}
        if year_from:
            params['as_ylo'] = str(year_from)

        self.start_urls = [
            f"https://scholar.google.com/scholar?{urlencode(params)}"]
        logger.info(f"Spider initialized with URL: {self.start_urls[0]}")

    def parse(self, response):
        """Parse Google Scholar search results with robust error handling."""
        try:
            # Check for blocking/CAPTCHA
            if "Our systems have detected unusual traffic" in response.text:
                logger.warning(
                    "Google Scholar is blocking requests - CAPTCHA detected")
                self.errors.append(
                    "BLOCKED: Google Scholar is showing a CAPTCHA page")
                return

            # Check for no results
            papers = response.css('div.gs_r.gs_or.gs_scl')
            if not papers:
                logger.info("No papers found for the query")
                self.errors.append("NO_RESULTS: No papers found for the query")
                return

            # Process paper results
            for paper in papers:
                if self.paper_count >= 10:  # Limit to 10 papers
                    break

                try:
                    # Extract title
                    title_elem = paper.css('h3.gs_rt')
                    if not title_elem:
                        continue

                    title = title_elem.css('a::text').get()
                    if not title:
                        # Try getting title with potential HTML tags
                        title = title_elem.get()
                        if title:
                            # Clean HTML tags
                            title = re.sub(r'<.*?>', '', title).strip()

                    # Skip if no title found
                    if not title:
                        continue

                    # Extract authors and publication info
                    authors_elem = paper.css('div.gs_a').get()
                    authors_info = self._clean_html(
                        authors_elem) if authors_elem else "No author information"

                    # Extract snippet/abstract
                    snippet_elem = paper.css('div.gs_rs').get()
                    snippet = self._clean_html(
                        snippet_elem) if snippet_elem else "No abstract available"

                    # Add to results
                    self.paper_count += 1
                    self.results.append({
                        'title': title.strip(),
                        'authors_and_publication': authors_info,
                        'snippet': snippet
                    })

                except Exception as e:
                    logger.error(f"Error processing paper: {e}")
                    # Continue with next paper even if one fails
                    continue

        except Exception as e:
            logger.error(f"Error in parse method: {e}")
            self.errors.append(f"PARSE_ERROR: {str(e)}")

    def _clean_html(self, html_text):
        """Remove HTML tags and clean up whitespace."""
        if not html_text:
            return ""
        # Remove HTML tags
        clean = re.sub(r'<.*?>', '', html_text)
        # Remove extra whitespace and newlines
        clean = ' '.join(clean.split())
        return clean.strip()


def run_spider_in_thread(query: str, year_from: Optional[int]) -> Dict:
    """
    Run the Scrapy spider in a separate thread and return results.

    This function creates a temporary directory for Scrapy to use,
    sets up signal handling, and runs the spider in an isolated process.

    Args:
        query: Search query string
        year_from: Optional starting year for filtering

    Returns:
        Dictionary with 'results' and 'errors' keys
    """
    # Create a queue for thread-safe data passing
    result_queue = Queue()

    def thread_worker():
        """Worker function to run in thread."""
        try:
            # Create a temporary directory for Scrapy to use
            with tempfile.TemporaryDirectory() as temp_dir:
                # Configure Scrapy settings with the temp directory
                settings = {
                    "FEEDS": {
                        os.path.join(temp_dir, "items.json"): {"format": "json"},
                    },
                    "FEED_EXPORT_ENCODING": "utf-8",
                }

                # Initialize the crawler process
                process = CrawlerProcess(settings)

                # Set up result collection via signals
                results = []
                errors = []

                def handle_spider_closed(spider):
                    """Callback when spider closes to collect results."""
                    nonlocal results, errors
                    results = spider.results
                    errors = spider.errors

                # Connect the signal
                dispatcher.connect(handle_spider_closed,
                                   signal=signals.spider_closed)

                # Create and run the crawler
                process.crawl(ScholarSpider, query=query, year_from=year_from)
                process.start()  # This blocks until crawling is finished

                # Put results in queue
                if errors:
                    result_queue.put({"status": "error", "errors": errors})
                else:
                    result_queue.put({"status": "success", "results": results})

        except Exception as e:
            # Capture the full traceback for debugging
            error_msg = f"Thread error: {str(e)}\n{traceback.format_exc()}"
            logger.error(error_msg)
            result_queue.put({"status": "error", "errors": [
                             f"THREAD_ERROR: {str(e)}"]})

    # Create and start the thread
    thread = threading.Thread(target=thread_worker)
    thread.daemon = True  # Thread will exit when main program exits
    thread.start()
    thread.join(timeout=30)  # Wait up to 30 seconds

    # Check if thread is still alive (timed out)
    if thread.is_alive():
        logger.error("Spider thread timed out after 30 seconds")
        return {"status": "error", "errors": ["TIMEOUT: Spider took too long to complete"]}

    # Get result from queue
    if result_queue.empty():
        logger.error("No results returned from spider thread")
        return {"status": "error", "errors": ["THREAD_ERROR: No results returned from thread"]}

    return result_queue.get()


def search_with_serpapi_fallback(query: str, year_from: Optional[int] = None) -> List[Dict[str, str]]:
    """
    Fallback search mechanism using SerpAPI when Scrapy fails.

    This function attempts to use the SerpAPI service to search Google Scholar
    as a fallback mechanism when the primary Scrapy-based search fails.

    Args:
        query: Search query string
        year_from: Optional starting year for filtering

    Returns:
        A list of dictionaries containing paper information or an error string
    """
    try:
        # Check if SerpAPI key is available
        import os
        serpapi_key = os.environ.get("SERPAPI_KEY")

        if not serpapi_key:
            logger.warning("No SerpAPI key found in environment variables")
            return "SERPAPI_ERROR: No API key found. Set SERPAPI_KEY environment variable."

        # Import SerpAPI library
        from serpapi import GoogleSearch

        # Prepare search parameters
        params = {
            "engine": "google_scholar",
            "q": query,
            "hl": "en",
            "api_key": serpapi_key
        }

        # Add year filter if specified
        if year_from:
            params["as_ylo"] = str(year_from)

        logger.info(f"Attempting SerpAPI fallback search for: {query}")
        search = GoogleSearch(params)
        results = search.get_dict()

        # Check for errors
        if "error" in results:
            logger.error(f"SerpAPI error: {results['error']}")
            return f"SERPAPI_ERROR: {results['error']}"

        # Extract organic results
        organic_results = results.get("organic_results", [])
        if not organic_results:
            logger.info("No results found via SerpAPI")
            return "SERPAPI_ERROR: No papers found for the given query."

        # Format results
        papers = []
        for result in organic_results[:10]:  # Limit to 10 papers
            papers.append({
                "title": result.get("title", "Unknown Title"),
                "authors_and_publication": result.get("publication_info", {}).get("summary", "No publication info"),
                "snippet": result.get("snippet", "No snippet available")
            })

        logger.info(
            f"SerpAPI fallback search successful, found {len(papers)} papers")
        return papers

    except ImportError:
        logger.error("SerpAPI library not installed")
        return "SERPAPI_ERROR: SerpAPI library not installed. Run 'pip install google-search-results'"
    except Exception as e:
        error_details = traceback.format_exc()
        logger.error(
            f"SerpAPI fallback search failed: {str(e)}\n{error_details}")
        return f"SERPAPI_ERROR: {str(e)}"


def search_scholar_with_scrapy(query: str, year_from: Optional[int] = None) -> str:
    """
    Production-grade Google Scholar search with automatic fallback mechanism.

    This function first attempts to search using a robust Scrapy implementation.
    If that fails, it automatically falls back to using SerpAPI (if configured).

    Args:
        query: The search query string
        year_from: Optional starting year for filtering results

    Returns:
        A formatted markdown string of results or an error message
    """
    logger.info(f"Starting search for: {query}, year from: {year_from}")

    try:
        # STEP 1: Try the primary Scrapy-based search
        logger.info("Attempting primary Scrapy-based search")
        result = run_spider_in_thread(query, year_from)

        # Check for errors in Scrapy search
        if result.get("status") == "error":
            errors = result.get("errors", ["Unknown error"])
            error_msg = errors[0] if errors else "Unknown error"

            # Log the error
            logger.warning(f"Primary search failed: {error_msg}")

            # STEP 2: If Scrapy search fails, try SerpAPI fallback
            logger.info("Primary search failed, attempting SerpAPI fallback")
            fallback_results = search_with_serpapi_fallback(query, year_from)

            # Check if fallback is a string (error message)
            if isinstance(fallback_results, str):
                # Both primary and fallback failed
                logger.error("Both primary and fallback search methods failed")
                return f"SEARCH_ERROR: Primary search failed ({error_msg}) and fallback search failed ({fallback_results})"

            # Fallback succeeded, use these results
            papers = fallback_results
            logger.info("Using results from SerpAPI fallback")
        else:
            # Primary search succeeded, use these results
            papers = result.get("results", [])
            logger.info("Using results from primary Scrapy search")

        # Check if we have any papers
        if not papers:
            return "SEARCH_ERROR: No papers found for the given query."

        # Format results as markdown
        markdown_output = ""
        for paper in papers:
            markdown_output += f"### {paper['title']}\n"
            markdown_output += f"**Source:** {paper['authors_and_publication']}\n"
            markdown_output += f"**Snippet:** {paper['snippet']}\n\n"

        logger.info(
            f"Search completed successfully, found {len(papers)} papers")
        return markdown_output.strip()

    except Exception as e:
        # Capture the full exception details
        error_details = traceback.format_exc()
        logger.error(
            f"Unexpected error in search_scholar_with_scrapy: {str(e)}\n{error_details}")
        return f"SEARCH_ERROR: An unexpected error occurred: {str(e)}"
