"""Tools for accessing academic data using SerpAPI.

This module provides tools for the Academic Research Assistant Agent to extract
information from researcher profiles and search for academic papers using SerpAPI.
SerpAPI provides structured access to search engine results without triggering
rate limits or CAPTCHAs.

The module contains functions for:
- Retrieving researcher profiles from Google Scholar
- Searching for academic papers on Google Scholar
- Processing and extracting structured data from API responses
- Managing API usage and implementing fallbacks

Dependencies:
    - serpapi: The SerpAPI Python client for making API requests
    - json: For processing API responses
"""

import json
import re
import time
from typing import Dict, List, Optional, Union

from serpapi import GoogleSearch

from ..shared_libraries import constants


def extract_author_id_from_url(url: str) -> Optional[str]:
    """
    Extracts the Google Scholar author ID from a profile URL.

    Args:
        url (str): The Google Scholar profile URL.

    Returns:
        Optional[str]: The extracted author ID or None if not found.
    """
    # Pattern to match Google Scholar author IDs
    pattern = r'user=([^&]+)'
    match = re.search(pattern, url)

    if match:
        return match.group(1)
    return None


def get_scholar_profile(url: str) -> str:
    """
    Retrieves a researcher's profile from Google Scholar using SerpAPI.

    This function extracts the author ID from the URL and uses SerpAPI to fetch
    the researcher's profile information, including publications, citations,
    and research interests.

    Args:
        url (str): The URL of the researcher's Google Scholar profile.

    Returns:
        str: A text representation of the researcher's profile or an error message.
    """
    # Check if SerpAPI key is available
    if not constants.SERPAPI_KEY:
        return "Error: SerpAPI key not found. Please add SERPAPI_KEY to your .env file."

    # Extract author ID from URL
    author_id = extract_author_id_from_url(url)
    if not author_id:
        return "Error: Could not extract author ID from the provided URL."

    try:
        # Set up the search parameters
        params = {
            "api_key": constants.SERPAPI_KEY,
            "engine": "google_scholar_author",
            "author_id": author_id,
            "hl": "en"
        }

        # Execute the search
        search = GoogleSearch(params)
        results = search.get_dict()

        # Check if the search was successful
        if "error" in results:
            return f"Error: {results['error']}"

        # Extract and format profile information
        profile_text = ""

        # Add author name and affiliation
        if "author" in results:
            profile_text += f"Name: {results['author']['name']}\n"
            if "affiliations" in results['author']:
                profile_text += f"Affiliation: {results['author']['affiliations']}\n"

        # Add research interests if available
        if "interests" in results:
            interests = [interest['title']
                         for interest in results['interests']]
            profile_text += f"Research Interests: {', '.join(interests)}\n\n"

        # Add publication information
        if "articles" in results:
            profile_text += "Publications:\n"
            for article in results['articles']:
                profile_text += f"- {article['title']}\n"
                if "publication" in article:
                    profile_text += f"  Published in: {article['publication']}\n"
                if "year" in article:
                    profile_text += f"  Year: {article['year']}\n"
                if "cited_by" in article and "value" in article["cited_by"]:
                    profile_text += f"  Citations: {article['cited_by']['value']}\n"
                profile_text += "\n"

        # Add citation metrics
        if "cited_by" in results:
            profile_text += "Citation Metrics:\n"
            for metric, value in results["cited_by"].items():
                profile_text += f"- {metric}: {value}\n"

        return profile_text

    except Exception as e:
        return f"Error: Failed to retrieve profile data: {str(e)}"


def search_scholar_papers(query: str, keywords: List[str] = None, year_from: int = None) -> str:
    """
    Searches for academic papers on Google Scholar using SerpAPI.

    This function searches for academic papers related to the provided query and keywords,
    optionally filtering by publication year.

    Args:
        query (str): The main search query.
        keywords (List[str], optional): Additional keywords to refine the search.
        year_from (int, optional): The earliest publication year to include.

    Returns:
        str: A formatted string containing the search results or an error message.
    """
    # Check if SerpAPI key is available
    if not constants.SERPAPI_KEY:
        return "Error: SerpAPI key not found. Please add SERPAPI_KEY to your .env file."

    try:
        # Prepare the search query
        search_query = query
        if keywords and len(keywords) > 0:
            # Add up to 3 keywords to avoid overly specific queries
            additional_terms = " ".join(keywords[:3])
            search_query = f"{search_query} {additional_terms}"

        # Set up the search parameters
        params = {
            "api_key": constants.SERPAPI_KEY,
            "engine": "google_scholar",
            "q": search_query,
            "hl": "en",
            "num": 10  # Limit to 10 results to conserve API usage
        }

        # Add year filter if provided
        if year_from:
            params["as_ylo"] = year_from

        # Execute the search
        search = GoogleSearch(params)
        results = search.get_dict()

        # Check if the search was successful
        if "error" in results:
            return f"Error: {results['error']}"

        # Format the search results
        formatted_results = "### Search Results\n\n"

        if "organic_results" in results and results["organic_results"]:
            for i, paper in enumerate(results["organic_results"], 1):
                formatted_results += f"### {paper['title']}\n"

                if "publication_info" in paper:
                    authors = paper.get("publication_info",
                                        {}).get("authors", [])
                    if authors:
                        author_names = [author.get("name", "")
                                        for author in authors]
                        formatted_results += f"*Authors:* {', '.join(author_names)}\n"

                    venue_info = []
                    if "summary" in paper["publication_info"]:
                        venue_info.append(paper["publication_info"]["summary"])
                    if "published_date" in paper["publication_info"]:
                        venue_info.append(
                            paper["publication_info"]["published_date"])

                    if venue_info:
                        formatted_results += f"*Published in:* {' - '.join(venue_info)}\n"

                if "snippet" in paper:
                    formatted_results += f"**Abstract:** {paper['snippet']}\n"
                else:
                    formatted_results += "**Abstract:** Abstract not available.\n"

                if "inline_links" in paper and "cited_by" in paper["inline_links"]:
                    formatted_results += f"*Citations:* {paper['inline_links']['cited_by']['total']}\n"

                formatted_results += "\n"
        else:
            formatted_results += "No results found for the given query.\n"

        return formatted_results

    except Exception as e:
        return f"Error: Failed to search for papers: {str(e)}"


def extract_keywords_from_profile(profile_text: str) -> str:
    """
    Extracts keywords from a researcher's profile text.

    This function analyzes the profile text to identify key research areas,
    topics, and methodologies. It's used as a helper function when processing
    profile data from SerpAPI.

    Args:
        profile_text (str): The text content of a researcher's profile.

    Returns:
        str: A comma-separated list of extracted keywords.
    """
    # Extract explicit research interests if available
    interests_match = re.search(r'Research Interests: (.*?)\n', profile_text)
    if interests_match:
        return interests_match.group(1)

    # Otherwise, extract keywords from publication titles
    titles = re.findall(r'- (.*?)\n', profile_text)
    if not titles:
        return "PROFILING_ERROR: Sparse Profile"

    # Count word frequency in titles
    word_counts = {}
    for title in titles:
        # Split title into words and filter out common stop words
        words = title.lower().split()
        for word in words:
            if len(word) > 3:  # Skip short words
                word_counts[word] = word_counts.get(word, 0) + 1

    # Get the top 15 most frequent words
    top_words = sorted(word_counts.items(),
                       key=lambda x: x[1], reverse=True)[:15]
    keywords = [word for word, _ in top_words]

    return ", ".join(keywords) if keywords else "PROFILING_ERROR: Sparse Profile"
