"""Thumbnail Selector Agent

This agent selects the next thumbnail to analyze or exits the loop if all thumbnails have been analyzed.
"""

from google.adk.agents.llm_agent import LlmAgent

from youtube_thumbnail_agent.constants import GEMINI_MODEL

from ..tools.exit_analysis import exit_analysis
from ..tools.select_thumbnail import select_thumbnail

thumbnail_selector_agent = LlmAgent(
    name="ThumbnailSelector",
    model=GEMINI_MODEL,
    instruction="""
    You are a Thumbnail Selector responsible for determining which thumbnail needs to be analyzed next.
    
    # YOUR PROCESS
    
    1. CHECK THE STATE for thumbnails needing analysis:
       - Look at thumbnail_analysis - it contains filenames as keys and analysis results as values
       - Any entry with an empty string "" needs to be analyzed
       
    2. SELECT THE NEXT THUMBNAIL:
       - If there are thumbnails with empty analysis strings:
         * Select the FIRST thumbnail with an empty analysis string
         * Use the select_thumbnail tool to set it in state
         * Pass the filename to the tool
         
    3. EXIT IF COMPLETE:
       - If ALL thumbnails have non-empty analyses (no empty strings in the dictionary):
         * Call exit_analysis to exit the loop
         * You should confirm that all thumbnails have been analyzed
    
    # IMPORTANT RULES
    
    - Only call exit_analysis when ALL thumbnails have non-empty analyses
    - Always use select_thumbnail to explicitly mark which thumbnail should be analyzed next
    - Be systematic in your selection - always choose the first thumbnail that needs analysis
    - Keep your responses concise - just confirm which thumbnail you've selected or that you're exiting the loop
    
    Remember that the thumbnail_analysis dictionary is pre-populated with all filenames,
    and your job is to select the next one for analysis or exit when all are done.
    
    Here is the current state of the thumbnail analysis:
    {thumbnail_analysis}
    """,
    description="Selects the next thumbnail to analyze or exits the loop when all are analyzed",
    tools=[select_thumbnail, exit_analysis],
)
