"""Tools for scraping and processing academic researcher profiles.

This module provides tools for the Academic Research Assistant Agent to extract
information from researcher profiles on academic websites. It uses web scraping
techniques to obtain text content from public profile pages.

The module contains functions for:
- Scraping researcher profiles from URLs
- Processing and cleaning the extracted text content
- Handling errors and edge cases in web requests

Dependencies:
    - requests: For making HTTP requests to profile URLs
    - BeautifulSoup: For parsing and extracting text from HTML content
"""

import requests
from bs4 import BeautifulSoup


def scrape_profile(url: str) -> str:
    """
    Scrapes a researcher's profile URL to extract the text content.

    This function retrieves the HTML content from a researcher's public profile page,
    removes HTML tags and scripts, and extracts the plain text content. It handles
    various error cases and limits the text length to avoid exceeding model context limits.

    Args:
        url (str): The URL of the researcher's public profile (e.g., Google Scholar,
                  ORCID, ResearchGate, or institutional pages).

    Returns:
        str: The cleaned text content of the profile page, stripped of HTML and
             limited to 15,000 characters. If an error occurs during retrieval or
             processing, returns an error message string instead.

    Raises:
        No exceptions are raised as errors are caught and returned as strings.

    Example:
        >>> profile_text = scrape_profile("https://scholar.google.com/citations?user=...")
        >>> keywords = extract_keywords_from_profile(profile_text)
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')

        # Remove script and style elements
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        # Get text and clean up whitespace
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip()
                  for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        # Limit the amount of text to avoid exceeding model context limits
        return text[:15000]

    except requests.exceptions.RequestException as e:
        return f"Error: Could not retrieve the URL. {e}"
