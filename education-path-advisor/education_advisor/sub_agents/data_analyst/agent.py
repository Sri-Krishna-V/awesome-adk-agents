"""Education data analyst agent for finding educational information using Google search"""

from google.adk import Agent
from google.adk.tools import google_search

from . import prompt

MODEL = "gemini-2.0-flash"

data_analyst_agent = Agent(
    model=MODEL,
    name="data_analyst",
    instruction=prompt.DATA_ANALYST_PROMPT,
    output_key="education_data_analysis_output",
    tools=[google_search],
)
