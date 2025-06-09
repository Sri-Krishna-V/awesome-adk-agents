"""Tools for the comparison root agent sub-agents.

This module contains tools used by the comparison root agent's sub-agents
to perform various tasks in the analysis workflow.

Exported functions:
    exit_analysis: Signals the loop agent to exit when analysis is approved
"""

from .exit_analysis import exit_analysis

__all__ = ["exit_analysis"]
