# 🚀 ADK Crash Course

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4.svg)](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder)
[![Tutorial](https://img.shields.io/badge/Tutorial-Video-red.svg)](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s)

> **🎥 HIGHLY RECOMMENDED**: Watch the [ADK Crash Course Video](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s) by Brandon Hancock for the best explanation and implementation guide!

This directory contains a progressive series of 12 hands-on examples designed to teach the fundamentals of building agents with Google's Agent Development Kit (ADK). Each example builds on the previous one, introducing new concepts incrementally from basic agents to complex multi-agent systems.

## 📚 Learning Path

Follow these examples in **sequential order** to build your understanding from basic to advanced concepts:

| # | Example | Description | Key Concepts |
|---|---------|-------------|--------------|
| 1 | **[Basic Agent](./1-basic-agent/)** | Creating your first simple ADK agent | Agent fundamentals, initialization |
| 2 | **[Tool Agent](./2-tool-agent/)** | Adding custom tools to your agent | Custom tools, function calling |
| 3 | **[LiteLLM Agent](./3-litellm-agent/)** | Working with different LLM providers | Multi-provider support, flexibility |
| 4 | **[Structured Outputs](./4-structured-outputs/)** | Controlling agent output formats | Response formatting, data validation |
| 5 | **[Sessions and State](./5-sessions-and-state/)** | Implementing memory and context | State management, conversation memory |
| 6 | **[Persistent Storage](./6-persistent-storage/)** | Saving information across sessions | Data persistence, storage solutions |
| 7 | **[Multi-Agent](./7-multi-agent/)** | Creating a system with multiple agents | Agent coordination, distributed systems |
| 8 | **[Stateful Multi-Agent](./8-stateful-multi-agent/)** | Building complex agent interactions | Advanced coordination, shared state |
| 9 | **[Callbacks](./9-callbacks/)** | Adding hooks for monitoring and control | Event handling, monitoring, logging |
| 10 | **[Sequential Agent](./10-sequential-agent/)** | Implementing step-by-step workflows | Sequential processing, workflow design |
| 11 | **[Parallel Agent](./11-parallel-agent/)** | Running multiple agents concurrently | Concurrent processing, performance |
| 12 | **[Loop Agent](./12-loop-agent/)** | Creating agents with iterative processing | Iterative workflows, continuous processing |

## ⚡ Quick Start

### Prerequisites

- **Python 3.9+** (Python 3.11+ recommended)
- **Google ADK**: `pip install google-adk`
- **Google API Key** from [Google AI Studio](https://aistudio.google.com/)
- Basic Python knowledge

### Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up Environment Variables**
   Create a `.env` file:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

3. **Start Learning**
   Navigate to the first example:
   ```bash
   cd 1-basic-agent/
   ```

## 🏗️ Project Structure

Each example follows this consistent structure:

```text
example-name/
├── README.md           # Instructions and explanation
├── agent_name/         # Main agent code
│   ├── __init__.py
│   ├── agent.py        # Core agent definition
│   └── tools/          # Custom tools (if applicable)
└── requirements.txt    # Dependencies
```

## 🎯 Recommended Learning Approach

1. **📺 Watch First**: Start with the [video tutorial](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s) for visual learning
2. **🔍 Start with the basics**: Understand how a simple agent works before moving to complex examples
3. **📖 Read the code**: Each example is thoroughly commented to explain key concepts
4. **🧪 Modify and experiment**: After running an example, try changing parameters and behavior
5. **🚀 Build your own**: After completing the crash course, create your own agent from scratch

## 🔗 Navigation

- **[⬅️ Back to AI with Brandon Examples](../README.md)**
- **[🎬 Watch the Video Tutorial](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s)**
- **[📚 Start with Example 1: Basic Agent](./1-basic-agent/)**

## 🙏 Credits

Created by **[Brandon Hancock](https://github.com/bhancockio)** - Thank you for making ADK learning accessible to everyone!

## 📄 License

Please refer to the original creator's licensing terms.

---

**Ready to start building intelligent agents?** 🤖 Begin your journey with [Example 1: Basic Agent](./1-basic-agent/)!
