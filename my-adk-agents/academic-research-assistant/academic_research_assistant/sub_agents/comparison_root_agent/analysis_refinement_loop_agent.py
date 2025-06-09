"""Analysis Refinement Loop Agent

This agent iteratively refines the analysis until it meets quality standards.
"""

from google.adk.agents import LoopAgent

from ...shared_libraries import constants
from . import prompt
from .analysis_generator_agent import analysis_generator_agent
from .analysis_critic_agent import analysis_critic_agent

# Create the Loop Agent that iteratively refines the analysis until approved by the critic
analysis_refinement_loop_agent = LoopAgent(
    model=constants.MODEL,
    name="analysis_refinement_loop_agent",
    description="Iteratively refines the analysis until it meets quality standards.",
    instruction=prompt.ANALYSIS_REFINEMENT_LOOP_PROMPT,
    sub_agents=[analysis_generator_agent, analysis_critic_agent],
)
