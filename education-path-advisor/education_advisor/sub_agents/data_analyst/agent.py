"""education_data_analyst_agent for finding educational information using google search"""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.0-flash"

data_analyst_agent = Agent(
    model=MODEL,
    # Changed from "education_data_analyst_agent" to match prompt reference
    name="data_analyst",
    instruction=prompt.DATA_ANALYST_PROMPT,
    output_key="education_data_analysis_output",
    tools=[google_search],
)
