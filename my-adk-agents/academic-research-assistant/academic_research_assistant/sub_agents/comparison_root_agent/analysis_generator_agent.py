"""Analysis Generator Agent

This agent generates detailed analyses comparing a researcher's work to new papers.
"""

from google.adk.agents import Agent

from ...shared_libraries import constants
from . import prompt

analysis_generator_agent = Agent(
    model=constants.MODEL,
    name="analysis_generator_agent",
    description="Generates an analysis comparing the user's work to new papers.",
    instruction=prompt.ANALYSIS_GENERATOR_PROMPT,
)
