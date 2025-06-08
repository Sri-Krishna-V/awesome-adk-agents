"""Tools for the Academic Research Assistant Agent.

This package contains specialized tools used by the Academic Research Assistant
to interact with external systems and process data. The tools include:

1. profile_scraper: Tools for scraping and extracting text from researcher profiles
   on academic websites like Google Scholar, ORCID, etc.

Each tool is implemented as a function that can be called by the agent system
to perform specific tasks as part of the research workflow.

Exported functions:
    scrape_profile: Scrapes a researcher's profile URL to extract text content
"""

from .profile_scraper import scrape_profile

__all__ = ["scrape_profile"]
