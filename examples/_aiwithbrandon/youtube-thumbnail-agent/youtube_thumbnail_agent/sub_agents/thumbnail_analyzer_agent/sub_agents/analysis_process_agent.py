"""Analysis Process Agent

This module defines a sequential agent that first selects a thumbnail to analyze, 
then analyzes it in detail.
"""

from google.adk.agents import SequentialAgent

from .save_analysis_agent import save_analysis_agent
from .single_thumbnail_analyzer_agent import single_thumbnail_analyzer_agent
from .thumbnail_selector_agent import thumbnail_selector_agent

# Create a Sequential Agent that first selects a thumbnail,
# then analyzes the selected thumbnail
analysis_process_agent = SequentialAgent(
    name="ThumbnailAnalysisProcess",
    sub_agents=[
        thumbnail_selector_agent,  # Step 1: Select which thumbnail to analyze
        single_thumbnail_analyzer_agent,  # Step 2: Analyze the selected thumbnail
        save_analysis_agent,  # Step 3: Save the analysis results
    ],
    description="""
        Processes thumbnails one at a time by:
        1. Selecting the next thumbnail that needs analysis
        2. Performing detailed visual analysis of the selected thumbnail
        3. Saving the analysis for future reference and style guide creation
    """,
)
