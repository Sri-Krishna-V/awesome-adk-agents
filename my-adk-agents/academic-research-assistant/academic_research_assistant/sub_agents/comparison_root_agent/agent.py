from google.adk.agents.llm_agent import Agent

from ...shared_libraries import constants
from . import prompt


analysis_generator_agent = Agent(
    model=constants.MODEL,
    name="analysis_generator_agent",
    description="Generates an analysis comparing the user's work to new papers.",
    instruction=prompt.ANALYSIS_GENERATOR_PROMPT,
)

analysis_critic_agent = Agent(
    model=constants.MODEL,
    name="analysis_critic_agent",
    description="Critiques the generated analysis for accuracy and insight.",
    instruction=prompt.ANALYSIS_CRITIC_PROMPT,
)

comparison_root_agent = Agent(
    model=constants.MODEL,
    name="comparison_root_agent",
    description="Orchestrates the analysis and critique of academic papers.",
    instruction=prompt.COMPARISON_ROOT_PROMPT,
    sub_agents=[analysis_generator_agent, analysis_critic_agent],
)
