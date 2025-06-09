"""Analysis Critic Agent

This agent critiques the generated analysis for accuracy and insight.
"""

from google.adk.agents import Agent

from ...shared_libraries import constants
from . import prompt

analysis_critic_agent = Agent(
    model=constants.MODEL,
    name="analysis_critic_agent",
    description="Critiques the generated analysis for accuracy and insight.",
    instruction=prompt.ANALYSIS_CRITIC_PROMPT,
)
