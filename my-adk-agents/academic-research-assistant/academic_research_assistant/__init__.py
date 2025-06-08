"""Academic Research Assistant Agent package.

This package implements an AI assistant designed to accelerate academic literature
reviews by orchestrating specialized sub-agents in a sequential workflow.

The agent helps researchers find relevant papers based on their research profile
and interests, then analyzes how these papers relate to the researcher's work.

Main components:
- Root agent: Coordinates the overall workflow
- Profiler agent: Analyzes researcher profiles to extract relevant keywords
- Searcher agent: Finds relevant academic papers using web browsing
- Comparison agent: Analyzes papers and generates insights

Usage:
    from academic_research_assistant.agent import root_agent
    root_agent.start()
"""

from . import agent
