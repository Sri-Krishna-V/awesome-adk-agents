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

_The most comprehensive curated collection for Google's Agent Development Kit (ADK) - featuring **80+ production-ready agents, learning resources, and deployment templates** from hackathon winners ($50K prize pool, 476 submissions), Google's official samples (35+ examples), and a growing community of 15.6K+ GitHub stars. From beginner tutorials to enterprise-grade multi-agent systems, discover battle-tested solutions for research, business automation, education, and specialized domains._

## 📖 Table of Contents

- [🎯 What This List Solves](#-what-this-list-solves)
- [What is Google's Agent Development Kit (ADK)?](#what-is-googles-agent-development-kit-adk)
- [🏆 Featured Projects](#-featured-projects)
- [🏆 ADK Hackathon Winners](#-adk-hackathon-winners)
- [🚀 Templates & Starters](#-templates--starters)
- [🌟 Community Excellence](#-community-excellence)
- [📚 Learning Resources](#-learning-resources)
- [🎯 Official Examples](#-official-examples)
- [🚀 Getting Started](#-getting-started)
- [🤝 Contributing](#-contributing)
- [🙏 Acknowledgements](#-acknowledgements)

##

> Welcome to **Awesome ADK Agents**👋👋

A comprehensive ecosystem resource for Google's Agent Development Kit - the fastest-growing agentic AI framework with 15.6K stars, 2.5K forks, and 2.8K dependent projects. Whether you're exploring AI agents for the first time or deploying production multi-agent systems, this collection provides vetted implementations, learning paths, and deployment patterns from Google's official team and a vibrant global community.

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

**Google's Agent Development Kit (ADK)** is Google's open-source, code-first Python framework for building production AI agents - backed by Google Cloud with tight Gemini integration while remaining fully model-agnostic (supports Claude, Ollama, LiteLLM). Launched in 2024, ADK has rapidly gained traction with 15.6K GitHub stars, bi-weekly releases (currently v1.19.0), and adoption by 2.8K projects, positioning itself as a serious alternative to established frameworks like LangChain and CrewAI.

**Why ADK Matters in 2025:**

- **Google's Strategic Bet**: Deep integration with Vertex AI, Cloud Run, BigQuery, and Google's AI ecosystem
- **Production-First Design**: Built for enterprise deployment from day one, not research experiments  
- **Model Flexibility**: While optimized for Gemini 2.5, supports Anthropic Claude, Ollama, and any LLM via adapters
- **Active Innovation**: 202 contributors, community hackathons with $50K prizes, and rapid feature development
- **Growing Ecosystem**: Official samples, third-party integrations (MongoDB, MCP, A2A protocol), and strong community momentum

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
- 🔥 [Deep Search ADK Quickstart](https://github.com/google/adk-samples/tree/main/python/agents/deep-search) 🏭🔴⭐ - **The gold standard**: Complete fullstack research agent (formerly Gemini Fullstack) with React frontend, human-in-the-loop workflows, autonomous research pipelines, and Cloud Run deployment
- 🧪 [Yash-Kavaiya/google-adk-test-automation](https://github.com/Yash-Kavaiya/google-adk-test-automation) 🏭🟡 - Comprehensive ADK testing framework with automated conversation flows, session management, and detailed CSV reporting
- 📱 [kkdai/linebot-adk](https://github.com/kkdai/linebot-adk) 🏭🟢 - LINE Bot template with Docker, Cloud Run deployment, and security configurations  
- 🌐 [phamvuhoang/google-adk-nextjs-starter](https://github.com/phamvuhoang/google-adk-nextjs-starter) 🟢 - Next.js starter template for Google ADK projects with Angular frontend
- 🎨 [abhishekkumar35/google-adk-nocode](https://github.com/abhishekkumar35/google-adk-nocode) 🟢 - Visual, no-code interface for creating AI agents (supports cloud and local Ollama models)

---

## 🌟 Community Excellence

_Outstanding community projects showcasing ADK capabilities_

### Multi-Agent Systems

- 🤖 [derailed-dash/rickbot-adk](https://github.com/derailed-dash/rickbot-adk) 🏭🟡 - Multi-personality chatbot with FastAPI backend, Next.js UI, OAuth, and multi-agent RAG/search architecture
- 🔥 [Parth0248/Forkcast](https://github.com/Parth0248/Forkcast) 🏭🟡 - Multi-agent AI system for collaborative dining decisions with deployed webapp, technical reports, and Cloud Run deployment
- 🚀 [kweinmeister/agentic-trading](https://github.com/kweinmeister/agentic-trading) 🏭🔴 - Multi-agent trading system with risk management, featuring AlphaBot and RiskGuard agents with complete A2A protocol implementation and production deployment
- 📊 [vladkol/CRM Data Q&A Agent](https://github.com/vladkol/crm-data-agent) 🏭🔴 - Multi-agentic system with Advanced RAG and NL2SQL over Salesforce Data, "Run on Google Cloud" deployment
- 🏙️ [M-JULIANI/nyc-monitor](https://github.com/M-JULIANI/nyc-monitor) 🟡🏭🔥 - AI-powered urban intelligence system for real-time NYC event analysis and reporting with multi-agent architecture and automated Google Slides reports
- 🏛️ [intent-solutions-io/iam-bobs-brain](https://github.com/intent-solutions-io/iam-bobs-brain) 🏭🔴 - General-purpose enterprise orchestrator on Google ADK + Vertex AI Agent Engine with risk tiers (R0-R4), policy gates, evidence bundles, and Mission Spec v1 workflows
- 🌐 [seehiong/adk-web-multi-agent](https://github.com/seehiong/adk-web-multi-agent) 🟡 - Multi-agent system with Google ADK and OpenRouter models coordinating specialist agents to query PostgreSQL (via MCP Toolbox) and Data Commons

### Integration & Advanced Patterns

- 🔌 [RubensZimbres/A2A_ADK_MCP](https://github.com/RubensZimbres/A2A_ADK_MCP) 🔴 - Multi-Agent Systems using Google's ADK + A2A + MCP
- 🎤 [bhancockio/Voice-Enabled-Agent](https://github.com/bhancockio/adk-voice-agent) 🟡 - Speech-to-text and voice interaction capabilities with G-Calendar integration and comprehensive setup documentation
- 🔗 [serkanyasr/mcp-agent-tool-adapter](https://github.com/serkanyasr/mcp-agent-tool-adapter) 🟡 - Converts MCP tools into Google ADK or LangGraph agents with streaming FastAPI/CLI
- 🔧 [codeninja/Mongoose Migration Agent System](https://gist.github.com/codeninja/a6e117a3480de8d32dd9ef01b519cdae) 🔴🔥 - Multi-agent system for automated Mongoose database migration (v6→v8) with specialized agents and MCP integration
- 🖥️ [trendmicro/adk-agui-middleware](https://github.com/trendmicro/adk-agui-middleware) 🏭🟡 - Python middleware bridging Google ADK agents with the AG-UI protocol via Server-Sent Events for real-time agent interactions in frontend applications
- 🛡️ [imran-siddique/agent-os](https://github.com/imran-siddique/agent-os) 🏭🔴🔥 - Kernel-level governance for AI agents with policy enforcement, action interception, and OWASP Agentic Top 10 coverage — works with Google ADK, LangChain, CrewAI, AutoGen, and more
- 🔐 [Idun-Group/idun-agent-platform](https://github.com/Idun-Group/idun-agent-platform) 🏭🔴🔥 - Open-source Agent Governance Platform that turns any LangGraph or ADK agent into a production-ready service with AG-UI, OpenTelemetry, MCP, memory, guardrails, SSO, and RBAC

### Agent Development & Engineering Platforms

- 🛠️ [VidyutChakrabarti/AgentFlux](https://github.com/VidyutChakrabarti/AgentFlux) 🏭🔴🔥 - Agent engineering platform with interactive playgrounds, graph visualization, automated refinement loops, and fine-tuned models for prompt optimization
- 🏗️ [antiv/mate](https://github.com/antiv/mate) 🏭🔴🔥 - Production-ready multi-agent orchestration engine built on Google ADK with database-driven agent config, 50+ LLM providers, MCP protocol, persistent memory, web dashboard, and RBAC
- 🗄️ [edu010101/adk-extra-services](https://github.com/edu010101/adk-extra-services) 🏭🟡 - Python package providing additional service backends for Google ADK (S3, Redis, MongoDB, Azure, Supabase) to replace default in-memory storage
- 🧠 [serkanh/adk-with-memorybank](https://github.com/serkanh/adk-with-memorybank) 🏭🟡 - ADK agents integrated with Vertex AI Memory Bank for persistent cross-session memory and context management

### Domain-Specific Applications

- 💰 [mtwn105/zerodha-mcp](https://github.com/mtwn105/zerodha-mcp) 🟡 - Zerodha MCP Server & Client integrating Google ADK for financial applications
- 📈 [sudsk/tradesage-mvp](https://github.com/sudsk/tradesage-mvp) 🏭🟡 - Multi-agent trading hypothesis analysis system with 6 specialized agents and Cloud Run deployment
- 💹 [RubensZimbres/Financial_ADK_Agent_Graph_Database](https://github.com/RubensZimbres/Financial_ADK_Agent_Graph_Database) 🏭🔴 - Multi-agent financial analytics with Neo4j graph database, SEC filings RAG, and ML stock predictions
- ✈️ [AashiDutt/Google-Agent-Development-Kit-Demo](https://github.com/AashiDutt/Google-Agent-Development-Kit-Demo) 🟢 - ADK-powered travel planner
- 📊 [jenyss/google-adk-data-visualization-agent](https://github.com/jenyss/google-adk-data-visualization-agent) 🟡 - Data visualization agent built with Google ADK
- 🏥 [Ahsan462aggk/Medical_Search_Pro_Agent](https://github.com/Ahsan462aggk/Medical_Search_Pro_Agent) 🟡🏭 - Multi-agent biomedical research system with PubMed search, analysis, and email delivery
- 🧠 [IhateCreatingUserNames2/Cognisphere](https://github.com/IhateCreatingUserNames2/Cognisphere) 🔴 - AI agent development framework built on Google's ADK
- 🎨 [bhancockio/YouTube-Thumbnail-Agent](https://github.com/bhancockio/adk-youtube-thumbnail-agent) 🟢 - Automated thumbnail generation and optimization
- 🏭 [ntg2208/production-ai-customer-support](https://github.com/ntg2208/production-ai-customer-support) 🔴🏭 - Enterprise-grade multi-agent system with Policy Agent, Ticket Agent, and Master orchestrator featuring location intelligence, RAG knowledge base, and comprehensive tutorials
- 📊 [AI Trends Analysis Pipeline](https://github.com/Astrodevil/ADK-Agent-Examples/tree/main/analyzer_agent) 🟡🔥 - Comprehensive AI analysis pipeline using Exa Search, Tavily Search, Firecrawl and Nebius AI
- 📁 [Job Finder Agent](https://github.com/Astrodevil/ADK-Agent-Examples/tree/main/jobfinder_agent) 🟡 - Sequential Agent using Mistral OCR, Linkup API and Nebius AI
- 📧 [Email ADK Agent](https://github.com/Astrodevil/ADK-Agent-Examples/tree/main/email_adk_agent) 🟢 - Email management and automation agent using Resend API
- 📦 [arjunprabhulal/MCP-Gemma-3-Agent](https://github.com/arjunprabhulal/adk-mcp-gemma3) 🟡 - Gemma 3 leveraged by Ollama, MCP Youtube Search
- 🔧 [serkanh/sre-bot](https://github.com/serkanh/sre-bot) 🏭🟡 - SRE/DevOps bot built on Google ADK for intelligent infrastructure management and incident response
- 🔍 [sreekar2858/JobSearch-Agent](https://github.com/sreekar2858/JobSearch-Agent) 🟡 - Automated job search agent using ADK that scrapes listings from LinkedIn, Indeed, and Glassdoor, filters by preferences, and manages applications
- 👔 [akajammythakkar/adk_hiring_agent](https://github.com/akajammythakkar/adk_hiring_agent) 🟡 - AI-powered hiring agent using Google ADK and Gemini to analyze resumes, assess skills, and match candidates via multi-agent collaboration
- 🔬 [emansarahafi/Research-Assistant-Agent](https://github.com/emansarahafi/Research-Assistant-Agent) 🟡 - Multi-agent research assistant with Researcher, Analyst, and Formatter sub-agents using ArXiv search, deployable locally (Flask) or on Vertex AI
- 📚 [Anubhob435/Ai-Agents-EditorHouse](https://github.com/Anubhob435/Ai-Agents-EditorHouse) 🟡 - Multi-agent book creation system using Google ADK that plans, writes, edits, illustrates, and compiles complete books from a single topic prompt with MongoDB metadata tracking
- 💬 [B4K2/WhatsApp-agent](https://github.com/B4K2/WhatsApp-agent) 🟡 - Intelligent WhatsApp agent built with MCP + Google ADK for conversational automation

---

## 📚 Learning Resources

_Comprehensive guides, tutorials, and educational content_

### ⭐ Featured Training Platform

- 🏆 **[Google ADK Training Hub](https://raphaelmansuy.github.io/adk_training/)** 🟢🟡🔴📚🔥 - **The most comprehensive ADK training platform**: 35+ hands-on tutorials, production deployment patterns, multi-agent architectures, Cloud Run/Vertex AI deployment, React/Next.js integration, and enterprise-grade best practices. Progressive learning paths from beginner to advanced with copy-paste ready code and working implementations.

### 🚀 Quickstart Courses

- 📚 [ADK Crash Course by Brandon Hancock](https://github.com/bhancockio/agent-development-kit-crash-course) 🟢📚 - Fundamentals of ADK, from basics to advanced workflows and multi-agent systems with [Youtube](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=2659s) tutorial
- 📚 [A2A Crash Course by Brandon Hancock](https://github.com/bhancockio/agent2agent) 🟡📚 - Comprehensive guide to building agent-to-agent (A2A) communication using ADK with [Youtube](https://www.youtube.com/watch?v=mFkw3p5qSuA&t=172s) tutorial  
- 📚 [chongdashu/adk-made-simple](https://github.com/chongdashu/adk-made-simple) 🟢📚 - From basics to A2A integration with real world applications and projects
- 📚 [theailifestyle/google-adk-demos](https://github.com/theailifestyle/google-adk-demos) 🟢📚 - Collection of practical demos showcasing various ADK features
- 📚 [arjunprabhulal/google-adk-masterclass](https://github.com/arjunprabhulal/google-adk-masterclass) 🟡📚 - 20-module masterclass covering ADK basics through advanced topics including MCP, Vertex AI, and production deployment
- 📚 [omerbsezer/Fast-LLM-Agent-MCP](https://github.com/omerbsezer/Fast-LLM-Agent-MCP) 🟡📚 - Comprehensive resource covering LLMs, RAG, fine-tuning, agents, MCP, and Google ADK both theoretically and practically with reference documents
- 📚 [proflead/how-to-build-ai-agent](https://github.com/proflead/how-to-build-ai-agent) 🟢📚 - Beginner-friendly tutorial for building AI agents with Google ADK, covering install, tools, and first agent creation

### 🧪 Official Hands-on Learning

- 🧪 [Google ADK Codelabs](https://codelabs.developers.google.com/?text=ADK) ⭐📚 - Interactive, guided tutorials with hands-on coding exercises from Google
- 🧪 [Build Your First ADK Agent Workforce](https://cloud.google.com/blog/topics/developers-practitioners/build-your-first-adk-agent-workforce) ⭐🟢📚 - Complete learning path with 3 official codelabs: building autonomous agents, empowering agents with tools, and orchestrating multi-agent systems
- 🧪 [Building GraphRAG Agents with ADK and Neo4j](https://codelabs.developers.google.com/neo4j-adk-graphrag-agents) ⭐🟡📚💡 - Official 65-minute codelab building multi-agent investment research system with Neo4j graph database, MCP Toolbox integration, and GraphRAG patterns for complex relationship traversal and multi-hop reasoning
- 🎓 [5-Day Agents Course on Kaggle](https://www.kaggle.com/learn-guide/5-day-agents) ⭐📚 - Comprehensive 5-day online course crafted by Google's ML researchers and engineers exploring foundations and practical applications of AI agents, covering core components (models, tools, orchestration, memory, and evaluation) and production-ready systems
- 📖 [Introduction to Agents Whitepaper](https://www.kaggle.com/whitepaper-introduction-to-agents) ⭐📚 - Comprehensive whitepaper by Google's AI researchers explaining the paradigm shift from passive AI models to autonomous problem-solving agents, covering agent architecture, capabilities, and real-world applications

### 📖 Tutorials & Walkthroughs

- 📖 [chongdashu/adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course) 🟡📖🔥 - Complete multi-agent system with ADK + A2A + MCP integration, featuring Notion and ElevenLabs with full architecture, testing, and [YouTube](https://www.youtube.com/watch?v=s6-Ofu-uu2k) tutorial
- 📖 [mongodb-developer/MongoDB-ADK-Agents](https://github.com/mongodb-developer/MongoDB-ADK-Agents) 🟡📖💡 - Official MongoDB grocery shopping agent implementation with Vector Search, complete dataset, and step-by-step setup - companion repository  for the MongoDB Atlas tutorial
- 📖 [datascalehq/datascale](https://github.com/datascalehq/datascale/tree/main/cookbook/tutorials/agent_docs) 🟡📖🔥 - Multi-agent documentation builder with planner and writer agents that automatically analyze codebases and generate structured knowledge bases - companion repository for the codebase documentation article
- 📖 [meteatamel/adk-demos](https://github.com/meteatamel/adk-demos/) 🟢📖 - Collection of demos and tutorials for Google's Agent Development Kit
- 📖 [sokart/adk-walkthrough](https://github.com/sokart/adk-walkthrough) 🟡📖 - Step-by-step guides and examples using the open-source Python ADK framework
- 📖 [bhancockio/RAG-Agent-Tutorial](https://github.com/bhancockio/adk-rag-agent) 🟡📖 - Complete RAG implementation with ADK and Vertex AI with [YouTube](https://www.youtube.com/watch?v=TvW4A0a75mw&t=14s) tutorial
- 📖 [bhancockio/MCP Integration Tutorial](https://github.com/bhancockio/adk-mcp-tutorial) 🟡📖 - Model Context Protocol (both local and remote) with ADK with [Youtube](https://www.youtube.com/watch?v=HkzOrj2qeXI&t=2362s) tutorial
- 📖 [thomas-chong/google-adk-visual-agent-builder-demo](https://github.com/thomas-chong/google-adk-visual-agent-builder-demo) 🟡📖 - Complete demo of Google ADK Visual Agent Builder with a multi-agent research system walkthrough
- 📖 [lavinigam-gcp/build-with-adk](https://github.com/lavinigam-gcp/build-with-adk) 🏭🟡📖 - Design patterns and production-ready architectures for building multi-agent AI systems with Google ADK on Cloud Run, Vertex AI, and AI Studio

#### 🎓 Google ADK Tutorial Examples

_Comprehensive tutorial examples from [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) demonstrating ADK patterns and capabilities_

**Structured Output Agents:**

- 📖 [Customer Support Ticket Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/3_structured_output_agent/3_1_customer_support_ticket_agent) 🟢📖 - Generates structured support tickets with Pydantic schemas
- 📖 [Email Generator Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/3_structured_output_agent/3_2_email_agent) 🟢📖 - Creates formatted emails with structured output

**Tool-Using Agents:**

- 📖 [Code Execution Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/4_tool_using_agent/4_1_builtin_tools/code_exec_agent) 🟢📖 - Built-in code execution tools
- 📖 [Google Search Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/4_tool_using_agent/4_1_builtin_tools/search_agent) 🟢📖 - Web search capabilities
- 📖 [Filesystem Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/4_tool_using_agent/4_4_mcp_tools/filesystem_agent) 🟢📖 - MCP filesystem tools integration
- 📖 [LangChain Integration Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/4_tool_using_agent/4_3_thirdparty_tools/langchain_agent) 🟢📖 - Third-party tool integration with LangChain
- 📖 [CrewAI Integration Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/4_tool_using_agent/4_3_thirdparty_tools/crewai_agent) 🟢📖 - Third-party tool integration with CrewAI

**Callback Agents:**

- 📖 [Agent Lifecycle Callbacks](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/6_callbacks/6_1_agent_lifecycle_callbacks) 🟢📖 - Monitoring agent execution lifecycle
- 📖 [LLM Interaction Callbacks](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/6_callbacks/6_2_llm_interaction_callbacks) 🟢📖 - Tracking LLM calls and responses
- 📖 [Tool Execution Callbacks](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/6_callbacks/6_3_tool_execution_callbacks) 🟢📖 - Monitoring tool usage and execution

**Plugin Agents:**

- 📖 [Plugin-based Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/7_plugins) 🟢📖 - Extensible plugin architecture for modular agent design

**Multi-Agent Systems:**

- 📖 [Sequential Multi-Agent Pattern](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/9_multi_agent_patterns/9_1_sequential_agent) 🟢📖 - Step-by-step multi-agent coordination
- 📖 [Loop Multi-Agent Pattern](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/9_multi_agent_patterns/9_2_loop_agent) 🟢📖 - Iterative multi-agent workflows
- 📖 [Parallel Multi-Agent Pattern](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/9_multi_agent_patterns/9_3_parallel_agent) 🟢📖 - Concurrent multi-agent execution

**Multi-Agent Applications:**

- 📖 [AI Financial Coach Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/ai_financial_coach_agent) 🟡📖 - Financial advisory system with specialized agent teams
- 📖 [AI Home Renovation Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/ai_home_renovation_agent) 🟡📖 - Home improvement planning with multi-agent coordination
- 📖 [AI SEO Audit Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_seo_audit_team) 🟡📖 - Website SEO analysis with specialized agent teams
- 📖 [Multimodal UI/UX Feedback Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_uiux_feedback_agent_team) 🟡📖 - Design review system with multimodal capabilities

### 📝 Articles & Best Practices

- 📝 [Introducing the File Search Tool in Gemini API](https://blog.google/technology/developers/file-search-gemini-api/) ⭐🟢📝💡 - Official launch of fully managed RAG system in Gemini API with free storage/embeddings, automatic chunking, vector search, and built-in citations - essential for building knowledge-grounded agents
- 📝 [More Ways to Build, Scale, and Govern AI Agents with Vertex AI Agent Builder](https://cloud.google.com/blog/products/ai-machine-learning/more-ways-to-build-and-scale-ai-agents-with-vertex-ai-agent-builder) ⭐🟡📝🏭 - Official Google Cloud announcement of ADK updates including observability, evaluation, agent identities, and production scaling features with real customer case studies
- 📝 [ADK Architecture: When to Use Sub-Agents versus Agents as Tools](https://cloud.google.com/blog/topics/developers-practitioners/where-to-use-sub-agents-versus-agents-as-tools) ⭐🟡📝 - Essential architectural guide with decision matrix for choosing between sub-agents and agent tools, featuring real-world use cases (data agents, travel planners) and best practices for multi-agent systems
- 📝 [From Zero to Multi-Agents: A Beginner's Guide to Google ADK](https://medium.com/@sokratis.kartakis/from-zero-to-multi-agents-a-beginners-guide-to-google-agent-development-kit-adk-b56e9b5f7861) 🟢📝 - Step-by-step beginner guide by Dr Sokratis Kartakis
- 📝 [Ralph Loop with Google ADK: AI Agents That Verify, Not Guess](https://medium.com/google-cloud/ralph-loop-with-google-adk-ai-agents-that-verify-not-guess-b41f71c0f30f) 🔴📝🔥 - Advanced guide to implementing Ralph Loop pattern for external verification-driven workflows, featuring multi-agent Dockerfile generation with Docker-based validation and iterative refinement until objective success criteria are met. Check the repo [here.](https://github.com/thomas-chong/google-adk-ralph-loop-demo)
- 📝 [Choosing the Right Deployment Path for Your Google ADK Agents](https://medium.com/google-cloud/choosing-the-right-deployment-path-for-your-google-adk-agents-86c89c251ab5) 🟡📝🏭 - Official Google Cloud guide comparing deployment strategies (Cloud Run vs Vertex AI vs GKE) for production ADK agents
- 📝 [Announcing a Datastore-Backed Session Service for the ADK](https://medium.com/google-cloud/announcing-a-new-datastore-backed-session-service-for-the-adk-d14596ae28df) 🟡📝🏭 - Google Cloud solution for persistent agent sessions in serverless environments using Cloud Datastore instead of SQLite
- 📝 [Drawing Charts in Your AI Agent Frontend with Google ADK](https://medium.com/@dconsonni/drawing-charts-in-your-ai-agent-frontend-with-google-adk-9c74a4a98931) 🟡📝🏭 - Production-ready guide to agent-generated visualizations using ADK Artifacts with Apache ECharts/vis-network, featuring FastAPI integration, session-scoped artifact management, and complete working examples for rendering charts from agent outputs
- 📝 [Build a Python AI Agent in 15 Minutes with Google ADK and MongoDB Atlas Vector Search](https://medium.com/google-cloud/build-a-python-ai-agent-in-15-minutes-with-google-adk-and-mongodb-atlas-vector-search-groceries-b6c4af017629) 🟡📝💡 - Practical tutorial building a grocery shopping agent with ADK, MongoDB Vector Search, and Gemini 2.0 Flash
- 📝 [Building Next-Gen AI Agents with Google ADK, MCP, RAG and Ollama](https://medium.com/@tam.tamanna18/building-next-gen-ai-agents-with-google-adk-mcp-rag-and-ollama-ca3c1e5002da) 🟡📝💡 - Comprehensive tutorial on building multi-agent chatbots integrating ADK + MCP + RAG + Ollama with step-by-step code and architecture diagrams
- 📝 [Google ADK + LM Studio: The Power Couple of Local Agent Development](https://medium.com/@c-damien/google-adk-lm-studio-the-power-couple-of-local-agent-development-2dd225bae36f) 🟡📝💡 - Complete guide to running ADK agents locally with LM Studio, featuring setup instructions, model configuration, and privacy-focused development without cloud dependencies
- 📝 [Building a Knowledge Base from Your Codebase using Google ADK](https://medium.com/gitconnected/building-a-knowledge-base-from-your-codebase-using-google-adk-7508e845bdc1) 🟡📝🔥 - Complete guide to building multi-agent documentation systems that automatically analyze codebases and generate structured knowledge bases using ADK's planner and writer agents
- 📝 [Optimize Your Google ADK Agent's SOP with GEPA](https://raphaelmansuy.github.io/adk_training/blog/gepa-optimization-tutorial/) 🔴📝🔥 - Advanced guide to systematic prompt optimization using GEPA (Genetic Evolutionary Prompt Augmentation) with LLM-based reflection, automated SOP evolution, and production-ready implementation achieving 0% to 100% success rates

### 🎥 Video Content

- 🎥 [Introducing Agent Development Kit (ADK)](https://www.youtube.com/watch?v=zgrOwow_uTQ) 🟢🎥 - 3-minute product overview shown at launch  
- 🎥 [Getting started with ADK](https://www.youtube.com/watch?v=44C8u0CDtSo) 🟢🎥 - 12-minute "hello-world" coding session from pip install to first agent
- 🎥 [Google Launches an Agent SDK – ADK Deep Dive](https://www.youtube.com/watch?v=G9wnpfW6lZY) 🟡🎥 - Independent review comparing ADK to other agent SDKs
- 🎥 [Agent Factory: AI Agents for Data Engineering and Data Science](https://cloud.google.com/blog/topics/developers-practitioners/agent-factory-recap-ai-agents-for-data-engineering-and-data-science) 🟡🎥 - Episode recap featuring BigQuery Data Engineering Agent, Data Science Agent in Colab Enterprise, and creative ADK application with Spanner graph database
- 🎥 [ADK Tutorial Playlist](https://www.youtube.com/playlist?list=PL6tW9BrhiPTAZts0W5nQS9dbW6VMnLKab) 🟢🎥 - Comprehensive video tutorial series covering ADK fundamentals and advanced topics

---

## 🎯 Official Examples

_Google ADK samples repository - educational and demonstration purposes only_

> **⚠️ Important:** These are official Google examples for learning and demonstration purposes only. They are not intended for production use without significant modification. See the [ADK samples disclaimer](https://github.com/google/adk-samples).

### 🔬 Research & Analysis

- 📚 [Academic Research Agent](https://github.com/google/adk-samples/tree/main/python/agents/academic-research) 🟡📚 - Assists researchers in identifying recent publications and discovering emerging research areas
- 📊 [Data Science Agent](https://github.com/google/adk-samples/tree/main/python/agents/data-science) 🟡📚 - Multi-agent system for sophisticated data analysis with NL2SQL and structured data processing
- 🏛️ [FOMC Research Agent](https://github.com/google/adk-samples/tree/main/python/agents/fomc-research) 🔴📚 - Federal Reserve meeting analysis and market event insights
- 🔍 [LLM Auditor](https://github.com/google/adk-samples/tree/main/python/agents/llm-auditor) 🟢📚 - Chatbot response verification and content auditing with Google Search integration
- 📺 [YouTube Analyst](https://github.com/google/adk-samples/tree/main/python/agents/youtube-analyst) 🟡📚 - YouTube channel performance and audience engagement analysis using YouTube Data API with interactive Plotly visualizations via a dedicated visualization sub-agent

### 💼 Business & Customer Service

- 🛡️ [Auto Insurance Agent](https://github.com/google/adk-samples/tree/main/python/agents/auto-insurance-agent) 🟡📚 - Auto insurance management for members, claims, rewards and roadside assistance with Apigee integration
- 🎯 [Brand Search Optimization](https://github.com/google/adk-samples/tree/main/python/agents/brand-search-optimization) 🟡📚 - E-commerce product data enrichment analyzing top search results with BigQuery integration
- 🎨 [Brand Aligner Agent](https://github.com/google/adk-samples/tree/main/python/agents/brand-aligner) 🔴📚 - End-to-end visual asset (images/videos) evaluation against brand guidelines using Gecko on Vertex AI Eval Service, with sequential multi-agent orchestration and GCS artifact storage
- 🏠 [Customer Service Agent](https://github.com/google/adk-samples/tree/main/python/agents/customer-service) 🟢📚 - Home & garden customer service with product selection, order management, and live streaming support
- 💰 [Financial Advisor](https://github.com/google/adk-samples/tree/main/python/agents/financial-advisor) 🟡📚 - Educational content assistant for financial advisors covering finance and investment topics
- 🚨 [Incident Management](https://github.com/google/adk-samples/tree/main/python/agents/incident-management) 🟢📚 - ServiceNow integration with Application Integration Connectors and dynamic identity propagation
- 📦 [Order Processing](https://github.com/google/adk-samples/tree/main/python/agents/order-processing) 🟢📚 - Automated order workflows with human-in-the-loop using Application Integration Connectors

### 🛍️ E-commerce & Marketing

- 🛒 [Personalized Shopping](https://github.com/google/adk-samples/tree/main/python/agents/personalized-shopping) 🟡📚 - AI-driven product recommendations and shopping assistance
- 📱 [Marketing Agency](https://github.com/google/adk-samples/tree/main/python/agents/marketing-agency) 🟡📚 - Website and product launch automation with domain optimization, content generation, and brand asset design
- ✈️ [Travel Concierge](https://github.com/google/adk-samples/tree/main/python/agents/travel-concierge) 🟡📚 - Multi-agent travel planning and digital task assistance with dynamic instructions
- 📈 [Google Trends Agent](https://github.com/google/adk-samples/tree/main/python/agents/google-trends-agent) 🟡📚 - BigQuery-powered trending search terms analysis by region and time period
- 📺 [Product Catalog Ad Generation](https://github.com/google/adk-samples/tree/main/python/agents/product-catalog-ad-generation) 🟡📚 - Automated advertising content generation from product catalogs

### 🔧 Development & Technical

- 🐛 [Software Bug Assistant](https://github.com/google/adk-samples/tree/main/python/agents/software-bug-assistant) 🟡📚 - Bug resolution assistant with RAG, MCP, and external knowledge sources (GitHub, StackOverflow)
- 🤖 [Machine Learning Engineering](https://github.com/google/adk-samples/tree/main/python/agents/machine-learning-engineering) 🔴📚 - Autonomous ML model building and training for state-of-the-art performance on diverse ML tasks
- 🧩 [RAG Systems](https://github.com/google/adk-samples/tree/main/python/agents/RAG) 🟡📚 - Vertex AI RAG Engine powered document Q&A with citations
- 📊 [Data Engineering Agent](https://github.com/google/adk-samples/tree/main/python/agents/data-engineering) 🔴📚 - BigQuery and Dataform pipeline builder for ELT workflows and analytics engineering
- 🔧 [Plumber Data Engineering Assistant](https://github.com/google/adk-samples/tree/main/python/agents/plumber-data-engineering-assistant) 🔴📚 - Big data pipeline creator for Apache Spark, Apache Beam, and dBT on GCP
- 🧪 [SWE Benchmark Agent](https://github.com/google/adk-samples/tree/main/python/agents/swe-benchmark-agent) 🔴📚 - Software engineering benchmark testing and evaluation agent
- 🧪 [Tau2 Benchmark Agent](https://github.com/google/adk-samples/tree/main/python/agents/tau2-benchmark-agent) 🔴📚 - Tau2 benchmark agent for advanced evaluation tasks

### 🎨 Specialized Applications

- 🎨 [Image Scoring Agent](https://github.com/google/adk-samples/tree/main/python/agents/image-scoring) 🟢📚 - Image generation and policy compliance scoring with Imagen integration
- 🐪 [CAMEL Integration](https://github.com/google/adk-samples/tree/main/python/agents/camel) 🔴📚 - Multi-agent communication framework integration with CAMEL
- 🔥 [Deep Search](https://github.com/google/adk-samples/tree/main/python/agents/deep-search) 🔴📚⭐ - **Complete fullstack research agent** (formerly Gemini Fullstack) with React frontend, FastAPI backend, and Human-in-the-Loop workflows
- 🏥 [Medical Pre-Authorization](https://github.com/google/adk-samples/tree/main/python/agents/medical-pre-authorization) 🟡📚 - Healthcare pre-authorization automation analyzing medical records and policies for coverage determination
- 🎬 [Short Movie Agents](https://github.com/google/adk-samples/tree/main/python/agents/short-movie-agents) 🟡📚 - End-to-end video construction based on user intent with multi-agent coordination
- 🎙️ [Podcast Transcript Agent](https://github.com/google/adk-samples/tree/main/python/agents/podcast_transcript_agent) 🟡📚 - Podcast transcription and analysis agent
- ✍️ [Blog Writer](https://github.com/google/adk-samples/tree/main/python/agents/blog-writer) 🟡📚 - Automated blog content generation and writing assistant
- 📖 [Story Teller](https://github.com/google/adk-samples/tree/main/python/agents/story_teller) 🟡📚 - Multi-agent collaborative story writer with a PromptEnhancer, Parallel Writers (creative + focused temperature), Critique Agent, and final Editor — showcases Sequential, Parallel, and Loop agent composition
- 🛡️ [Safety Guardrail Plugins](https://github.com/google/adk-samples/tree/main/python/agents/safety-plugins) 🟡📚 - Security filters using Gemini-as-judge and Model Armor for jailbreak protection
- 💳 [Antom Payment](https://github.com/google/adk-samples/tree/main/python/agents/antom-payment) 🟡📚 - Ant International payment and refund integration via MCP tools
- 💬 [Realtime Conversational Agent](https://github.com/google/adk-samples/tree/main/python/agents/realtime-conversational-agent) 🟡📚 - Live streaming conversational agent with real-time interaction capabilities
- ⚡ [ADK Bidi-streaming Demo](https://github.com/google/adk-samples/tree/main/python/agents/bidi-demo) 🟡📚 - Real-time bidirectional streaming demo with WebSocket communication, multimodal support (audio/video/text), and concurrent task handling
- 🛡️ [AI Security Agent](https://github.com/google/adk-samples/tree/main/python/agents/ai-security-agent) 🔴📚 - LLM red team agent for comprehensive security testing and vulnerability assessment
- 💰 [Currency Agent](https://github.com/google/adk-samples/tree/main/python/agents/currency-agent) 🟡📚 - Currency exchange rate lookups and conversions with A2A and MCP integration
- 🏗️ [Hierarchical Workflow Automation](https://github.com/google/adk-samples/tree/main/python/agents/hierarchical-workflow-automation) 🔴📚 - Structured multi-system transaction orchestration with multi-agent architecture
- 🔀 [Parallel Task Decomposition Execution](https://github.com/google/adk-samples/tree/main/python/agents/parallel_task_decomposition_execution) 🔴📚 - Design pattern for parallel task decomposition and execution with ADK agents
- 🔐 [Policy-as-Code Agent](https://github.com/google/adk-samples/tree/main/python/agents/policy-as-code) 🟡📚 - Data governance agent implementing policy-as-code patterns for compliance
- 🏪 [Retail AI Location Strategy](https://github.com/google/adk-samples/tree/main/python/agents/retail-ai-location-strategy) 🟡📚 - Retail location optimization and market analysis with multi-agent system

### 🌐 Other Language Samples

_Official ADK samples in TypeScript, Java, and Go_

**TypeScript**

- 🏠 [Customer Service Agent (TypeScript)](https://github.com/google/adk-samples/tree/main/typescript/agents/customer_service) 🟢📚 - TypeScript port of the customer service agent for home & garden retail with product selection and order management

**Java**

- 🐛 [Software Bug Assistant (Java)](https://github.com/google/adk-samples/tree/main/java/agents/software-bug-assistant) 🟡📚 - Java port of the bug resolution assistant using ADK Java with RAG and external knowledge integration
- 📈 [Time Series Forecasting (Java)](https://github.com/google/adk-samples/tree/main/java/agents/time-series-forecasting) 🔴📚 - ADK Java agent using MCP Toolbox + BigQuery `AI.FORECAST` for natural language time series forecasting over public datasets, deployable to Cloud Run

**Go**

- 🔍 [LLM Auditor (Go)](https://github.com/google/adk-samples/tree/main/go/agents/llm-auditor) 🟢📚 - Go port of the LLM response auditor for chatbot verification and content auditing
- ⛵ [Boat Agent (Go)](https://github.com/google/adk-samples/tree/main/go/agents/boat-agent) 🟢📚 - Go ADK sample agent for sailing/boating assistance
- 📋 [Naval List (Go)](https://github.com/google/adk-samples/tree/main/go/agents/navallist) 🟢📚 - Go ADK sample demonstrating list management with a naval theme
- 🔭 [Sail Researcher (Go)](https://github.com/google/adk-samples/tree/main/go/agents/sail-researcher) 🟡📚 - Go ADK research agent for sailing-domain information retrieval

---

## 🚀 Getting Started

### Quick Start with Google ADK

```bash
# Install ADK framework
pip install google-adk

# Create your first agent
adk create my-agent
cd my-agent

# Run with web interface
adk web
```

### Using This Repository

This is a **hybrid awesome list** - combining curated resources with featured implementations:

- **Browse & Learn**: Explore categorized projects for inspiration and best practices
- **Clone & Build**: Featured projects in `/my-adk-agents/` are production-ready starting points
- **Contribute**: Add your own projects or improve existing ones via [CONTRIBUTING.md](./CONTRIBUTING.md)

### Essential ADK Commands

```bash
adk web         # Launch web UI (recommended)
adk run         # Interactive CLI
adk create      # Generate new agent template
adk deploy      # Deploy to cloud platforms
```

### Resources

- 📖 [Official ADK Documentation](https://google.github.io/adk-docs/)
- � [Third-Party Tools for ADK](https://google.github.io/adk-docs/tools/third-party/) - Official catalog of integrated third-party tools including Browserbase, Exa, Firecrawl, GitHub, Hugging Face, Notion, Tavily, and more
- �💬 [Community Discussions](https://github.com/google/adk-python/discussions)
- 🎓 [Learning Path](#-learning-resources)

---

## 🤝 Contributing

We welcome high-quality contributions that advance the ADK ecosystem. See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

**Quality Standards**: Production-ready code, comprehensive documentation, and adherence to ADK best practices.

## 📞 Support

- 🐛 **Issues**: Report bugs or request features via GitHub Issues
- 💡 **Discussions**: Join the community for questions and ideas
- 📧 **Maintainer**: Contact repository owner for collaboration opportunities

---

## 🙏 Acknowledgements

**Core Contributors:**

- Google ADK Team - Framework development
- Brandon Hancock - Educational content and tutorials  
- Community Contributors - Featured projects and improvements

## ⭐ Impact

This repository serves **2,500+ developers** building production AI agents. Help us grow:

- ⭐ **Star** if this helps your development
- 🔗 **Share** with your network
- 🤝 **Contribute** your expertise

- [![MseeP.ai Security Assessment Badge](https://mseep.net/pr/sri-krishna-v-awesome-adk-agents-badge.png)](https://mseep.ai/app/sri-krishna-v-awesome-adk-agents)

---

<div align="center">
<strong>Building the future of AI agents, one contribution at a time.</strong><br>
<em>Powered by Google ADK • Curated by the community</em>
</div>
