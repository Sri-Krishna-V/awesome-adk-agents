"""Risk Analysis Agent for providing the final risk evaluation"""

from google.adk import Agent

from . import prompt

MODEL = "gemini-2.0-flash"

risk_analyst_agent = Agent(
    model=MODEL,
    name="risk_analyst_agent",
    instruction=prompt.RISK_ANALYST_SYSTEM_PROMPT,
    output_key="final_risk_assessment_output",
)
