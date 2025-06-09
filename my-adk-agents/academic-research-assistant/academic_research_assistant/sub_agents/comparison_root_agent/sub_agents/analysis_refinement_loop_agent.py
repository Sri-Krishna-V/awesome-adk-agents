"""Analysis Refinement Loop Agent

This agent iteratively refines the analysis until it meets quality standards.
"""

from google.adk.agents import LoopAgent

from .analysis_generator_agent import analysis_generator_agent
from .analysis_critic_agent import analysis_critic_agent

# Create the Loop Agent that iteratively refines the analysis until approved by the critic
analysis_refinement_loop_agent = LoopAgent(
    name="analysis_refinement_loop_agent",
    max_iterations=7,  # Maximum number of iterations before stopping
    sub_agents=[analysis_generator_agent, analysis_critic_agent],
    description="Iteratively refines the analysis until it meets quality standards.",
)
