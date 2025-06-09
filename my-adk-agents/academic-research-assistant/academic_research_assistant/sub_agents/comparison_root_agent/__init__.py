"""Comparison Root Agent for analyzing and comparing academic papers.

This module exports the Comparison Root Agent, which is responsible for analyzing
academic papers in relation to a researcher's profile and generating insightful
comparisons and recommendations.

The agent serves as the final step in the Academic Research Assistant workflow,
taking inputs from previous agents and producing the final report for the user.

The agent uses a hierarchical structure with:
1. A root sequential agent that orchestrates the entire process
2. A loop agent that iterates between:
   a. An analysis generator agent that produces detailed paper comparisons
   b. An analysis critic agent that reviews and refines the generated analysis
3. A final formatter agent that prepares the approved analysis for presentation

Exported components:
    comparison_root_agent: The agent instance that can be used by the root agent
"""

from .agent import comparison_root_agent

__all__ = ["comparison_root_agent"]
