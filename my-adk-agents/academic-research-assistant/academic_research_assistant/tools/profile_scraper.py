import requests
from bs4 import BeautifulSoup


def scrape_profile(url: str) -> str:
    """
    Scrapes a researcher's profile URL to extract the text content.

    Args:
        url: The URL of the researcher's public profile (e.g., Google Scholar).

    Returns:
        The text content of the page, stripped of HTML, or an error message.
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
