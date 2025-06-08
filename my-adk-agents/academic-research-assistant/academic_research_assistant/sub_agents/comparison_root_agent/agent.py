"""Comparison Root Agent for analyzing and comparing academic papers.

This module defines the Comparison Root Agent and its sub-agents, which are responsible
for analyzing academic papers in relation to a researcher's profile and generating
insightful comparisons and recommendations.

The agent architecture follows a hierarchical structure with:
1. A root comparison agent that orchestrates the analysis process
2. An analysis generator agent that produces detailed paper comparisons
3. An analysis critic agent that reviews and refines the generated analysis

This module serves as the final step in the Academic Research Assistant workflow,
taking inputs from previous agents and producing the final report for the user.
"""

from google.adk.agents.llm_agent import Agent

from ...shared_libraries import constants
from . import prompt


analysis_generator_agent = Agent(
    model=constants.MODEL,
    name="analysis_generator_agent",
    description="Generates an analysis comparing the user's work to new papers.",
    instruction=prompt.ANALYSIS_GENERATOR_PROMPT,
)

analysis_critic_agent = Agent(
    model=constants.MODEL,
    name="analysis_critic_agent",
    description="Critiques the generated analysis for accuracy and insight.",
    instruction=prompt.ANALYSIS_CRITIC_PROMPT,
)

comparison_root_agent = Agent(
    model=constants.MODEL,
    name="comparison_root_agent",
    description="Orchestrates the analysis and critique of academic papers.",
    instruction=prompt.COMPARISON_ROOT_PROMPT,
    sub_agents=[analysis_generator_agent, analysis_critic_agent],
)
