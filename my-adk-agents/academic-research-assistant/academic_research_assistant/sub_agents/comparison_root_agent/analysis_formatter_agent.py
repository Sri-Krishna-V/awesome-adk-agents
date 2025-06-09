"""Analysis Formatter Agent

This agent formats the approved analysis for final presentation to the user.
"""

from google.adk.agents import Agent

from ...shared_libraries import constants
from . import prompt

analysis_formatter_agent = Agent(
    model=constants.MODEL,
    name="analysis_formatter_agent",
    description="Formats the approved analysis for final presentation to the user.",
    instruction=prompt.ANALYSIS_FORMATTER_PROMPT,
)
