"""Searcher Agent for finding relevant academic papers.

This module exports the Searcher Agent, which is responsible for finding relevant
academic papers based on a research topic and keywords. The agent uses web browsing
capabilities to search academic databases and extract paper information.

The agent serves as the second step in the Academic Research Assistant workflow,
taking inputs from the Profiler Agent and providing results to the Comparison Agent.

Exported components:
    searcher_agent: The agent instance that can be used by the root agent
"""

from .agent import searcher_agent
