from google.adk.agents.llm_agent import Agent

from ...shared_libraries import constants
from . import prompt
from ...tools import profile_scraper
profiler_agent = Agent(
    model=constants.MODEL,
    name="profiler_agent",
    description="An agent to extract keywords from a researcher's profile.",
    instruction=prompt.PROFILER_PROMPT,
    tools=[profile_scraper.scrape_profile],
)
