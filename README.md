# 🤖 Awesome ADK Agents

<p align="center"><img src="https://google.github.io/adk-docs/assets/agent-development-kit.png" width="200px" alt="Agent Development Kit">
</p>
<p align="center">
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License: Apache 2.0"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
  <a href="https://github.com/google/adk-python"><img src="https://img.shields.io/badge/Powered%20by-Google%20ADK-yellow" alt="Powered by Google ADK"></a>
    <a href="https://www.reddit.com/r/agentdevelopmentkit/"><img src="https://img.shields.io/badge/Reddit-r%2Fagentdevelopmentkit-FF4500?style=flat&logo=reddit&logoColor=white" alt="Reddit: r/agentdevelopmentkit"></a>

> A curated collection of AI agents built with Google's Agent Development Kit (ADK) for various domains, applications and use-cases.

## 📖 Table of Contents

- [What is Google's Agent Development Kit (ADK)?](#what-is-googles-agent-development-kit-adk)
- [🚀 Getting Started](#-getting-started--installation)
- [✨ Agent Showcase](#-agent-showcase)
  - [My ADK Agents](#my-adk-agents)
  - [Examples from Google Agent Garden](#examples-from-google-agent-garden)
  - [Examples from aiwithbrandon Collection](#examples-from-aiwithbrandon-collection)
- [🚀 Getting Started / Installation](#-getting-started--installation)
- [🛠️ Usage](#️-usage)
- [🗺️ Roadmap](#️-roadmap)
- [🤝 How to Contribute](#-how-to-contribute)
- [❓ How to Get Help / Report Issues](#-how-to-get-help--report-issues)
- [🙏 Credits and Acknowledgements](#-credits-and-acknowledgements)
- [⭐ Call to Action](#-call-to-action)

##

>Welcome to **Awesome ADK Agents**👋👋

From simple helpers to complex multi-agent systems, this repository will serve as a comprehensive resource for anyone interested in building AI agents using Google's Agent Development Kit (ADK).

### Who is this for?

>- Peeps looking to build AI agents with Google's ADK
>- Peeps who want templates and examples to kickstart their projects
>- Peeps who want to build production-ready agents with best practices

## What is Google's Agent Development Kit (ADK)?

Agent Development Kit (ADK) is a flexible and modular framework for developing and deploying AI agents. While optimized for Gemini and the Google ecosystem, ADK is model-agnostic, deployment-agnostic, and is built for compatibility with other frameworks. ADK was designed to make agent development feel more like software development, to make it easier for developers to create, deploy, and orchestrate agentic architectures that range from simple tasks to complex workflows.

### 🗝️ Key Features

- **Rich Tool Ecosystem**: Utilize pre-built tools, custom functions,
  OpenAPI specs, or integrate existing tools to give agents diverse
  capabilities, all for tight integration with the Google ecosystem.

- **Code-First Development**: Define agent logic, tools, and orchestration
  directly in Python for ultimate flexibility, testability, and versioning.

- **Modular Multi-Agent Systems**: Design scalable applications by composing multiple specialized agents into flexible hierarchies.

- **Deploy Anywhere**: Easily containerize and deploy agents on Cloud Run or scale seamlessly with Vertex AI Agent Engine.

## ✨ Agent Showcase

### My ADK Agents

| Agent Name | Category/Domain | Short Description |
|------------|----------------|-------------------|
| [Job Interview Agent](./job-interview-agent/) | HR/Recruitment | AI-powered interview assistant with calendar integration and real-time feedback |
| [Project Manager Agent](./project-manager-agent/) | Productivity/Management | Automated project management with task tracking and progress monitoring |
| [Local RAG Agent (WIP)](./my_custom_agents/advanced_rag_agent/) | Information Retrieval | Enhanced RAG implementation with vector search and context optimization |

### Courses on ADK

- 📚 [ADK Crash Course by Brandon Hancock](https://github.com/bhancockio/agent-development-kit-crash-course)
  - A fabulous curation for beginners covering the fundamentals of ADK, from basic agent creation to advanced workflows and multi-agent systems.

- 📚 [chongdashu/adk-made-simple](https://github.com/chongdashu/adk-made-simple)
  - From basics to A2A integration, this course explores real world applications and projects

- 📚 [theailifestyle/google-adk-demos](https://github.com/theailifestyle/google-adk-demos)
  - A collection of practical demos showcasing various ADK features and capabilities

#### 🔬 Research & Analysis

- 📚 [Academic Research Agent](https://github.com/google/adk-samples/tree/main/python/agents/academic-research): Comprehensive research assistant for academic papers and citations
- 📊 [Data Science Agent](https://github.com/google/adk-samples/tree/main/python/agents/data-science): Automated data analysis and visualization workflows
- 📈 [Time Series Forecasting Agent](https://github.com/google/adk-samples/tree/main/java/agents/time-series-forecasting): Advanced predictive analytics for time-based data
- 🏛️ [FOMC Research Agent](https://github.com/google/adk-samples/tree/main/python/agents/fomc-research): Federal Reserve meeting analysis and insights

#### 💼 Business & Customer Service

- 🛡️ [Auto Insurance Agent](https://github.com/google/adk-samples/tree/main/python/agents/auto-insurance-agent): Automated insurance claim processing and customer support
- 🎯 [Brand Search Optimization](https://github.com/google/adk-samples/tree/main/python/agents/brand-search-optimization): SEO and brand visibility enhancement for products in retail websites
- 📞 [Customer Service Agent](https://github.com/google/adk-samples/tree/main/python/agents/customer-service): Multi-channel customer support automation
- 💰 [Financial Advisor](https://github.com/google/adk-samples/tree/main/python/agents/financial-advisor): Personalized financial planning and investment advice

#### 🛍️ E-commerce & Marketing

- 🛒 [Personalized Shopping](https://github.com/google/adk-samples/tree/main/python/agents/personalized-shopping): AI-driven product recommendations and shopping assistance
- 📱 [Marketing Agency](https://github.com/google/adk-samples/tree/main/python/agents/marketing-agency): Comprehensive digital marketing campaign management
- ✈️ [Travel Concierge](https://github.com/google/adk-samples/tree/main/python/agents/travel-concierge): Intelligent travel planning and booking assistance

#### 🔧 Development & Technical

- 🐛 [Software Bug Assistant](https://github.com/google/adk-samples/tree/main/java/agents/software-bug-assistant): Automated bug detection and resolution suggestions to help IT Support and SDE
- 🔍 [LLM Auditor](https://github.com/google/adk-samples/tree/main/python/agents/llm-auditor)Model performance evaluation and optimization
- 📚 [RAG Systems](https://github.com/google/adk-samples/tree/main/python/agents/RAG): Advanced Retrieval-Augmented Generation implementations

---

#### 🧠 Advanced Techniques

- 📖 [RAG Agent Tutorial](https://github.com/bhancockio/adk-rag-agent): Complete RAG implementation with ADK and Vertex AI

- 🎤 [Voice-Enabled Agent](https://github.com/bhancockio/adk-voice-agent): Speech-to-text and voice interaction capabilities with G-Calendar integration

- 🔌 [MCP Integration Tutorial](https://github.com/bhancockio/adk-mcp-tutorial): Model Context Protocol (Both local and remote) with ADK

- 🎨 [YouTube Thumbnail Agent](https://github.com/bhancockio/adk-youtube-thumbnail-agent): Automated thumbnail generation and optimization


### 💹 Trading & Finance

- 📈 [Agentic Trading Simulator](https://github.com/kweinmeister/agentic-trading): Multi-agent trading system with risk management, featuring AlphaBot (SMA strategy) and RiskGuard agents communicating via A2A protocol


## 🚀 Getting Started / Installation

👋 **New to ADK agents?** Check out our comprehensive [**Getting Started Guide**](./GETTING_STARTED.md) for step-by-step instructions!

### Quick Start

Follow these steps to set up the repository and start working with ADK agents:

### Clone the Repository

```bash
git clone https://github.com/[YOUR_USERNAME]/awesome-adk-agents.git
cd awesome-adk-agents
```

## 🛠️ Usage

### General Workflow

1. **Navigate to an Agent Directory**: Choose either a custom agent or an example:

   ```bash
   # For custom agents
   cd job-interview-agent/
   
   # For Google Agent Garden examples
   cd examples/google_agent_garden/academic-research/
   
   # For aiwithbrandon examples
   cd examples/_aiwithbrandon/adk-rag-agent/
   ```

2. **Follow Agent-Specific Instructions**: Each agent has its own `README.md` with detailed setup and usage instructions.

    Generally, the setup involves:

    - Creating a Python virtual environment

        ```bash
        python -m venv .venv
        source .venv/bin/activate  # macOS/Linux
        .venv\Scripts\activate  # Windows
        ```

    - Installing dependencies

        ```bash
        pip install -r requirements.txt
        ```

3. **Common Commands of ADK**:

   ```bash
    Usage: adk [OPTIONS] COMMAND [ARGS]...

    Agent Development Kit CLI tools.

    Options:
        --help  Show this message and exit.

        Commands:
        web         Starts a FastAPI server with Web UI for agents(Mostly used)
        api_server  Starts a FastAPI server for agents
        create      Creates a new app in the current folder with prepopulated agent...
        deploy      Deploys agent to hosted environments
        eval        Evaluates an agent given the eval sets
        run         Runs an interactive CLI for a certain agent
        
   ```

### Tips for Success

- **Read Each Agent's README**: Setup requirements and usage patterns vary between agents
- **Check Dependencies**: Install agent-specific requirements before running
- **Environment Variables**: Many agents require specific environment variables for API keys
- **Test in Development**: Always test agents in a safe environment before production use

## 🗺️ Roadmap

Our future plans for this repository include:

- 🧠 **Advanced Custom Agents**: More sophisticated agents for specialized domains (healthcare, legal, scientific research)
- 📚 **Comprehensive Tutorials**: Step-by-step guides for building agents from scratch
- 🔄 **ADK Feature Showcases**: Examples highlighting new ADK capabilities as they're released
- 🎯 **Domain-Specific Collections**: Curated agent collections for specific industries
- 🤖 **Multi-Modal Agents**: Agents that work with text, image, audio, and video

## 🤝 How to Contribute

We welcome contributions from the community! Here's how you can help:

### Contributing Your Own Agents

1. **Fork this repository**
2. **Create a feature branch**: `git checkout -b feature/your-agent-name`
3. **Add your agent**: Place it in the appropriate directory with comprehensive documentation
4. **Update the README**: Add your agent to the relevant showcase section
5. **Submit a Pull Request**: Include a clear description of your agent's functionality

### Reporting Issues or Suggestions

- 🐛 **Bug Reports**: Found an issue with an existing agent?
- 💡 **Feature Requests**: Have ideas for new agents or improvements?
- 📚 **Documentation**: Spotted unclear or missing documentation?

### Contribution Guidelines

For detailed contribution guidelines, coding standards, and submission requirements, please see [CONTRIBUTING.md](./CONTRIBUTING.md).

**Remember**: All contributions should follow Google ADK best practices and include appropriate documentation.

## ❓ How to Get Help / Report Issues

Need assistance or found a problem? We're here to help!

**For issues, questions, or suggestions, please [open an issue](https://github.com/[YOUR_USERNAME]/awesome-adk-agents/issues) on this repository.**

When reporting issues, please include:

- Agent name and directory path
- Steps to reproduce the problem
- Error messages or unexpected behavior
- Your environment details (Python version, ADK version, OS)

For general ADK questions, you may also want to check:

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Google ADK GitHub Discussions](https://github.com/google/adk-python/discussions)

## 🙏 Credits and Acknowledgements

This repository wouldn't be possible without the amazing work and contributions from:

- **Google ADK Team**: For creating an exceptional framework for AI agent development
- **Google Agent Garden**: For providing comprehensive, production-quality agent examples
- **Brandon Hancock**: For creating educational ADK content and tutorials that help developers learn

Special thanks to the developers and researchers pushing the boundaries of AI agent capabilities with Google's tools and technologies.

## ⭐ Call to Action

If you find this repository useful for your AI agent development journey, please consider:

- **⭐ Starring this repository** to help others discover it
- **🔗 Sharing it** with fellow developers and AI enthusiasts
- **🤝 Contributing** your own agents or improvements
- **📢 Spreading the word** about Google ADK and its capabilities

Together, we can build an amazing collection of AI agents that showcase the power and versatility of Google's Agent Development Kit!

---

*Happy agent building! 🤖✨*
