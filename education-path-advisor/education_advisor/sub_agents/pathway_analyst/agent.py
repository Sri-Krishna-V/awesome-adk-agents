"""Pathway_analyst_agent for developing educational pathway strategies"""

from google.adk import Agent

from . import prompt

MODEL = "gemini-2.0-flash"

pathway_analyst_agent = Agent(
    model=MODEL,
    name="pathway_analyst_agent",
    instruction=prompt.PATHWAY_ANALYST_SYSTEM_PROMPT,
    # {proposed_pathway_strategies_output}
    output_key="proposed_pathway_strategies_output",
)
