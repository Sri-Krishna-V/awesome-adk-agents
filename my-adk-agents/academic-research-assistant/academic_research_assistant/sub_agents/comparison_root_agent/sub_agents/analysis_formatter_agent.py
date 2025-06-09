"""Analysis Formatter Agent

This agent formats the approved analysis into a well-structured final report.
"""

from google.adk.agents.llm_agent import LlmAgent

from ....shared_libraries import constants
from . import prompt

analysis_formatter_agent = LlmAgent(
    model=constants.MODEL,
    name="analysis_formatter_agent",
    description="Formats the approved analysis into a well-structured final report.",
    instruction=prompt.ANALYSIS_FORMATTER_PROMPT,
    output_key="comparison_report",
)
