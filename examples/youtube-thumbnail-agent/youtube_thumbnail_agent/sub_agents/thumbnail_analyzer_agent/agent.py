"""
Thumbnail Analyzer Root Agent

This module defines the root agent for thumbnail analysis that:
1. Analyzes all thumbnails in a loop through a sequential process
2. Generates a comprehensive style guide based on all analyses
"""

from google.adk.agents import LoopAgent, SequentialAgent

from .sub_agents.analysis_process_agent import analysis_process_agent
from .sub_agents.style_guide_generator_agent import style_guide_generator_agent

# Create the Loop Agent that repeatedly runs the analysis process
# until all thumbnails are processed
thumbnail_analysis_loop_agent = LoopAgent(
    name="ThumbnailAnalysisLoop",
    max_iterations=20,  # Maximum number of iterations (should be more than max thumbnails)
    sub_agents=[
        analysis_process_agent,  # The sequential agent that selects and analyzes thumbnails
    ],
    description="""
        Iteratively analyzes thumbnails one by one
        until all are processed
    """,
)

# Create the root Sequential Agent that:
# 1. Loops through all thumbnails to analyze them
# 2. Generates a comprehensive style guide
thumbnail_analyzer_agent = SequentialAgent(
    name="ThumbnailAnalyzerRoot",
    sub_agents=[
        thumbnail_analysis_loop_agent,  # Step 1: Analyze all thumbnails in a loop
        style_guide_generator_agent,  # Step 2: Generate style guide from all analyses
    ],
    description="""
        Analyzes multiple thumbnails from a YouTube channel,
        then creates a comprehensive style guide based on all analyses
    """,
)
