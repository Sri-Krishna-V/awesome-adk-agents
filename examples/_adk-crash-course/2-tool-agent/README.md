# 2. Tool Agent

This example demonstrates how to enhance your agent with tools, giving it capabilities beyond just generating text.

## What You'll Learn

- How to add built-in ADK tools to your agent
- Understanding how agents use tools
- Running an agent with external capabilities

## Agent Overview

The tool agent expands on the basic agent by adding a Google Search tool:
- It uses Gemini 2.0 Flash as its model
- It has access to the `google_search` tool
- It can retrieve real-time information from the web

## Code Walkthrough

```python
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search
    """,
    tools=[google_search],
)
```

Key additions from the basic agent:

1. **Importing tools**: `from google.adk.tools import google_search`
2. **Adding tools to the agent**: `tools=[google_search]`
3. **Updating instructions**: Informing the agent about its available tools

## Running the Agent

1. Create a `.env` file with your Google API keys:
   ```
   GOOGLE_API_KEY=your_api_key_here
   GOOGLE_SEARCH_API_KEY=your_search_api_key_here
   GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id_here
   ```

2. Run the agent:
   ```bash
   cd tool_agent
   python -m google.adk run
   ```

3. Try asking questions that require real-time information:
   - "What are the latest news about artificial intelligence?"
   - "Who won the last World Cup?"

## Creating Custom Tools

The commented code in `agent.py` shows how you could create a custom tool:

```python
def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
```

To use this tool:
1. Uncomment the function and its import
2. Add it to the agent's tools list: `tools=[get_current_time]`
3. Update the instructions to mention this tool

## Key Concepts

- **Tools**: Functions that agents can call to perform actions or retrieve information
- **Built-in Tools**: ADK provides several ready-to-use tools like `google_search`
- **Custom Tools**: You can define your own functions as tools for specialized capabilities

## Next Steps

Continue to [LiteLLM Agent](../3-litellm-agent) to learn how to work with different LLM providers beyond just Gemini.
