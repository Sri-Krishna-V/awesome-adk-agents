"""Comparison Root Agent for analyzing and comparing academic papers.

This module defines the Comparison Root Agent and its sub-agents, which are responsible
for analyzing academic papers in relation to a researcher's profile and generating
insightful comparisons and recommendations.

The agent architecture follows a hierarchical structure with:
1. A root sequential agent that orchestrates the entire process
2. A loop agent that iterates between:
   a. An analysis generator agent that produces detailed paper comparisons
   b. An analysis critic agent that reviews and refines the generated analysis
3. A final formatter agent that prepares the approved analysis for presentation

This module serves as the final step in the Academic Research Assistant workflow,
taking inputs from previous agents and producing the final report for the user.
"""

from google.adk.agents import SequentialAgent, LoopAgent

from .sub_agents.analysis_generator_agent import analysis_generator_agent
from .sub_agents.analysis_critic_agent import analysis_critic_agent
from .sub_agents.analysis_formatter_agent import analysis_formatter_agent

analysis_refinement_loop_agent = LoopAgent(
    name="analysis_refinement_loop_agent",
    description="Manages the iterative refinement process between analysis generation and critique.",
    max_iterations=5,
    sub_agents=[analysis_generator_agent, analysis_critic_agent],
)

# Create the root Sequential Agent that:
# 1. Refines the analysis through a loop until approved
# 2. Formats the final approved analysis for presentation
comparison_root_agent = SequentialAgent(
    name="comparison_root_agent",
    description="Orchestrates the analysis, critique, and presentation of academic papers.",
    sub_agents=[analysis_refinement_loop_agent, analysis_formatter_agent],
)
