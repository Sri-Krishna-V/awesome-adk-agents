"""Profiler Agent for analyzing researcher profiles.

This module exports the Profiler Agent, which is responsible for extracting
relevant keywords from a researcher's academic profile. The agent serves as
the first step in the Academic Research Assistant workflow.

Exported components:
    profiler_agent: The agent instance that can be used by the root agent
"""

from .agent import profiler_agent
