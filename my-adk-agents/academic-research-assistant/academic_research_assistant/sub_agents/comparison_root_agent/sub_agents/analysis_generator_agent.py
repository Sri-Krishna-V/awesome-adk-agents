"""Analysis Generator Agent

This agent generates detailed analyses comparing a researcher's work to new papers.
"""

from google.adk.agents.llm_agent import LlmAgent

from ....shared_libraries import constants
from . import prompt
from .tools.exit_analysis import exit_analysis

analysis_generator_agent = LlmAgent(
    model=constants.MODEL,
    name="analysis_generator_agent",
    description="Generates an analysis comparing the user's work to new papers.",
    instruction=prompt.ANALYSIS_GENERATOR_PROMPT,
    output_key="generated_analysis",
    tools=[exit_analysis],
)
