from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

local_agent = Agent(
    # Must use 'ollama_chat' prefix
    model=LiteLlm(model="ollama_chat/qwen3:8b"),
    name="senior_software_engineer",
    instruction="You are a senior software engineer tasked with website designing. You suggest neatly formatted code for React, Vue, Next and Node JS",
)

root_agent = local_agent
