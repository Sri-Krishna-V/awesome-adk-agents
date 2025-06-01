# 🤖 Awesome ADK Agents

<p align="center">
  <img src="https://google.github.io/adk-docs/assets/agent-development-kit.png" width="200px" alt="Agent Development Kit">
</p>

<p align="center">
  <a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License: Apache 2.0"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
  <a href="https://github.com/google/adk-python"><img src="https://img.shields.io/badge/Powered%20by-Google%20ADK-yellow" alt="Powered by Google ADK"></a>
</p>

A curated collection of ready-to-use agents built with Google's Agent Development Kit (ADK). From simple helpers to complex multi-agent systems, this repository serves as both a learning resource and a practical toolkit for developers working with ADK.

<p align="center">
  <b>⭐ Star this repo to stay updated with new agents and features! ⭐</b>
</p>

## 📚 What is ADK?

[Agent Development Kit (ADK)](https://google.github.io/adk-docs/) is Google's flexible and modular framework for developing and deploying AI agents. While optimized for Gemini and the Google ecosystem, ADK is model-agnostic and deployment-agnostic, designed to make agent development feel more like software development.

ADK allows you to create, deploy, and orchestrate agent architectures ranging from simple tasks to complex workflows, with features like:

- 🧩 **Multi-agent system design** - Build applications with specialized agents working together
- 🛠️ **Rich tool ecosystem** - Equip agents with diverse capabilities through function tools
- 🔄 **Flexible orchestration** - Define complex workflows with sequential, parallel, and loop agents
- 🧪 **Integrated developer tooling** - Debug and visualize agent interactions with the dev UI
- 📡 **Native streaming support** - Create real-time, interactive experiences
- 📊 **Built-in agent evaluation** - Assess and improve agent performance systematically  

## 🔍 Overview

The **awesome-adk-agents** repository is a comprehensive collection of agent examples, templates, and production-ready implementations built using ADK. Whether you're just getting started with ADK or building sophisticated agent systems, this repository provides:

- 💻 **Practical Examples**: Learn ADK by examining real, working agents
- 🧰 **Templates**: Jump-start your development with pre-built agent structures
- 🚀 **Production-Ready Agents**: Deploy and use fully functional agents for common tasks
- 📚 **Learning Resources**: Progress from basic to advanced ADK concepts through tutorials

## 📂 Repository Structure

The repository is organized into categories based on agent complexity and use case:

### 🔬 Domain-Specific Agents

| Agent | Description | Category |
|-------|-------------|----------|
| [Academic Research](examples/academic-research/) | Research assistance with paper analysis | Research |
| [Brand Search Optimization](examples/brand-search-optimization/) | SEO and marketing optimization tools | Marketing |
| [Customer Service](examples/customer-service/) | Customer support automation | Business |
| [Data Science](examples/data-science/) | Analytics and data processing | Analytics |
| [Financial Advisor](examples/financial-advisor/) | Investment and financial planning | Finance |
| [FOMC Research](examples/fomc-research/) | Federal Reserve policy analysis | Finance |
| [LLM Auditor](examples/llm-auditor/) | Evaluation and improvement of LLM outputs | AI Safety |
| [Marketing Agency](examples/marketing-agency/) | Content creation and marketing tools | Marketing |
| [Personalized Shopping](examples/personalized-shopping/) | Customized retail recommendations | Retail |
| [RAG](examples/RAG/) | Retrieval-augmented generation implementations | Knowledge |
| [Software Bug Assistant](examples/software-bug-assistant/) | Programming help and debugging | Development |
| [Time Series Forecasting](examples/time-series-forecasting/) | Predictive analytics for temporal data | Analytics |
| [Travel Concierge](examples/travel-concierge/) | Trip planning and booking assistance | Travel |
| [YouTube Thumbnail Agent](examples/youtube-thumbnail-agent/) | Content optimization for video creators | Content |

### 🛠️ Utility Agents

| Agent | Description | Category |
|-------|-------------|----------|
| [Project Manager Agent](project-manager-agent/) | Tool for managing ADK agent projects | Development |

Each agent directory contains its own README with detailed instructions, requirements, and usage examples.

## 🚀 Getting Started

### Prerequisites

- Python 3.9+ or Java 17+
- Google ADK (`pip install google-adk`)
- API keys for LLMs (Gemini, GPT, Claude, etc. depending on agent)
- Additional requirements specified per-agent

### Installation

1. **Clone this repository**:

   ```bash
   git clone https://github.com/yourusername/awesome-adk-agents.git
   cd awesome-adk-agents
   ```

2. **Navigate to any agent directory** and follow its specific README instructions.

## 🧩 Agent Categories

The repository includes agents for various domains and use cases:

- 📊 **Data Processing**: ETL, analysis, and data transformation agents
- 🔄 **Autonomous Workflows**: Agents that complete complex multi-step tasks
- 🛠️ **Development Tools**: Coding assistants, project management, and DevOps agents
- 🔌 **API Wrappers**: Agents that simplify interactions with external services
- 📱 **Personal Assistants**: Task management, scheduling, and productivity agents
- 🧠 **Multi-Agent Systems**: Complex architectures with specialized sub-agents

## 💡 Use Cases

These agents can be used in many real-world scenarios:

- **Developers**: Automate code generation, testing, documentation, and project management
- **Researchers**: Literature review, data collection, and experimental design assistants
- **Marketers**: Content creation, SEO analysis, and campaign optimization
- **Support Teams**: Customer service automation and knowledge base management
- **Data Scientists**: Data cleaning, exploration, visualization, and model training
- **Enterprise**: Process automation, document management, and compliance monitoring

## 📝 Agent Structure

Each agent directory follows a consistent structure:

```
agent-name/
├── README.md                 # Description, usage, examples
├── agent_name/               # Main agent code
│   ├── __init__.py
│   ├── agent.py              # Core agent definition
│   ├── tools/                # Custom tools
│   ├── sub_agents/           # (If applicable)
│   └── shared_libraries/     # Utilities and shared code
├── deployment/               # Deployment configurations
├── tests/                    # Unit and integration tests
└── eval/                     # Evaluation datasets and metrics
```

## 🤝 How to Contribute

Contributions are welcome! Here's how you can help:

1. **Add a New Agent**: Build and submit a new agent implementation
2. **Improve Existing Agents**: Enhance functionality, fix bugs, or optimize performance
3. **Documentation**: Improve READMEs, add examples, or create tutorials
4. **Testing**: Add test cases or evaluation datasets

Please see our [Contributing Guidelines](CONTRIBUTING.md) for detailed instructions.

### Contribution Process

1. **Fork the Repository** - Create your own fork of the project
2. **Create a Branch** - Make a new branch for your contribution

   ```bash
   git checkout -b feature/amazing-agent
   ```

3. **Make Changes** - Implement your contribution following the structure guidelines
4. **Test Your Changes** - Ensure your agent works as expected
5. **Submit a Pull Request** - Open a PR against the main repository

## 🛣️ Roadmap

Future plans for this repository include:

- **Industry-Specific Agents**: Healthcare, finance, legal, and education
- **Multi-Modal Agents**: Agents working with images, audio, and video
- **Agent Evaluation Framework**: Standardized benchmarks and metrics
- **Deployment Templates**: Cloud-ready configurations for major platforms
- **Mobile Integration**: Agents optimized for mobile applications
- **Edge Deployment**: Lightweight agents for IoT and edge devices

## 📄 License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

## ✨ Credits

- Thanks to the [Google ADK team](https://github.com/google/adk-python) for creating ADK
- Contributors to this repository
- The broader AI agent community for inspiration and shared knowledge

---

<p align="center">
  <a href="https://github.com/yourusername/awesome-adk-agents/stargazers">
    <img src="https://img.shields.io/github/stars/yourusername/awesome-adk-agents?style=social" alt="GitHub stars">
  </a>
</p>

<p align="center">
  <i>This repository is not officially affiliated with Google or the ADK team. It is a community-driven collection of agent implementations.</i>
</p>
