"""Implementation_analyst_agent for developing implementation strategies for educational pathways"""

from google.adk import Agent

from . import prompt

MODEL = "gemini-2.0-flash"

implementation_analyst_agent = Agent(
    model=MODEL,
    name="implementation_analyst_agent",
    instruction=prompt.IMPLEMENTATION_ANALYST_SYSTEM_PROMPT,
    output_key="implementation_plan_output",
)
