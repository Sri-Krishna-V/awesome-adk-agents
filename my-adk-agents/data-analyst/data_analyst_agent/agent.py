from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import built_in_code_execution

local_agent = Agent(
    # Must use 'ollama_chat' prefix
    model=LiteLlm(model="ollama_chat/qwen3:8b"),
    name="Senior Software Engineer",
    instruction="You are a senior software engineer tasked with website designing. You suggest neatly formatted code for React, Vue, Next and Node JS",
    tools=[built_in_code_execution],
)

root_agent = local_agent