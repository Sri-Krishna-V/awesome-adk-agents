<div align="center">
  <h1>
    Awesome ADK Agents 
    <a href="https://awesome.re">
      <img src="https://awesome.re/badge.svg" alt="Awesome">
    </a>
  </h1>
</div>

<p align="center"><img src="https://google.github.io/adk-docs/assets/agent-development-kit.png" width="200px" alt="Agent Development Kit">
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/sri-krishna-v/awesome-adk-agents?style=flat-square" alt="Stars">
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
  <a href="https://github.com/google/adk-python"><img src="https://img.shields.io/badge/Powered%20by-Google%20ADK-yellow" alt="Powered by Google ADK"></a>
  <a href="https://www.reddit.com/r/agentdevelopmentkit/"><img src="https://img.shields.io/badge/Reddit-r%2Fagentdevelopmentkit-FF4500?style=flat&logo=reddit&logoColor=white" alt="Reddit: r/agentdevelopmentkit"></a>
  <a href="https://deepwiki.com/google/adk-python"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

_The most comprehensive curated collection for Google's Agent Development Kit (ADK) - featuring **90+ production-ready agents, templates, and resources** from hackathon winners, industry experts, and the vibrant ADK community. From beginner tutorials to enterprise-grade multi-agent systems, discover battle-tested solutions for research, business automation, education, content creation, and specialized domains._

## 📖 Table of Contents

