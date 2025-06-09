"""Profiler Agent for analyzing researcher profiles.

This module defines the Profiler Agent, which is responsible for extracting
relevant keywords from a researcher's academic profile. It uses the profile_scraper
tool to obtain text content from profile URLs and then analyzes this content to
identify key research areas, methodologies, and technical terms.

The agent serves as the first step in the Academic Research Assistant workflow,
providing essential context for subsequent paper searches and analyses.
"""

from google.adk.agents.llm_agent import Agent

from ...shared_libraries import constants
from . import prompt
from ...tools import profile_scraper

profiler_agent = Agent(
    model=constants.MODEL,
    name="profiler_agent",
    description="An agent to extract keywords from a researcher's profile.",
    instruction=prompt.PROFILER_PROMPT,
    tools=[
        profile_scraper.scrape_profile,
        profile_scraper.extract_keywords_manually,
    ],
)
