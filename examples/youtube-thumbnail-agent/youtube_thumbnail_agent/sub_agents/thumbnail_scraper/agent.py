"""
Thumbnail Scraper Agent

This agent is responsible for scraping YouTube thumbnails from a specific channel.
"""

from google.adk.agents.llm_agent import LlmAgent

from youtube_thumbnail_agent.constants import GEMINI_MODEL

from .tools.scrape_channel import scrape_channel

thumbnail_scraper_agent = LlmAgent(
    name="ThumbnailScraper",
    model=GEMINI_MODEL,
    instruction="""
    You are a YouTube Thumbnail Scraper specialized in downloading thumbnails from YouTube channels.
    
    Your task is to process a channel URL, handle, or name provided by the user
    and download thumbnails from their most recent videos.
    
    # YOUR PROCESS
    
    1. Take the channel URL, handle, or name provided by the user
    2. Use the scrape_channel tool to download thumbnails from this channel
       - If there are API errors, explain clearly what went wrong
    3. Confirm the successful download of thumbnails
    
    # IMPORTANT NOTES
    
    - YouTube API key must be set in the environment variables as YOUTUBE_API_KEY
    - Thumbnails will be saved to a reference_images directory
    - Each thumbnail's filename will be structured as "channel_thumbnail_X.jpg"
    - The tool also initializes the thumbnail_analysis dictionary in state with empty strings for each thumbnail
    - Once you're done scraping, delegate to the thumbnail_analyzer_agent to start the thumbnail analysis process
    """,
    description="Scrapes thumbnails from YouTube channels for analysis",
    tools=[scrape_channel],
)