- [🎯 What This List Solves](#-what-this-list-solves)
- [What is Google's Agent Development Kit (ADK)?](#what-is-googles-agent-development-kit-adk)
- [🏆 Featured Projects](#-featured-projects)
- [🏆 ADK Hackathon Winners](#-adk-hackathon-winners)
- [🚀 Templates & Starters](#-templates--starters)
- [🌟 Community Excellence](#-community-excellence)
- [📚 Learning Resources](#-learning-resources)
- [🎯 Official Examples](#-official-examples)
- [🚀 Getting Started / Installation](#-getting-started--installation)
- [🙏 Credits and Acknowledgements](#-credits-and-acknowledgements)
- [⭐ Call to Action](#-call-to-action)

##

> Welcome to **Awesome ADK Agents**👋👋

From simple helpers to complex multi-agent systems, this repository will serve as a comprehensive resource for anyone interested in building AI agents using Google's Agent Development Kit (ADK).

## 🎯 What This List Solves

Building production-ready AI agents with Google's ADK shouldn't require starting from scratch or piecing together fragmented tutorials. This curated collection addresses three critical challenges that slow down agent development:

### 1. **Template Discovery & Quality Gap**

- **Problem**: Most developers waste weeks searching for reliable starting points and end up with toy examples that don't scale
- **Solution**: Curated, battle-tested templates and real-world implementations you can actually build upon

### 2. **Production Readiness Barrier**

- **Problem**: Tutorials teach basics, but deploying robust, scalable agents requires understanding integration patterns, error handling, and deployment strategies
- **Solution**: Production-ready examples with complete implementation details, from development to deployment

### 3. **Implementation Learning Curve**

- **Problem**: The jump from "Hello World" tutorials to building meaningful solutions feels overwhelming
- **Solution**: Progressive examples that bridge theory and practice, showing how real developers solve actual problems

**Whether you're a beginner looking for solid foundations or an experienced developer seeking proven patterns, this repository eliminates the trial-and-error phase and accelerates your path to production-ready agents.**

## What is Google's Agent Development Kit (ADK)?

**Google's Agent Development Kit (ADK)** is a Python framework that makes building AI agents feel like software development. Model-agnostic and deployment-flexible, ADK simplifies creating everything from single-purpose tools to complex multi-agent systems.

### 🗝️ Key Features

- **🛠️ Rich Tool Ecosystem**: Pre-built tools, custom functions, OpenAPI specs, and Google ecosystem integration
- **💻 Code-First Development**: Define agents in Python with full testability and version control
- **🔗 Multi-Agent Orchestration**: Compose specialized agents into scalable hierarchies
- **🚀 Deploy Anywhere**: Cloud Run, Vertex AI Agent Engine, or any containerized environment

## 🏆 Featured Projects

_My showcase agents demonstrating production-ready ADK implementations_

| Agent Name | Category/Domain | Short Description | Badges |
|------------|----------------|-------------------|---------|
| [Job Interview Agent](./my-adk-agents/job-interview-agent/) | HR/Recruitment | AI-powered interview assistant with calendar integration and real-time feedback | ⭐🏭🟡 |
| [Education Path Advisor for India](./my-adk-agents/education-path-advisor/) | Education/Career Guidance | Multi-agent AI advisor for Indian students/parents: personalized pathways, stepwise plans, risk analysis, and region/reservation-aware guidance | ⭐🟡 |
| [Academic Research Assistant](./my-adk-agents/academic-research-assistant/) | Research/Academia | Multi-agent literature review assistant with profile analysis, robust paper search (with SerpAPI fallback), and personalized research synthesis | 🟡 |
| [Project Manager Agent](./my-adk-agents/project-manager-agent/) | Productivity/Management | Automated project management with task tracking and progress monitoring | 🟡 |
| [Learning Content System (WIP)](./my-adk-agents/local-rag-agent/) | Information Retrieval | Enhanced RAG implementation with vector search and context optimization using pgvector and PostgreSQL | 🚧🟡 |

**Badge Legend:**

- ⭐ **My Showcase** - Featured portfolio projects
- 🏭 **Production-Ready** - Has deployment code and infrastructure
- 🔥 **Community Pick** - Outstanding community contributions
- 🚧 **In Development** - Work in progress
- 📚 **Learning Resource** - Educational/tutorial content (official examples are demo/educational only)
- 🟢🟡🔴 **Difficulty**: Beginner, Intermediate, Advanced

---

## 🏆 ADK Hackathon Winners

_Outstanding projects from the Agent Development Kit Hackathon with Google Cloud (May 12 - June 23, 2025)_

> **🎉 $50,000 in prizes awarded** | **476 submissions** | **10,432 participants worldwide**
> 
> [View all submissions](https://googlecloudmultiagents.devpost.com/project-gallery) | [Hackathon details](https://googlecloudmultiagents.devpost.com/)

### 🥇 Grand Prize Winner ($15,000)

- 🏆 **[TradeSage AI](https://devpost.com/software/tradesage-ai)** 🏭🔴🔥 - Intelligent multi-agent financial analysis platform that revolutionizes trading hypothesis evaluation using ADK, Agent Engine, Cloud Run and Vertex AI

### 🌍 Regional Winners ($8,000 each)

- 🌎 **North America**: [Energy Agent AI](https://devpost.com/software/energy-agent-ai) 🏭🟡🔥 - Multi-agent AI transforming energy customer management through Google ADK orchestration
- 🌍 **Europe/Middle East/Africa**: [Bleach](https://devpost.com/software/bleach-7tqdmo) 🟡🔥 - Visual AI agent builder for Google ADK with plain English descriptions, visual design, and instant testing
- 🌏 **Asia Pacific**: [Edu.AI](https://devpost.com/software/edu-ai-multi-agent-educational-system-for-brazil) 🟡🔥 - Multi-agent educational system democratizing Brazil's education with autonomous AI agents
- 🌎 **Latin America**: [SalesShortcut](https://devpost.com/software/salesshortcut) 🏭🟡🔥 - Comprehensive AI-powered Sales Development Representative system with multi-agent architecture

### 🎖️ Honorable Mentions ($1,000 each)

- 🧪 [Particle Physics Agent](https://devpost.com/software/particle-physics-agent) 🔴🔥 - Physics AI agent converting natural language into validated Feynman diagrams using real physical laws
- ♻️ [GreenOps](https://devpost.com/software/greenops-gzp4aj) 🟡🔥 - Multi-agent system optimizing operational costs while reducing carbon emissions
- 🎓 [Nexora-AI](https://devpost.com/software/teachai-upzofa) 🟡🔥 - Next-gen personalized education with interactive lessons, visuals, and smart AI support

### 🌟 Notable Submissions

- 🎮 [Lucilla AI Agent Game Studio](https://devpost.com/software/lucilla-ai-agent-game-studio) 🔴🔥 - World's most comprehensive AI game agent platform with fully functional microservices
- 🛡️ [GuardianOS](https://devpost.com/software/guardianos) 🔴🔥 - Multi-agent compliance and monitoring system for privacy-preserving blockchain transactions
- 🌾 [AgriFlow Nexus](https://devpost.com/software/agriflow-nexus) 🟡🔥 - AI-powered platform slashing SADC farm-to-market costs with price prediction and sustainability grading
- 🛠️ [DA-Forge](https://devpost.com/software/da-forge-autonomous-developer-agent) 🔴🔥 - Autonomous developer agent turning text instructions into working automation workflows
- 🚗 [Let's ON:DRIVE](https://devpost.com/software/let-s-on-drive) 🟡🔥 - Emotion-aware AI assistant preventing drowsy driving accidents
- 📊 [Vendo AI](https://devpost.com/software/vendo-ai) 🏭🟡🔥 - Analytics co-pilot connecting to data and helping teams make faster, smarter decisions

**Hackathon Highlights:**
- **476 total submissions** from global developers
- **Multi-agent focus**: All projects showcase collaborative AI systems
- **Categories**: Automation, Data Analysis, Customer Service, Content Creation
- **Google Cloud Integration**: Heavy use of ADK, Vertex AI, Cloud Run, BigQuery
- **Innovation**: Novel applications across physics, education, finance, sustainability, and gaming

---

## 🚀 Templates & Starters

_Ready-to-use templates to kickstart your ADK projects_

- 🚀 [GoogleCloudPlatform/agent-starter-pack](https://github.com/GoogleCloudPlatform/agent-starter-pack) 🏭🟢 - Production-ready Generative AI Agent templates for Google Cloud with ADK samples, comprehensive deployment infrastructure
- 🔥 [Gemini Fullstack ADK Quickstart](https://github.com/google/adk-samples/tree/main/python/agents/gemini-fullstack) 🏭🟡⭐ - **The gold standard**: Complete fullstack research agent with React frontend, human-in-the-loop workflows, autonomous research pipelines, and Cloud Run deployment
- 📱 [kkdai/linebot-adk](https://github.com/kkdai/linebot-adk) 🏭🟢 - LINE Bot template with Docker, Cloud Run deployment, and security configurations  
- 🌐 [phamvuhoang/google-adk-nextjs-starter](https://github.com/phamvuhoang/google-adk-nextjs-starter) 🟢 - Next.js starter template for Google ADK projects with Angular frontend
- 🎨 [abhishekkumar35/google-adk-nocode](https://github.com/abhishekkumar35/google-adk-nocode) 🟢 - Visual, no-code interface for creating AI agents (supports cloud and local Ollama models)

---

## 🌟 Community Excellence

_Outstanding community projects showcasing ADK capabilities_

### Multi-Agent Systems

- 🔥 [Parth0248/Forkcast](https://github.com/Parth0248/Forkcast) 🏭🟡 - Multi-agent AI system for collaborative dining decisions with deployed webapp, technical reports, and Cloud Run deployment
- 🚀 [kweinmeister/agentic-trading](https://github.com/kweinmeister/agentic-trading) 🏭🔴 - Multi-agent trading system with risk management, featuring AlphaBot and RiskGuard agents with complete A2A protocol implementation and production deployment
- 📊 [vladkol/CRM Data Q&A Agent](https://github.com/vladkol/crm-data-agent) 🏭🔴 - Multi-agentic system with Advanced RAG and NL2SQL over Salesforce Data, "Run on Google Cloud" deployment
- 🏙️ [M-JULIANI/nyc-monitor](https://github.com/M-JULIANI/nyc-monitor) 🟡🏭🔥 - AI-powered urban intelligence system for real-time NYC event analysis and reporting with multi-agent architecture and automated Google Slides reports

### Integration & Advanced Patterns

- 🔌 [RubensZimbres/A2A_ADK_MCP](https://github.com/RubensZimbres/A2A_ADK_MCP) 🔴 - Multi-Agent Systems using Google's ADK + A2A + MCP
- 🎤 [bhancockio/Voice-Enabled-Agent](https://github.com/bhancockio/adk-voice-agent) 🟡 - Speech-to-text and voice interaction capabilities with G-Calendar integration and comprehensive setup documentation
- 🔗 [serkanyasr/mcp-agent-tool-adapter](https://github.com/serkanyasr/mcp-agent-tool-adapter) 🟡 - Converts MCP tools into Google ADK or LangGraph agents with streaming FastAPI/CLI
- 🔧 [codeninja/Mongoose Migration Agent System](https://gist.github.com/codeninja/a6e117a3480de8d32dd9ef01b519cdae) 🔴🔥 - Multi-agent system for automated Mongoose database migration (v6→v8) with specialized agents and MCP integration

### Agent Development & Engineering Platforms

- 🛠️ [VidyutChakrabarti/AgentFlux](https://github.com/VidyutChakrabarti/AgentFlux) 🏭🔴🔥 - Agent engineering platform with interactive playgrounds, graph visualization, automated refinement loops, and fine-tuned models for prompt optimization

### Domain-Specific Applications

- 💰 [mtwn105/zerodha-mcp](https://github.com/mtwn105/zerodha-mcp) 🟡 - Zerodha MCP Server & Client integrating Google ADK for financial applications
- 📈 [sudsk/tradesage-mvp](https://github.com/sudsk/tradesage-mvp) 🏭🟡 - Multi-agent trading hypothesis analysis system with 6 specialized agents and Cloud Run deployment
- ✈️ [AashiDutt/Google-Agent-Development-Kit-Demo](https://github.com/AashiDutt/Google-Agent-Development-Kit-Demo) 🟢 - ADK-powered travel planner
- 📊 [jenyss/google-adk-data-visualization-agent](https://github.com/jenyss/google-adk-data-visualization-agent) 🟡 - Data visualization agent built with Google ADK
- 🏥 [Ahsan462aggk/Medical_Search_Pro_Agent](https://github.com/Ahsan462aggk/Medical_Search_Pro_Agent) 🟡🏭 - Multi-agent biomedical research system with PubMed search, analysis, and email delivery
- 🧠 [IhateCreatingUserNames2/Cognisphere](https://github.com/IhateCreatingUserNames2/Cognisphere) 🔴 - AI agent development framework built on Google's ADK
- 🎨 [bhancockio/YouTube-Thumbnail-Agent](https://github.com/bhancockio/adk-youtube-thumbnail-agent) 🟢 - Automated thumbnail generation and optimization
- 📊 [AI Trends Analysis Pipeline](https://github.com/Astrodevil/ADK-Agent-Examples/tree/main/analyzer_agent) 🟡🔥 - Comprehensive AI analysis pipeline using Exa Search, Tavily Search, Firecrawl and Nebius AI
- 📁 [Job Finder Agent](https://github.com/Astrodevil/ADK-Agent-Examples/tree/main/jobfinder_agent) 🟡 - Sequential Agent using Mistral OCR, Linkup API and Nebius AI
- 📧 [Email ADK Agent](https://github.com/Astrodevil/ADK-Agent-Examples/tree/main/email_adk_agent) 🟢 - Email management and automation agent using Resend API
- 📦 [arjunprabhulal/MCP-Gemma-3-Agent](https://github.com/arjunprabhulal/adk-mcp-gemma3) 🟡 - Gemma 3 leveraged by Ollama, MCP Youtube Search

---

## 📚 Learning Resources

_Comprehensive guides, tutorials, and educational content_

### 🚀 Quickstart Courses

- 📚 [ADK Crash Course by Brandon Hancock](https://github.com/bhancockio/agent-development-kit-crash-course) 🟢📚 - Fundamentals of ADK, from basics to advanced workflows and multi-agent systems with [Youtube](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=2659s) tutorial
- 📚 [A2A Crash Course by Brandon Hancock](https://github.com/bhancockio/agent2agent) 🟡📚 - Comprehensive guide to building agent-to-agent (A2A) communication using ADK with [Youtube](https://www.youtube.com/watch?v=mFkw3p5qSuA&t=172s) tutorial  
- 📚 [chongdashu/adk-made-simple](https://github.com/chongdashu/adk-made-simple) 🟢📚 - From basics to A2A integration with real world applications and projects
- 📚 [theailifestyle/google-adk-demos](https://github.com/theailifestyle/google-adk-demos) 🟢📚 - Collection of practical demos showcasing various ADK features

### 🧪 Official Hands-on Learning

- 🧪 [Google ADK Codelabs](https://codelabs.developers.google.com/?text=ADK) ⭐📚 - Interactive, guided tutorials with hands-on coding exercises from Google

### 📖 Tutorials & Walkthroughs

- 📖 [chongdashu/adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course) 🟡📖🔥 - Complete multi-agent system with ADK + A2A + MCP integration, featuring Notion and ElevenLabs with full architecture, testing, and [YouTube](https://www.youtube.com/watch?v=s6-Ofu-uu2k) tutorial
- 📖 [mongodb-developer/MongoDB-ADK-Agents](https://github.com/mongodb-developer/MongoDB-ADK-Agents) 🟡📖💡 - Official MongoDB grocery shopping agent implementation with Vector Search, complete dataset, and step-by-step setup - companion repository  for the MongoDB Atlas tutorial
- 📖 [datascalehq/datascale](https://github.com/datascalehq/datascale/tree/main/cookbook/tutorials/agent_docs) 🟡📖🔥 - Multi-agent documentation builder with planner and writer agents that automatically analyze codebases and generate structured knowledge bases - companion repository for the codebase documentation article
- 📖 [meteatamel/adk-demos](https://github.com/meteatamel/adk-demos/) 🟢📖 - Collection of demos and tutorials for Google's Agent Development Kit
- 📖 [sokart/adk-walkthrough](https://github.com/sokart/adk-walkthrough) 🟡📖 - Step-by-step guides and examples using the open-source Python ADK framework
- 📖 [bhancockio/RAG-Agent-Tutorial](https://github.com/bhancockio/adk-rag-agent) 🟡📖 - Complete RAG implementation with ADK and Vertex AI with [YouTube](https://www.youtube.com/watch?v=TvW4A0a75mw&t=14s) tutorial
- 📖 [bhancockio/MCP Integration Tutorial](https://github.com/bhancockio/adk-mcp-tutorial) 🟡📖 - Model Context Protocol (both local and remote) with ADK with [Youtube](https://www.youtube.com/watch?v=HkzOrj2qeXI&t=2362s) tutorial

### 📝 Articles & Best Practices

- 📝 [From Zero to Multi-Agents: A Beginner's Guide to Google ADK](https://medium.com/@sokratis.kartakis/from-zero-to-multi-agents-a-beginners-guide-to-google-agent-development-kit-adk-b56e9b5f7861) 🟢📝 - Step-by-step beginner guide by Dr Sokratis Kartakis
- 📝 [Choosing the Right Deployment Path for Your Google ADK Agents](https://medium.com/google-cloud/choosing-the-right-deployment-path-for-your-google-adk-agents-86c89c251ab5) 🟡📝🏭 - Official Google Cloud guide comparing deployment strategies (Cloud Run vs Vertex AI vs GKE) for production ADK agents
- 📝 [Build a Python AI Agent in 15 Minutes with Google ADK and MongoDB Atlas Vector Search](https://medium.com/google-cloud/build-a-python-ai-agent-in-15-minutes-with-google-adk-and-mongodb-atlas-vector-search-groceries-b6c4af017629) 🟡📝💡 - Practical tutorial building a grocery shopping agent with ADK, MongoDB Vector Search, and Gemini 2.0 Flash
- 📝 [Building Next-Gen AI Agents with Google ADK, MCP, RAG and Ollama](https://medium.com/@tam.tamanna18/building-next-gen-ai-agents-with-google-adk-mcp-rag-and-ollama-ca3c1e5002da) 🟡📝💡 - Comprehensive tutorial on building multi-agent chatbots integrating ADK + MCP + RAG + Ollama with step-by-step code and architecture diagrams
- 📝 [Building a Knowledge Base from Your Codebase using Google ADK](https://medium.com/gitconnected/building-a-knowledge-base-from-your-codebase-using-google-adk-7508e845bdc1) 🟡📝🔥 - Complete guide to building multi-agent documentation systems that automatically analyze codebases and generate structured knowledge bases using ADK's planner and writer agents

### 🎥 Video Content

- 🎥 [Introducing Agent Development Kit (ADK)](https://www.youtube.com/watch?v=zgrOwow_uTQ) 🟢🎥 - 3-minute product overview shown at launch  
- 🎥 [Getting started with ADK](https://www.youtube.com/watch?v=44C8u0CDtSo) 🟢🎥 - 12-minute "hello-world" coding session from pip install to first agent
- 🎥 [Google Launches an Agent SDK – ADK Deep Dive](https://www.youtube.com/watch?v=G9wnpfW6lZY) 🟡🎥 - Independent review comparing ADK to other agent SDKs

---

## 🎯 Official Examples

_Google ADK samples repository - educational and demonstration purposes only_

> **⚠️ Important:** These are official Google examples for learning and demonstration purposes only. They are not intended for production use without significant modification. See the [ADK samples disclaimer](https://github.com/google/adk-samples).

### 🔬 Research & Analysis

- 📚 [Academic Research Agent](https://github.com/google/adk-samples/tree/main/python/agents/academic-research) 🟡📚 - Comprehensive research assistant for academic papers and citations
- 📊 [Data Science Agent](https://github.com/google/adk-samples/tree/main/python/agents/data-science) 🟡📚 - Automated data analysis and visualization workflows  
- 📈 [Time Series Forecasting Agent](https://github.com/google/adk-samples/tree/main/java/agents/time-series-forecasting) 🔴📚 - Advanced predictive analytics for time-based data
- 🏛️ [FOMC Research Agent](https://github.com/google/adk-samples/tree/main/python/agents/fomc-research) 🟡📚 - Federal Reserve meeting analysis and insights

### 💼 Business & Customer Service

- 🛡️ [Auto Insurance Agent](https://github.com/google/adk-samples/tree/main/python/agents/auto-insurance-agent) 🟡📚 - Automated insurance claim processing and customer support
- 🎯 [Brand Search Optimization](https://github.com/google/adk-samples/tree/main/python/agents/brand-search-optimization) 🟡📚 - SEO and brand visibility enhancement for products in retail websites
- 📞 [Customer Service Agent](https://github.com/google/adk-samples/tree/main/python/agents/customer-service) 🟡📚 - Multi-channel customer support automation
- 💰 [Financial Advisor](https://github.com/google/adk-samples/tree/main/python/agents/financial-advisor) 🟡📚 - Personalized financial planning and investment advice

### 🛍️ E-commerce & Marketing

- 🛒 [Personalized Shopping](https://github.com/google/adk-samples/tree/main/python/agents/personalized-shopping) 🟡📚 - AI-driven product recommendations and shopping assistance
- 📱 [Marketing Agency](https://github.com/google/adk-samples/tree/main/python/agents/marketing-agency) 🟡📚 - Comprehensive digital marketing campaign management
- ✈️ [Travel Concierge](https://github.com/google/adk-samples/tree/main/python/agents/travel-concierge) 🟡📚 - Intelligent travel planning and booking assistance

### 🔧 Development & Technical

- 🐛 [Software Bug Assistant](https://github.com/google/adk-samples/tree/main/java/agents/software-bug-assistant) 🟡📚 - Automated bug detection and resolution suggestions to help IT Support and SDE
- 🔍 [LLM Auditor](https://github.com/google/adk-samples/tree/main/python/agents/llm-auditor) 🔴📚 - Model performance evaluation and optimization
- 📚 [RAG Systems](https://github.com/google/adk-samples/tree/main/python/agents/RAG) 🔴📚 - Advanced Retrieval-Augmented Generation implementations

---

## 🚀 Getting Started / Installation

Follow these steps to set up the repository and start working with ADK agents:

### Clone the Repository

```bash
git clone https://github.com/[YOUR_USERNAME]/awesome-adk-agents.git
cd awesome-adk-agents
```

### General Workflow

1. **Navigate to an Agent Directory**: Choose either a custom agent or an example:

```bash
# For custom agents
cd my-adk-agents/job-interview-agent/
```

1. **Follow Agent-Specific Instructions**: Each agent has its own `README.md` with detailed setup and usage instructions.

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

1. **Common Commands of ADK**:

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

---

### Reporting Issues or Suggestions

- 🐛 **Bug Reports**: Found an issue with an existing agent?
- 💡 **Feature Requests**: Have ideas for new agents or improvements?
- 📚 **Documentation**: Spotted unclear or missing documentation?

### Contribution Guidelines

For detailed contribution guidelines, coding standards, and submission requirements, please see [CONTRIBUTING.md](./CONTRIBUTING.md).

**Remember**: All contributions should follow Google ADK best practices and include appropriate documentation.

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

_Happy agent building!_ 🤖✨
