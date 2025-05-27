# 1. Basic Agent

This example introduces the fundamental building block of ADK: a simple greeting agent.

## What You'll Learn

- How to set up a basic ADK agent
- Core agent components (name, model, description, instruction)
- Running your first agent

## Agent Overview

The greeting agent is the simplest possible ADK agent:
- It uses Gemini 2.0 Flash as its model
- It's instructed to greet users and ask for their name
- It has no additional tools or capabilities

## Code Walkthrough

```python
from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",
    description="Greeting agent",
    instruction="""
    You are a helpful assistant that greets the user. 
    Ask for the user's name and greet them by name.
    """,
)
```

This minimal code creates a fully functional agent:

1. `name`: Identifies the agent
2. `model`: Specifies which LLM powers the agent
3. `description`: Provides a short summary of the agent's purpose
4. `instruction`: Defines the agent's behavior

## Running the Agent

1. Create a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

2. Run the agent:
   ```bash
   cd greeting_agent
   python -m google.adk run
   ```

3. Interact with your agent in the terminal

## Key Concepts

- **Agent**: The core unit in ADK, representing an AI assistant with specific capabilities
- **Instruction**: The "system prompt" that guides the agent's behavior
- **Model**: The underlying large language model (Gemini, GPT, etc.)

## Next Steps

Once you understand this basic example, you're ready to move on to [Tool Agent](../2-tool-agent), where you'll learn how to enhance your agent with custom capabilities.
