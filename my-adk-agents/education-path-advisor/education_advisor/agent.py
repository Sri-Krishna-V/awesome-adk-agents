"""Education Path Advisor: provide personalized educational pathway guidance for Indian students"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.data_analyst import data_analyst_agent
from .sub_agents.pathway_analyst import pathway_analyst_agent
from .sub_agents.implementation_analyst import implementation_analyst_agent
from .sub_agents.risk_analyst import risk_analyst_agent

MODEL = "gemini-2.0-flash"


education_coordinator = LlmAgent(
    name="education_coordinator",
    model=MODEL,
    description=('Coordinator agent for the Education Path Advisor, helping users navigate their educational journey.'),
    instruction=prompt.EDUCATION_COORDINATOR_SYSTEM_PROMPT,
    output_key="education_coordinator_output",
    tools=[
        AgentTool(agent=data_analyst_agent),
        AgentTool(agent=implementation_analyst_agent),
        AgentTool(agent=pathway_analyst_agent),
        AgentTool(agent=risk_analyst_agent),
    ],
)

root_agent = education_coordinator
