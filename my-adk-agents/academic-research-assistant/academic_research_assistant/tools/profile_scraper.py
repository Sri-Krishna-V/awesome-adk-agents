"""Tools for scraping and processing academic researcher profiles.

This module provides tools for the Academic Research Assistant Agent to extract
information from researcher profiles on academic websites. It uses web scraping
techniques to obtain text content from public profile pages.

The module contains functions for:
- Scraping researcher profiles from URLs
- Processing and cleaning the extracted text content
- Handling errors and edge cases in web requests
- Manual extraction of keywords when scraping fails

Dependencies:
    - requests: For making HTTP requests to profile URLs
    - BeautifulSoup: For parsing and extracting text from HTML content
"""

import requests
import time
import random
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
    # Common user agents to rotate through
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
    ]

    # Set up headers with a random user agent
    headers = {
        'User-Agent': random.choice(user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }

    # Maximum number of retry attempts
    max_retries = 3
    retry_count = 0

    while retry_count < max_retries:
        try:
            # Add a delay between requests to avoid rate limiting
            if retry_count > 0:
                # Random delay between 2-5 seconds
                time.sleep(2 + random.random() * 3)

            response = requests.get(url, headers=headers, timeout=15)
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
            retry_count += 1
            if retry_count >= max_retries:
                return f"Error: Could not retrieve the URL after {max_retries} attempts. {e}"
            # If it's a 429 error (Too Many Requests), wait longer before retrying
            if hasattr(e, 'response') and e.response and e.response.status_code == 429:
                time.sleep(5 + random.random() * 5)  # Wait 5-10 seconds


def extract_keywords_manually(research_topic: str) -> str:
    """
    Extracts keywords from a research topic when profile scraping fails.

    This function serves as a fallback when the profile URL cannot be accessed.
    It analyzes the provided research topic to extract relevant keywords.

    Args:
        research_topic (str): The research topic provided by the user.

    Returns:
        str: A comma-separated list of keywords derived from the research topic.

    Example:
        >>> keywords = extract_keywords_manually("protein folding using deep learning")
        >>> print(keywords)
        "protein folding, deep learning, protein structure prediction, computational biology"
    """
    # For protein folding using deep learning, we can provide some common keywords
    if "protein folding" in research_topic.lower() and "deep learning" in research_topic.lower():
        return "protein folding, deep learning, protein structure prediction, AlphaFold, computational biology, structural biology, molecular dynamics, neural networks, bioinformatics, structural prediction"

    # For general AI/ML topics
    elif any(term in research_topic.lower() for term in ["machine learning", "deep learning", "artificial intelligence", "neural network", "ai"]):
        return "machine learning, deep learning, neural networks, artificial intelligence, data science, algorithms, computational models, predictive modeling, feature engineering, supervised learning"

    # For natural language processing
    elif any(term in research_topic.lower() for term in ["nlp", "natural language", "language model", "text mining"]):
        return "natural language processing, NLP, language models, text mining, sentiment analysis, named entity recognition, machine translation, text classification, information extraction, computational linguistics"

    # For computer vision
    elif any(term in research_topic.lower() for term in ["computer vision", "image processing", "object detection", "image recognition"]):
        return "computer vision, image processing, object detection, image recognition, convolutional neural networks, CNN, feature extraction, image segmentation, pattern recognition, visual perception"

    # For general science topics, extract key terms from the topic itself
    else:
        # Extract key nouns and technical terms from the research topic
        words = research_topic.split()
        keywords = []

        # Add the full research topic as the first keyword
        keywords.append(research_topic)

        # Add individual technical terms or combinations
        for i in range(len(words)):
            if len(words[i]) > 3:  # Only consider words longer than 3 characters
                keywords.append(words[i])
            if i < len(words) - 1 and len(words[i]) > 2 and len(words[i+1]) > 2:
                keywords.append(f"{words[i]} {words[i+1]}")

        # Remove duplicates and limit to 10 keywords
        unique_keywords = list(set(keywords))
        return ", ".join(unique_keywords[:10])
