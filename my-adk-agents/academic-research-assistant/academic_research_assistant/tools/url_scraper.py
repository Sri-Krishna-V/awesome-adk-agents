"""A tool for reliably scraping text content from a URL."""

import logging
import requests
from bs4 import BeautifulSoup


def get_text_from_url(url: str) -> str:
    """
    Fetches the content from a URL and extracts clean text.

    Args:
        url: The URL of the academic profile or webpage.

    Returns:
        The extracted text content of the page, or an error string.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Remove script and style elements
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()

        # Get text and clean it up
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip()
                  for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        if not text:
            return "PROFILING_ERROR: The URL was valid, but no text content could be found."

        return text

    except requests.exceptions.RequestException as e:
        logging.error(f"URL scraping failed for {url}: {e}")
        return f"PROFILING_ERROR: Could not fetch content from the URL. Please check the link and try again. Error: {e}"
    except Exception as e:
        logging.error(f"An unexpected error occurred during URL scraping: {e}")
        return f"PROFILING_ERROR: An unexpected error occurred. {e}"
