# ADK Crash Course

This directory contains a progressive series of examples designed to teach the fundamentals of building agents with the Agent Development Kit (ADK). Each example builds on the previous one, introducing new concepts incrementally.

## Learning Path

Follow these examples in order to build your understanding from basic to advanced:

1. **Basic Agent** - Creating your first simple ADK agent
2. **Tool Agent** - Adding custom tools to your agent
3. **LiteLLM Agent** - Working with different LLM providers
4. **Structured Outputs** - Controlling agent output formats
5. **Sessions and State** - Implementing memory and context
6. **Persistent Storage** - Saving information across sessions
7. **Multi-Agent** - Creating a system with multiple agents
8. **Stateful Multi-Agent** - Building complex agent interactions
9. **Callbacks** - Adding hooks for monitoring and control
10. **Sequential Agent** - Implementing step-by-step workflows
11. **Parallel Agent** - Running multiple agents concurrently
12. **Loop Agent** - Creating agents with iterative processing

## Prerequisites

- Python 3.9+
- Google ADK (`pip install google-adk`)
- API keys for various LLMs (depends on example)

## Getting Started

Each example folder contains its own README with specific instructions, but the general process is:

1. Navigate to the example directory
2. Review the README for that example
3. Set up any required API keys
4. Run the example code
5. Experiment with modifications

## Example Structure

Each example typically follows this structure:

```
example-name/
├── README.md           # Instructions and explanation
├── agent_name/         # Main agent code
│   ├── __init__.py
│   ├── agent.py        # Core agent definition
│   └── tools/          # (If applicable)
└── requirements.txt    # Dependencies
```

## Recommended Learning Approach

1. **Start with the basics**: Understand how a simple agent works before moving to more complex examples
2. **Read the code**: Each example is thoroughly commented to explain key concepts
3. **Modify and experiment**: After running an example, try changing parameters and behavior
4. **Build your own**: After completing the crash course, try creating your own agent from scratch

Happy learning!
