<div align="center">
  <h1>
    Awesome ADK Agents
    <a href="https://awesome.re">
      <img src="https://awesome.re/badge.svg" alt="Awesome">
    </a>
  </h1>
</div>

<p align="center"><img src="https://adk.dev/assets/agent-development-kit.png" width="200px" alt="Agent Development Kit">
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/sri-krishna-v/awesome-adk-agents?style=flat-square" alt="Stars">
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
  <a href="https://github.com/google/adk-python"><img src="https://img.shields.io/badge/Powered%20by-Google%20ADK-yellow" alt="Powered by Google ADK"></a>
  <a href="https://www.reddit.com/r/agentdevelopmentkit/"><img src="https://img.shields.io/badge/Reddit-r%2Fagentdevelopmentkit-FF4500?style=flat&logo=reddit&logoColor=white" alt="Reddit: r/agentdevelopmentkit"></a>
  <a href="https://deepwiki.com/google/adk-python"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
  <a href="https://mseep.ai/app/sri-krishna-v-awesome-adk-agents"><img src="https://mseep.net/pr/sri-krishna-v-awesome-adk-agents-badge.png" alt="MseeP.ai Security Assessment Badge" height="20"></a>
</p>

_A curated collection for Google's Agent Development Kit (ADK): the official SDKs and recipes, community projects and integrations, hackathon winners, and learning resources, from beginner tutorials to production multi-agent systems. Every entry was re-checked against current ADK (2.x) in November 2026: dead links, archived repos and pre-1.0 projects were removed._

## 📖 Table of Contents

- [🎯 What This List Solves](#-what-this-list-solves)
- [What is Google's Agent Development Kit (ADK)?](#what-is-googles-agent-development-kit-adk)
- [🧰 Official SDKs & Tools](#-official-sdks--tools)
- [🏆 Featured Projects](#-featured-projects)
- [🚀 Templates & Starters](#-templates--starters)
- [🌟 Community Excellence](#-community-excellence)
- [🏆 ADK Hackathons & Challenges](#-adk-hackathons--challenges)
- [📚 Learning Resources](#-learning-resources)
- [🎯 Official Examples](#-official-examples)
- [🚀 Getting Started](#-getting-started)
- [🤝 Contributing](#-contributing)
- [🙏 Acknowledgements](#-acknowledgements)

##

> Welcome to **Awesome ADK Agents**👋👋

A comprehensive ecosystem resource for Google's Agent Development Kit - an open-source agent framework with 22K+ GitHub stars, 4.3K+ forks and 400+ contributors on the Python repo alone. Whether you're exploring AI agents for the first time or deploying production multi-agent systems, this collection provides vetted implementations, learning paths, and deployment patterns from Google's official team and a vibrant global community.

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

**Google's Agent Development Kit (ADK)** is Google's open-source, code-first framework for building, evaluating and deploying AI agents. It is optimized for Gemini but model-agnostic (Gemini, Gemma, Claude, OpenAI, Ollama, vLLM, LiteLLM and more) and deployment-agnostic (any container, Cloud Run, GKE, or Agent Runtime on Google Cloud). Launched in 2025, ADK 2.0 reached general availability for Python on 2026-05-19 and the current Python release is v2.13.0; official SDKs exist for Python, TypeScript, Go, Java and Kotlin.

**Why ADK Matters:**

- **Google's Strategic Bet**: Deep integration with Agent Platform (formerly Vertex AI), Cloud Run, GKE, BigQuery, and Google's AI ecosystem
- **Production-First Design**: Built for deployment from day one, with evaluation, tracing and managed hosting options
- **Model Flexibility**: Optimized for Gemini, with adapters for Claude, OpenAI, Gemma, Ollama, vLLM, LiteLLM and more
- **Active Innovation**: 400+ contributors, frequent releases, and the graph-based Workflow runtime introduced in ADK 2.0
- **Growing Ecosystem**: Official recipes, third-party integrations (MongoDB, MCP, A2A protocol), and strong community momentum

### 🗝️ Key Features

- **🧭 Graph-Based Workflows (ADK 2.0)**: Deterministic, graph-based execution with routing, fan-out/fan-in, loops, retries, state, human-in-the-loop and nested workflows
- **🛠️ Rich Tool Ecosystem**: Pre-built tools, custom functions, OpenAPI specs, MCP tools, and Google ecosystem integration
- **💻 Code-First Development**: Define agents in code (Python, TypeScript, Go, Java, Kotlin) with full testability and version control
- **🔗 Multi-Agent Orchestration**: Compose specialized agents into scalable hierarchies; delegate with the Task API
- **🚀 Deploy Anywhere**: Agent Runtime, Cloud Run, GKE, or any containerized environment

### 🆕 What's New in ADK 2.x

- **Workflow runtime**: graph-based execution with routing, fan-out/fan-in, loops, retries, human-in-the-loop and nested workflows. `Workflow` replaces the now-deprecated `SequentialAgent`, `ParallelAgent` and `LoopAgent`. See the [ADK 2.0 migration notes](https://adk.dev/2.0/)
- **Five official SDKs**: Python 2.0 (May 2026), Go 2.0 (June 2026), TypeScript 2.0 (August 2026), Java 1.0 (March 2026) and Kotlin 1.0 (September 2026)
- **Skills, plugins and evaluation**: `SkillToolset`, a plugin system, a user simulator, and `adk optimize` for prompt optimization
- **A2A**: expose or consume agents over the Agent2Agent protocol, which reached v1.0 in March 2026
- **Renames**: the docs moved to [adk.dev](https://adk.dev/); Vertex AI Agent Engine is now Agent Runtime on Gemini Enterprise Agent Platform; `google/adk-samples` is now [google/adk-recipes](https://github.com/google/adk-recipes); Agent Starter Pack is archived in favor of [Agents CLI](https://github.com/google/agents-cli)

## 🧰 Official SDKs & Tools

_Google's official ADK repositories and the protocol ADK builds on_

- 🐍 [google/adk-python](https://github.com/google/adk-python) - The core open-source Python ADK: graph workflows, skills, plugins, evaluation and A2A
- 🐹 [google/adk-go](https://github.com/google/adk-go) - ADK for Go with graph workflows, human-in-the-loop and A2A (module `google.golang.org/adk/v2`)
- ☕ [google/adk-java](https://github.com/google/adk-java) - ADK for Java with plugins, event compaction, tool confirmation and A2A
- 🟦 [google/adk-js](https://github.com/google/adk-js) - ADK for TypeScript and JavaScript (npm `@google/adk`) with graph workflows
- 🤖 [google/adk-kotlin](https://github.com/google/adk-kotlin) - ADK for Kotlin and Android
- 🖥️ [google/adk-web](https://github.com/google/adk-web) - The developer UI behind `adk web`: chat, traces, evaluation and the visual builder
- 📖 [google/adk-docs](https://github.com/google/adk-docs) - Source of the official documentation at [adk.dev](https://adk.dev/)
- 🍳 [google/adk-recipes](https://github.com/google/adk-recipes) 📚 - Official runnable recipes: core patterns, contributed agents in five languages, and vertical skill plugins (formerly adk-samples)
- 🧰 [google/agents-cli](https://github.com/google/agents-cli) 🟡 - CLI and skills that let a coding agent scaffold, evaluate, deploy and observe ADK agents on Google Cloud; successor to Agent Starter Pack
- 🧩 [google/adk-python-community](https://github.com/google/adk-python-community) 🟡 - Community-contributed ADK tools, service integrations and deployment scripts (`pip install google-adk-community`)
- 🔗 [a2aproject/A2A](https://github.com/a2aproject/A2A) 🟡 - The Agent2Agent open protocol (v1.0) for interoperable agents, supported natively by ADK

## 🏆 Featured Projects

_My showcase agents demonstrating production-ready ADK implementations_

| Agent Name | Category/Domain | Short Description | Badges |
|------------|----------------|-------------------|---------|
| [Job Interview Agent](./my-adk-agents/job-interview-agent/) | HR/Recruitment | AI-powered interview assistant with calendar integration and real-time feedback | ⭐🏭🟡 |
| [Education Path Advisor for India](./my-adk-agents/education-path-advisor/) | Education/Career Guidance | Multi-agent AI advisor for Indian students/parents: personalized pathways, stepwise plans, risk analysis, and region/reservation-aware guidance | ⭐🟡 |
| [Academic Research Assistant](./my-adk-agents/academic-research-assistant/) | Research/Academia | Multi-agent literature review assistant with profile analysis, robust paper search (with SerpAPI fallback), and personalized research synthesis | 🟡 |
| [Project Manager Agent](./my-adk-agents/project-manager-agent/) | Productivity/Management | Automated project management with task tracking and progress monitoring | 🟡 |
| [Learning Content System (WIP)](./my-adk-agents/learning-content-system%28WIP%29/) | Education/Content Creation | Multi-agent system that turns source material into lessons with visuals, audio, and slides, using Sequential, Parallel, and Loop agents, MCP tools, and a quality-check loop | 🚧🟡 |
| [Local Code Assistant (WIP)](./my-adk-agents/data-analyst/) | Software Development | Single agent that runs a local model (Ollama `qwen3:8b` via LiteLLM) and suggests React, Vue, Next.js, and Node.js code | 🚧🟢 |

**Badge Legend:**

- ⭐ **My Showcase** - Featured portfolio projects
- 🏭 **Production-Ready** - Has deployment code and infrastructure
- 🔥 **Community Pick** - Outstanding community traction
- 🚧 **In Development** - Work in progress
- 📚 **Learning Resource** - Educational/tutorial content (official examples are demo/educational only)
- 📖 **Tutorial / Walkthrough**, 📝 **Article**, 🎥 **Video**, 🧪 **Hands-on Lab**, 🎓 **Course**, 💡 **Worked Example**
- 🟢🟡🔴 **Difficulty**: Beginner, Intermediate, Advanced

---

## 🚀 Templates & Starters

_Ready-to-use templates to kickstart your ADK projects_

> Agent Starter Pack is archived. For Google's official scaffolding, use [google/agents-cli](https://github.com/google/agents-cli).

- 🔍 [Deep Search ADK Quickstart](https://github.com/google/adk-recipes/tree/main/core/python/deep-search) 🏭🔴📚 - Official fullstack research agent (formerly Gemini Fullstack) with a React frontend, human-in-the-loop plan approval, autonomous research pipelines, and Cloud Run deployment
- 📱 [kkdai/linebot-adk](https://github.com/kkdai/linebot-adk) 🏭🟢 - LINE Bot template with Docker, Cloud Run deployment, and security configurations
- 💬 [danishi/slack-bot-adk-python-cloudrun](https://github.com/danishi/slack-bot-adk-python-cloudrun) 🏭🟡 - Slack Bolt bot backend powered by ADK and deployed on Cloud Run
- ☕ [glaforge/adk-java-maven-template](https://github.com/glaforge/adk-java-maven-template) 🟢 - Maven project template for a first ADK for Java agent
- 🚀 [neo4j-labs/create-context-graph](https://github.com/neo4j-labs/create-context-graph) 🟡 - Neo4j Labs scaffolding CLI that generates domain-specific context-graph agent apps; `--framework google-adk` generates an ADK agent backend

---

## 🌟 Community Excellence

_Outstanding community projects showcasing ADK capabilities_

### Multi-Agent Systems

- 🤖 [derailed-dash/rickbot-adk](https://github.com/derailed-dash/rickbot-adk) 🏭🟡 - Multi-personality chatbot with FastAPI backend, Next.js UI, OAuth, and multi-agent RAG/search architecture
- 🚀 [kweinmeister/agentic-trading](https://github.com/kweinmeister/agentic-trading) 🏭🔴 - Trading-simulation sample demonstrating ADK and A2A interoperability: an AlphaBot trading agent and a RiskGuard risk agent communicate over the A2A protocol; Dockerfiles and Cloud Build configs included. For informational purposes only
- 📊 [vladkol/CRM Data Q&A Agent](https://github.com/vladkol/crm-data-agent) 🏭🔴 - Multi-agent system with advanced RAG and NL2SQL over Salesforce data, with Cloud Run deployment scripts. Reference only: last updated June 2025 and pinned to ADK 1.3 with older Gemini model IDs
- 🌐 [seehiong/adk-web-multi-agent](https://github.com/seehiong/adk-web-multi-agent) 🟡 - Multi-agent system with Google ADK and OpenRouter models coordinating specialist agents to query PostgreSQL (via MCP Toolbox) and Data Commons

### Frameworks & Platforms Built on ADK

- 🏗️ [antiv/mate](https://github.com/antiv/mate) 🏭🔴🔥 - Production-ready multi-agent orchestration engine built on Google ADK with database-driven agent config, 50+ LLM providers, MCP protocol, persistent memory, web dashboard, and RBAC
- 🏗️ [apowerb/apowerb](https://github.com/apowerb/apowerb) 🏭🔴 - Open-source platform that builds Google ADK agents (single, sequential, parallel, loop) from a web UI or REST API, with LiteLLM models, RAG, Text-to-SQL, MCP tools, token quotas and per-session audit; Docker Compose and Helm
- ☁️ [volcengine/veadk-python](https://github.com/volcengine/veadk-python) 🏭🔴 - Volcengine's agent development kit layered on Google ADK, with Volcengine model, memory, tracing and AgentKit deployment integrations; Go port: [volcengine/veadk-go](https://github.com/volcengine/veadk-go)
- 🧱 [yaalalabs/agent-kernel](https://github.com/yaalalabs/agent-kernel) 🏭🔴 - Runtime that runs Google ADK, LangGraph, CrewAI, OpenAI Agents SDK and others side by side, adding governance, pause/resume, sessions and multi-cloud deployment
- 🧪 [opensage-agent/opensage-adk](https://github.com/opensage-agent/opensage-adk) 🔴 - Research kit on ADK where the model creates its own agent topology, synthesizes toolsets and manages structured memory at runtime (paper and docs linked; pinned to ADK 1.x)

### UI, Protocols & Runtimes

- 🖥️ [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) 🟡🔥 - The AG-UI agent-to-frontend protocol; its ADK middleware (Python, JS, TypeScript) streams ADK agents to AG-UI clients
- 🪁 [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) 🟡🔥 - Frontend stack for agents and generative UI, with an ADK + Angular starter (`examples/integrations/adk-angular`)
- 🖥️ [trendmicro/adk-agui-middleware](https://github.com/trendmicro/adk-agui-middleware) 🟡 - Python middleware bridging Google ADK agents with the AG-UI protocol via Server-Sent Events for real-time agent interactions in frontend applications
- 🎛️ [neo-fetch/draw-your-agents](https://github.com/neo-fetch/draw-your-agents) 🟡 - Browser-based visual builder that compiles drag-and-drop agent graphs (or draw.io XML) into runnable ADK 2.0 graph-workflow projects, or LangGraph (AGPL-3.0)
- ⚡ [Atmosphere/atmosphere](https://github.com/Atmosphere/atmosphere) 🔴 - Portable JVM agent runtime whose `atmosphere-adk` module bridges ADK Java agent streams to WebSocket, SSE and gRPC clients
- ⏱️ [temporalio/samples-python (google_adk_agents)](https://github.com/temporalio/samples-python/tree/main/google_adk_agents) 🔴 - Run ADK agents durably inside Temporal workflows; the integration ships as the `temporalio-google-adk` package
- ⚡ [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) 🏭🔴🔥 - Cascading runtime that optimizes cost, latency, quality, and policy decisions inside the agent loop, with a Google ADK integration and support for 17+ model providers

### Observability, Evaluation & Security

- 🔭 [Arize-ai/openinference](https://github.com/Arize-ai/openinference) 🟡 - OpenTelemetry instrumentation for AI apps with ADK support (Python instrumentor and an ADK Java example) for any OTel backend
- 🔎 [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) 🟡 - AI observability and evaluation platform with ADK integration guides for Python and Java
- 🧭 [langfuse/langfuse](https://github.com/langfuse/langfuse) 🟡 - Open-source LLM observability that traces ADK agents via OpenTelemetry
- 🔬 [comet-ml/opik](https://github.com/comet-ml/opik) 🟡 - Debug, evaluate and monitor LLM apps and agents, with a native ADK integration
- 📊 [mlflow/mlflow](https://github.com/mlflow/mlflow) 🟡 - AI engineering platform with ADK tracing and `mlflow.genai.scorers.google_adk` scorers for evaluating ADK agents
- 🕵️ [AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops) 🟡 - Agent monitoring and cost tracking with a built-in ADK instrumentor
- 🧿 [monocle2ai/monocle](https://github.com/monocle2ai/monocle) 🟡 - OpenTelemetry-based GenAI tracing framework with ADK support and a sample ADK travel agent
- 📈 [grafana/agento11y](https://github.com/grafana/agento11y) 🟡 - Grafana Agent Observability SDK with ADK helpers for Python, TypeScript, Go and Java that map ADK callbacks to generation and tool recordings
- 🧪 [arklexai/arksim](https://github.com/arklexai/arksim) 🟡 - Multi-turn simulation testing where LLM-driven synthetic users converse with your agent to find failures before production; includes an ADK example
- 🚧 [trustabl/agent-reliability-analyzer](https://github.com/trustabl/agent-reliability-analyzer) 🟡 - Local, deterministic static scanner (340+ rules) that finds and fixes agent reliability failures, with deep Google ADK coverage
- 🚦 [ThreeMoonsLab/agents-shipgate](https://github.com/ThreeMoonsLab/agents-shipgate) 🟡 - Deterministic merge gate performing local-first, static Tool-Use Readiness review for MCP, OpenAPI, and SDK tool surfaces, including Google ADK Python and YAML configs (CLI + GitHub Action)
- 🧱 [pipelab-org/pipelock](https://github.com/pipelab-org/pipelock) 🟡 - Open-source agent firewall for MCP and agent egress (exfiltration, SSRF and prompt-injection scanning, signed action receipts) with a Google ADK guide
- 🛂 [sondera-ai/sondera-harness-python](https://github.com/sondera-ai/sondera-harness-python) 🟡 - Deterministic guardrails for agents with native ADK middleware (also LangGraph and Strands)
- 🛡️ [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) 🏭🔴🔥 - Governance toolkit for AI agents (maintained by Microsoft; successor to the archived `imran-siddique/agent-os`) with policy enforcement, zero-trust identity, execution sandboxing, and OWASP Agentic Top 10 coverage (7 full, 3 partial per its README); includes a Google ADK adapter
- 🔐 [Idun-Group/idun-agent-platform](https://github.com/Idun-Group/idun-agent-platform) 🏭🔴🔥 - Open-source Agent Governance Platform that turns any LangGraph or ADK agent into a production-ready service with AG-UI, OpenTelemetry, MCP, memory, guardrails, SSO, and RBAC
- 🔌 [RubensZimbres/Agent-to-Agent-Security-Pipeline](https://github.com/RubensZimbres/Agent-to-Agent-Security-Pipeline) 🔴 - Security-focused multi-agent pipeline using ADK + A2A + MCP: natural-language salary-database queries pass through threat-detection, SQL-execution, and PII-masking agents (requires `google-adk>=1.0,<2.0`)
- ✅ [ceodaradigu/proofline-agent](https://github.com/ceodaradigu/proofline-agent) 🏭🟡 - Evidence-first Google ADK agent that blocks external action until fresh authoritative evidence passes a deterministic four-state gate and explicit human approval, with Cloud Run deployment and unit tests
- 🚦 [vulnify/vulnify-examples: google-adk](https://github.com/vulnify/vulnify-examples/tree/main/google-adk) 🟢 - `before_tool_callback` that checks each tool call with Vulnify before it runs: ALLOW runs the tool, REVIEW holds it until a person approves, BLOCK refuses it. Runs offline in mock mode (no API or model key) with pytest tests
- 🧾 [Cygnux-Labs/Tracekit](https://github.com/Cygnux-Labs/Tracekit) 🟡 - ADK plugin that sends every tool call of every agent a Runner runs, sub-agents included, to a separate signer that allows, denies or holds it for a person, and records each call and result in a signed, hash-chained log that verifies offline

### Memory, Session & Storage

- 🧠 [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) 🟡 - Agent memory that learns; its ADK integration implements `BaseMemoryService` (retain on session end, recall on search) plus explicit tool wrappers
- 🧠 [moorcheh-ai/memanto (google-adk)](https://github.com/moorcheh-ai/memanto/tree/main/integrations/google-adk) 🟡 - Drop-in ADK memory service that extracts typed memories (preferences, facts, decisions) from turns, replacing `InMemoryMemoryService`
- 🗃️ [achetronic/adk-utils-go](https://github.com/achetronic/adk-utils-go) 🏭🟡 - Go utilities for ADK: OpenAI and Anthropic model clients, Redis sessions, Postgres + pgvector long-term memory, filesystem artifacts and a context-window guard plugin
- 🗄️ [edu010101/adk-extra-services](https://github.com/edu010101/adk-extra-services) 🟡 - Community Python package with extra session (Redis, MongoDB) and artifact (S3, Azure, Supabase, local folder) service backends for ADK. Last updated October 2025: artifact services lack the newer `list_artifact_versions` / `get_artifact_version` methods, so test against your ADK version

### Domain-Specific Applications

- 🛡️ [dandye/adk_runbooks](https://github.com/dandye/adk_runbooks) 🟡 - Manager-orchestrated multi-agent security operations system (incident response, threat hunting, detection engineering, alert triage) with a progressive-disclosure skills architecture
- 🏥 [hastimal/gemini-healthcare-agentic-platform](https://github.com/hastimal/gemini-healthcare-agentic-platform) 🏭🟡 - Agentic healthcare search with a three-agent ADK workflow, MCP, FHIR interoperability, grounding and citations; Streamlit demo, Docker and GKE deployment
- 💹 [RubensZimbres/Financial-Multi-Agents-Graph-Databasee](https://github.com/RubensZimbres/Financial-Multi-Agents-Graph-Databasee) 🏭🔴 - Multi-agent financial analytics with Neo4j graph database, SEC filings RAG, and ML stock predictions (requires `google-adk>=1.0,<2.0`)
- 🏭 [ntg2208/production-ai-customer-support](https://github.com/ntg2208/production-ai-customer-support) 🔴 - Multi-agent customer-support system with Policy Agent, Ticket Agent, and Master orchestrator featuring location intelligence, RAG knowledge base, guardrails, evaluation code, and step-by-step tutorials
- 🔧 [codeninja/Mongoose Migration Agent System](https://gist.github.com/codeninja/a6e117a3480de8d32dd9ef01b519cdae) 🔴🔥 - Multi-agent system for automated Mongoose database migration (v6→v8) with specialized agents and MCP integration
- 📊 [AI Trends Analysis Pipeline](https://github.com/Astrodevil/ADK-Agent-Examples/tree/main/analyzer_agent) 🟡🔥 - Comprehensive AI analysis pipeline using Exa Search, Tavily Search, Firecrawl and Nebius AI
- 📁 [Job Finder Agent](https://github.com/Astrodevil/ADK-Agent-Examples/tree/main/jobfinder_agent) 🟡 - Sequential Agent using Mistral OCR, Linkup API and Nebius AI
- 📧 [Email ADK Agent](https://github.com/Astrodevil/ADK-Agent-Examples/tree/main/email_adk_agent) 🟢 - Email management and automation agent using Resend API
- 🔧 [serkanh/sre-bot](https://github.com/serkanh/sre-bot) 🏭🟡 - SRE/DevOps bot built on Google ADK for intelligent infrastructure management and incident response
- 🔍 [sreekarrs/JobSearch-Agent](https://github.com/sreekarrs/JobSearch-Agent) 🏭🟡 - Job search automation built around a LinkedIn scraper, with ADK agents that parse job details and generate tailored CVs and cover letters; Docker and deploy workflow included
- 👔 [akajammythakkar/adk_hiring_agent](https://github.com/akajammythakkar/adk_hiring_agent) 🟡 - AI-powered hiring agent using Google ADK and Gemini to analyze resumes, assess skills, and match candidates via multi-agent collaboration
- 🔬 [emansarahafi/Research-Assistant-Agent](https://github.com/emansarahafi/Research-Assistant-Agent) 🟡 - Notebook-based multi-agent research assistant with Researcher, Analyst, and Formatter sub-agents using ArXiv search (README describes Flask and Vertex AI deployment paths)
- 📚 [Anubhob435/Ai-Agents-EditorHouse](https://github.com/Anubhob435/Ai-Agents-EditorHouse) 🟡 - Multi-agent book creation system using Google ADK that plans, writes, edits, illustrates, and compiles complete books from a single topic prompt with MongoDB metadata tracking
- 💬 [B4K2/WhatsApp-agent](https://github.com/B4K2/WhatsApp-agent) 🟡 - Intelligent WhatsApp agent built with MCP + Google ADK for conversational automation
- 📚 [Beever-AI/beever-atlas](https://github.com/Beever-AI/beever-atlas) 🟡 - Conversational wiki knowledge base with Slack/Teams/Discord bots, RAG, and MCP integration built on Google ADK
- 🌐 [anxuanzi/bua](https://github.com/anxuanzi/bua) 🟡 - AI-powered browser automation for Go — describe tasks in plain English and let the ADK-powered agent handle the clicks via vision-language models

---

## 🏆 ADK Hackathons & Challenges

_Winners of hackathons where teams built with ADK. Each list comes from the organizer's own announcement. Where ADK was optional, only winners whose code or project page shows ADK are listed._

### ADK-Focused Hackathons

#### Agent Development Kit Hackathon with Google Cloud (2025)

> **477 submissions** | **10,400+ participants from 62 countries** | [Winners announcement](https://cloud.google.com/blog/products/ai-machine-learning/adk-hackathon-results-winners-and-highlights) | [All submissions](https://googlecloudmultiagents.devpost.com/project-gallery)

- 🥇 **Grand Prize ($15,000)**: [SalesShortcut](https://devpost.com/software/salesshortcut) - AI-powered Sales Development Representative system with a multi-agent architecture for automated lead generation, research, proposal generation, and outreach ([source](https://github.com/merdandt/SalesShortcut))
- 🌎 **North America ($8,000)**: [Energy Agent AI](https://devpost.com/software/energy-agent-ai) - Multi-agent AI transforming energy customer management through Google ADK orchestration ([source](https://github.com/hazardscarn/energyagentai))
- 🌍 **Europe, Middle East & Africa ($8,000)**: [Nexora-AI](https://devpost.com/software/teachai-upzofa) - Next-gen personalized education with interactive lessons, visuals, quizzes, and smart AI support ([source](https://github.com/M4RKUS28/Nexora))
- 🌏 **Asia Pacific ($8,000)**: [GreenOps](https://devpost.com/software/greenops-gzp4aj) - AI team that continuously audits, forecasts, and optimizes cloud infrastructure for sustainability ([source](https://github.com/niksm7/GreenOps))
- 🌎 **Latin America ($8,000)**: [Edu.AI](https://devpost.com/software/edu-ai-multi-agent-educational-system-for-brazil) - Brazilian education system with agents that evaluate essays, generate personalized study plans, and create interdisciplinary mock exams ([source](https://github.com/giovannamoeller/edu-ai-adk-version))
- 🎖️ **Honorable Mention ($1,000)**: [Particle Physics Agent](https://devpost.com/software/particle-physics-agent) - Physics AI agent converting natural language into validated Feynman diagrams using real physical laws ([source](https://github.com/bee4come/Particle-Physics-Agent))
- 🎖️ **Honorable Mention ($1,000)**: [TradeSage AI](https://devpost.com/software/tradesage-ai) - Multi-agent financial analysis platform for evaluating trading hypotheses with ADK, Agent Engine, Cloud Run and Vertex AI ([source](https://github.com/sudsk/tradesage-mvp))
- 🎖️ **Honorable Mention ($1,000)**: [Bleach](https://devpost.com/software/bleach-7tqdmo) - Visual AI agent builder for Google ADK: describe agents in plain English, design them visually, and test instantly ([source](https://github.com/vivek100/bleachAgentBuilder))

---

## 📚 Learning Resources

_Comprehensive guides, tutorials, and educational content_

### ⭐ Community Training Platforms

- 🎓 **[mauripsale/doc-adk-training](https://github.com/mauripsale/doc-adk-training)** 🟡📚🔥 - "ADK: From Zero to Hero": 45-module ADK 2.0 curriculum by GDE and Google Cloud trainer Maurizio Ipsale with labs, quizzes, a solution vault and a Codespaces/Cloud Shell setup ([site](https://mauripsale.github.io/doc-adk-training/))
- 🏆 **[Google ADK Training Hub](https://raphaelmansuy.github.io/adk_training/)** 🟢🟡🔴📚 - Community-run training site with 35 tutorials covering ADK agents, tools, multi-agent patterns, deployment, and React/Next.js integration. Written for ADK 1.x (1.16+); check the [ADK 2.0 migration notes](https://adk.dev/2.0/) before following the code

### 🎓 Courses & Certifications

- 🎓 [Building Live Voice Agents with Google's ADK (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/building-live-voice-agents-with-googles-adk/) 🟡🎓 - Short course by Google engineers: voice agent, sessions, state and memory, tools, callback guardrails, multi-agent orchestration, and a Gemini TTS podcast capstone
- 🎓 [A2A: The Agent2Agent Protocol (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) 🟡🎓 - Course with Google Cloud and IBM Research: wrap agents built on ADK and other frameworks in A2A servers and orchestrate them in a healthcare multi-agent system
- 🎓 [Develop Agents with Agent Development Kit (ADK) track (DataCamp x Google Cloud)](https://www.datacamp.com/tracks/develop-agents-with-agent-development-kit-adk) 🟢🎓 - Five Google-created courses: build agents, optimize agent behavior, add tools, and manage memory and state
- 🎓 [Build Your First Agent with Agent Development Kit (Google Skills)](https://www.skills.google/course_templates/1563) 🟢🎓 - Introductory Google Skills course for building and running an ADK agent in Python and YAML
- 🎓 [5-Day AI Agents Intensive on Kaggle](https://www.kaggle.com/learn-guide/5-day-agents) 📚🎓 - Free, self-paced Learn Guide from Google and Kaggle's live course (Nov 2025) with whitepapers, podcasts, codelabs and recorded livestreams on agent foundations, tools, memory, evaluation and production; the hands-on codelabs use ADK

### 🚀 Quickstart Courses

- 📚 [A2A Crash Course by Brandon Hancock](https://github.com/bhancockio/agent2agent) 🟡📚 - Comprehensive guide to building agent-to-agent (A2A) communication using ADK with [Youtube](https://www.youtube.com/watch?v=mFkw3p5qSuA&t=172s) tutorial
- 📚 [chongdashu/adk-made-simple](https://github.com/chongdashu/adk-made-simple) 🟢📚 - From basics to A2A integration with real world applications and projects
- 📚 [arjunprabhulal/google-adk-masterclass](https://github.com/arjunprabhulal/google-adk-masterclass) 🟡📚 - 20-module masterclass covering ADK basics through advanced topics including MCP, Vertex AI, and production deployment
- 📚 [omerbsezer/Fast-LLM-Agent-MCP](https://github.com/omerbsezer/Fast-LLM-Agent-MCP) 🟡📚 - Comprehensive resource covering LLMs, RAG, fine-tuning, agents, MCP, and Google ADK both theoretically and practically with reference documents

### 🧪 Official Hands-on Learning

- 🧪 [Google ADK Codelabs](https://codelabs.developers.google.com/?text=ADK) 📚 - Interactive, guided tutorials with hands-on coding exercises from Google
- 🧪 [ADK 2 Orchestration: Graph, Collaborative & Dynamic Workflows](https://codelabs.developers.google.com/adk2/instructions) 🟡🧪 - About 50-minute Colab codelab teaching ADK 2.0 graph, collaborative (chat, single-turn, task) and dynamic workflows by building a race-day coach, one runnable step at a time
- 🧪 [Build Your First ADK Agent Workforce](https://cloud.google.com/blog/topics/developers-practitioners/build-your-first-adk-agent-workforce) 🟢🧪 - Learning path with 3 official codelabs: building autonomous agents, empowering agents with tools, and orchestrating multi-agent systems
- 🧪 [Building ADK Agents with Skills and Tools (Next '26 Developer Keynote)](https://codelabs.developers.google.com/next26/dev-keynote/building-agents-with-skills) 🟡🧪 - Codelab building a marathon-planner agent with a modular prompt, `SkillToolset` and Google Maps MCP tools, tested in `adk web` and deployed to Agent Runtime
- 🧪 [Building a Multi-Agent System using Gemini and Gemma models](https://codelabs.developers.google.com/next26/multi-agent-system) 🟡🧪 - Researcher, Judge, Content Builder and Orchestrator agents wired with workflow agents, `RemoteA2aAgent` and a Gemma model on a Cloud Run GPU
- 🧪 [Stateful Data Science Agent on Agent Runtime](https://codelabs.developers.google.com/next26/adk-deploy-scale) 🟡🧪🏭 - Codelab deploying a BigQuery data-science agent with Memory Bank and Cloud Trace to Agent Runtime with `adk deploy`
- 🧪 [Frontend Experiences with ADK and A2UI](https://codelabs.developers.google.com/next26/adk-a2ui) 🟡🧪 - Short codelab where an ADK agent replies with A2UI JSON that `adk web` renders as cards, lists and buttons
- 🧪 [Build AI Agents with ADK for Java](https://codelabs.developers.google.com/adk-java-getting-started) 🟢🧪 - Codelab building persona, tool, sub-agent and workflow agents in Java
- 🧪 [GoogleCloudPlatform/race-condition](https://github.com/GoogleCloudPlatform/race-condition) 🔴📚 - Multi-agent marathon simulation (ADK, Gemini, A2A, Go/Python/Angular) from the Google Cloud Next '26 Developer Keynote
- 🧪 [Building GraphRAG Agents with ADK and Neo4j](https://codelabs.developers.google.com/neo4j-adk-graphrag-agents) 🟡📚💡 - Official codelab building a multi-agent investment research system with Neo4j, MCP Toolbox, and GraphRAG for multi-hop reasoning (uses `google-adk>=1.21.0` and preview Gemini 3.x models)

### 📖 Tutorials & Walkthroughs

- 📖 [chongdashu/adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course) 🟡📖 - Complete multi-agent system with ADK + A2A + MCP integration, featuring Notion and ElevenLabs with full architecture, testing, and [YouTube](https://www.youtube.com/watch?v=s6-Ofu-uu2k) tutorial (pinned to ADK 1.2)
- 📖 [mongodb-developer/MongoDB-ADK-Agents](https://github.com/mongodb-developer/MongoDB-ADK-Agents) 🟡📖💡 - Official MongoDB grocery shopping agent with Atlas Vector Search, updated for ADK 2.x, with a complete dataset and step-by-step setup ([companion article](https://medium.com/google-cloud/build-a-python-ai-agent-in-15-minutes-with-google-adk-and-mongodb-atlas-vector-search-groceries-b6c4af017629))
- 📖 [kweinmeister/agent-design-patterns](https://github.com/kweinmeister/agent-design-patterns) 🟡📚 - Executable cookbook of agent architecture patterns using ADK and Gemini, with a published guide
- 📖 [datascalehq/datascale](https://github.com/datascalehq/datascale/tree/main/cookbook/tutorials/agent_docs) 🟡📖 - Multi-agent documentation builder with planner and writer agents that analyze codebases and generate structured knowledge bases ([companion article](https://medium.com/gitconnected/building-a-knowledge-base-from-your-codebase-using-google-adk-7508e845bdc1))
- 📖 [meteatamel/adk-demos](https://github.com/meteatamel/adk-demos/) 🟢📖 - Collection of demos and tutorials for Google's Agent Development Kit
- 📖 [sokart/adk-walkthrough](https://github.com/sokart/adk-walkthrough) 🟡📖 - Step-by-step guides and examples using the open-source Python ADK framework
- 📖 [bhancockio/MCP Integration Tutorial](https://github.com/bhancockio/adk-mcp-tutorial) 🟡📖 - Model Context Protocol (both local and remote) with ADK with [Youtube](https://www.youtube.com/watch?v=HkzOrj2qeXI&t=2362s) tutorial
- 📖 [thomas-chong/google-adk-visual-agent-builder-demo](https://github.com/thomas-chong/google-adk-visual-agent-builder-demo) 🟡📖 - Complete demo of Google ADK Visual Agent Builder with a multi-agent research system walkthrough
- 📖 [lavinigam-gcp/build-with-adk](https://github.com/lavinigam-gcp/build-with-adk) 🏭🟡📖 - Design patterns and production-ready architectures for building multi-agent AI systems with Google ADK on Cloud Run, Vertex AI, and AI Studio
- 📝 [Give a Google ADK agent per-user OAuth tools with Scalekit](https://docs.scalekit.com/agentkit/examples/google-adk/) 🟡📝 - Scalekit's guide to a Gmail-reading ADK agent: tools come either as native ADK tools from `actions.google.get_tools()` or from a Scalekit virtual MCP server through `McpToolset`, and a connected-account check sends the user an authorization link until the account is active. Sample code: [scalekit-inc/google-adk-agent-example](https://github.com/scalekit-inc/google-adk-agent-example).

#### 🎓 Google ADK Tutorial Examples

_Comprehensive tutorial examples from [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) demonstrating ADK patterns and capabilities_

**Fundamentals:**

- 📖 [Starter Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/1_starter_agent) 🟢📖 - Your first ADK agent: basic agent creation, the ADK workflow, and simple text processing
- 📖 [Model-Agnostic Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/2_model_agnostic_agent) 🟢📖 - Running ADK with non-Gemini models, with OpenAI and Anthropic Claude integration sub-examples
- 📖 [Memory Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/5_memory_agent) 🟢📖 - Memory and session management with in-memory conversation handling and persistent SQLite storage
- 📖 [Simple Multi-Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/8_simple_multi_agent) 🟢📖 - Multi-agent orchestration via a researcher pipeline of specialized agents in a sequential workflow
- 📖 [ADK YAML Examples](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/adk_yaml_examples) 🟢📖 - Config-driven agent definitions using ADK's YAML format

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

- 📖 [Sequential Multi-Agent Pattern](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/9_multi_agent_patterns/9_1_sequential_agent) 🟢📖 - Step-by-step multi-agent coordination (uses `SequentialAgent`, deprecated in ADK 2.x in favor of `Workflow`; still runs)
- 📖 [Loop Multi-Agent Pattern](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/9_multi_agent_patterns/9_2_loop_agent) 🟢📖 - Iterative multi-agent workflows (uses `LoopAgent`, deprecated in ADK 2.x in favor of `Workflow`; still runs)
- 📖 [Parallel Multi-Agent Pattern](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/9_multi_agent_patterns/9_3_parallel_agent) 🟢📖 - Concurrent multi-agent execution (uses `ParallelAgent`, deprecated in ADK 2.x in favor of `Workflow`; still runs)

**Multi-Agent Applications:**

- 📖 [AI Financial Coach Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/ai_financial_coach_agent) 🟡📖 - Financial advisory system with specialized agent teams
- 📖 [AI Home Renovation Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/ai_home_renovation_agent) 🟡📖 - Home improvement planning with multi-agent coordination
- 📖 [AI SEO Audit Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_seo_audit_team) 🟡📖 - Website SEO analysis with specialized agent teams
- 📖 [Multimodal UI/UX Feedback Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_uiux_feedback_agent_team) 🟡📖 - Design review system with multimodal capabilities
- 📖 [AI Negotiation Battle Simulator](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/ai_negotiation_battle_simulator) 🟡📖 - Buyer, seller, and orchestrator agents simulate negotiations with an AG-UI frontend (ag_ui_adk)
- 📖 [AI Sales Intelligence Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_sales_intelligence_agent_team) 🟡📖 - Sequential research agents that generate competitive battle cards and comparison charts
- 📖 [AI VC Due Diligence Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_vc_due_diligence_agent_team) 🟡📖 - Sequential agents producing HTML reports, infographics, and financial charts for VC due diligence

**Single-Agent Applications:**

- 📖 [Earnings Call Analyst Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/earnings_call_analyst_agent) 🟡📖 - Ingests and analyzes earnings calls with transcription, research, and analyst agents
- 📖 [AI Consultant Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/ai_consultant_agent) 🟡📖 - Business consulting agent using Google Search grounding and session management

### 📝 Articles & Best Practices

**Official Google posts:**

- 📝 [Announcing ADK for Go 2.0](https://developers.googleblog.com/announcing-adk-go-20) 🟡📝 - Clearest official explanation of the ADK 2.0 model: graph-based workflow engine, human-in-the-loop pause/resume, dynamic nodes, retries, and Chat/Task/SingleTurn agent modes
- 📝 [Hill-Climbing Agent Quality with Agents CLI Evaluation](https://developers.googleblog.com/hill-climbing-agent-quality-with-agents-cli-evaluation/) 🟡📝 - Baseline evals, regression checks, model comparison, nightly runs and automated prompt tuning with Agents CLI
- 📝 [Build Cross-Language Multi-Agent Team with ADK and A2A](https://developers.googleblog.com/build-cross-language-multi-agent-team-with-google-agent-development-kit-and-a2a/) 🟡📝 - Python extraction agent plus Go compliance validator orchestrated over A2A with a manual-review fallback
- 📝 [Build zero-trust AI agents with Google's Agent Development Kit](https://developers.googleblog.com/build-zero-trust-ai-agents-with-googles-agent-development-kit/) 🔴📝 - Prompt-injection-resistant agent with signed database writes, gVisor sandboxing and deterministic checks in CI
- 📝 [Building Collaborative AI: A Developer's Guide to Multi-Agent Systems with ADK](https://cloud.google.com/blog/topics/developers-practitioners/building-collaborative-ai-a-developers-guide-to-multi-agent-systems-with-adk) 🟢📝 - LLM, workflow and custom agents, sub-agents vs AgentTool, and state, with companion videos and a sample repo
- 📝 [ADK Architecture: When to Use Sub-Agents versus Agents as Tools](https://cloud.google.com/blog/topics/developers-practitioners/where-to-use-sub-agents-versus-agents-as-tools) 🟡📝 - Essential architectural guide with decision matrix for choosing between sub-agents and agent tools, featuring real-world use cases (data agents, travel planners) and best practices for multi-agent systems

**Community articles:**

- 📝 [Ralph Loop with Google ADK: AI Agents That Verify, Not Guess](https://medium.com/google-cloud/ralph-loop-with-google-adk-ai-agents-that-verify-not-guess-b41f71c0f30f) 🔴📝🔥 - Advanced guide to implementing Ralph Loop pattern for external verification-driven workflows, featuring multi-agent Dockerfile generation with Docker-based validation and iterative refinement until objective success criteria are met ([demo repo](https://github.com/thomas-chong/google-adk-ralph-loop-demo))
- 📝 [Choosing the Right Deployment Path for Your Google ADK Agents](https://medium.com/google-cloud/choosing-the-right-deployment-path-for-your-google-adk-agents-86c89c251ab5) 🟡📝 - Google Cloud guide comparing deployment strategies (Cloud Run vs Vertex AI vs GKE) for production ADK agents
- 📝 [Announcing a Datastore-Backed Session Service for the ADK](https://medium.com/google-cloud/announcing-a-new-datastore-backed-session-service-for-the-adk-d14596ae28df) 🟡📝🏭 - Google Cloud solution for persistent agent sessions in serverless environments using Cloud Datastore instead of SQLite
- 📝 [Drawing Charts in Your AI Agent Frontend with Google ADK](https://medium.com/@dconsonni/drawing-charts-in-your-ai-agent-frontend-with-google-adk-9c74a4a98931) 🟡📝 - Guide to agent-generated visualizations using ADK Artifacts with Apache ECharts/vis-network, featuring FastAPI integration and session-scoped artifact management
- 📝 [Building Next-Gen AI Agents with Google ADK, MCP, RAG and Ollama](https://medium.com/@tam.tamanna18/building-next-gen-ai-agents-with-google-adk-mcp-rag-and-ollama-ca3c1e5002da) 🟡📝💡 - Comprehensive tutorial on building multi-agent chatbots integrating ADK + MCP + RAG + Ollama with step-by-step code and architecture diagrams
- 📝 [Google ADK + LM Studio: The Power Couple of Local Agent Development](https://medium.com/@c-damien/google-adk-lm-studio-the-power-couple-of-local-agent-development-2dd225bae36f) 🟡📝💡 - Complete guide to running ADK agents locally with LM Studio, featuring setup instructions, model configuration, and privacy-focused development without cloud dependencies
- 📝 [Optimize Your Google ADK Agent's SOP with GEPA](https://raphaelmansuy.github.io/adk_training/blog/gepa-optimization-tutorial/) 🔴📝 - Walkthrough of prompt optimization with GEPA (reflective prompt evolution) on a small 5-scenario demo, with sample code

### 🎥 Video Content

- 🎥 [Introducing Agent Development Kit (ADK)](https://www.youtube.com/watch?v=zgrOwow_uTQ) 🟢🎥 - 3-minute product overview shown at launch
- 🎥 [Getting started with ADK](https://www.youtube.com/watch?v=44C8u0CDtSo) 🟢🎥 - "Hello-world" coding session from pip install to first agent
- 🎥 [Google Launches an Agent SDK – ADK Deep Dive](https://www.youtube.com/watch?v=G9wnpfW6lZY) 🟡🎥 - Independent review comparing ADK to other agent SDKs
- 🎥 [ADK Community Calls playlist](https://www.youtube.com/playlist?list=PLwi6PfxEP7zZbBPmWiZ8QbPcuKyAY5RR3) 🟡🎥 - Official monthly ADK community calls: release news, demos and Q&A (latest: [July 2026 – ADK Go 2.0, Agents CLI GA, Managed Agents](https://www.youtube.com/watch?v=-L8ys-nKCWc))
- 🎥 [Agent Factory: Agent Evaluation, Practical Tooling, and Multi-Agent Systems](https://cloud.google.com/blog/topics/developers-practitioners/agent-factory-recap-a-deep-dive-into-agent-evaluation-practical-tooling-and-multi-agent-systems) 🟡🎥 - Google Cloud episode recap on four-layer agent evaluation, golden test cases and the Trace tab in `adk web`, with the [full episode](https://youtu.be/vTjlLiFgFno)
- 🎥 [Google ADK Course (theailanguage playlist)](https://www.youtube.com/playlist?list=PL6tW9BrhiPTAZts0W5nQS9dbW6VMnLKab) 🟢🎥 - Community video course ("End-to-end Course 2026") covering ADK fundamentals and advanced topics

---

## 🎯 Official Examples

_Google ADK recipes repository (formerly adk-samples) - educational and demonstration purposes only_

> **⚠️ Important:** These are official Google examples for learning and demonstration purposes only. They are not intended for production use without significant modification. See the [ADK recipes repository](https://github.com/google/adk-recipes). Deep Search is listed under [Templates & Starters](#-templates--starters).

- 🧪 [ADK Python contributing samples](https://github.com/google/adk-python/tree/main/contributing/samples) 📚 - Small feature-focused samples inside the ADK repo, grouped by topic (workflows, A2A, plugins, evaluation, live, MCP, memory and more)

### 🧱 Core Recipes

- 💸 [Ambient Expense Agent](https://github.com/google/adk-recipes/tree/main/core/python/ambient-expense-agent) 🟡📚 - Ambient agent processing expense reports via Pub/Sub through an ADK 2.0 graph workflow, auto-approving low-value items and routing high-value ones through LLM risk review and human approval
- 🛍️ [GenMedia for Commerce](https://github.com/google/adk-recipes/tree/main/core/python/genmedia-for-commerce) 🔴📚 - Studio agent and Gemini workflows for retail media: photo and video virtual try-on, 360° product spins, and judge-model quality checks, usable as a web app or inside Gemini Enterprise
- 🛡️ [Safety Guardrail Plugins](https://github.com/google/adk-recipes/tree/main/core/python/safety-plugins) 🟡📚 - Security filters using Gemini-as-judge and Model Armor plugins for jailbreak protection
- 🧠 [Cross-Session Memory](https://github.com/google/adk-recipes/tree/main/core/python/cross-session-memory) 🟡📚 - ADK agent with Vertex AI Memory Bank that remembers user preferences and facts across sessions, deployable to Agent Runtime or Cloud Run
- 🔑 [OAuth User Consent Flow (Drive Reader)](https://github.com/google/adk-recipes/tree/main/core/python/oauth-user-consent-flow) 🔴📚 - ADK agent on Agent Runtime using OAuth 2.0 to read Google Drive files on behalf of authenticated users, locally via ADK Web UI and in production via Gemini Enterprise
- 🔎 [RAG Agent: Agent Platform Search](https://github.com/google/adk-recipes/tree/main/core/python/rag-agent-search) 🟡📚 - Starter RAG agent grounded on Agent Platform Search (Discovery Engine) with a GCS data connector and Terraform setup
- 🧩 [RAG Agent: Vector Search](https://github.com/google/adk-recipes/tree/main/core/python/rag-vector-search) 🟡📚 - Starter RAG agent grounded on Vector Search 2.0 with a Kubeflow Pipelines ingestion pipeline that loads, chunks, and imports documents
- 🎙️ [ADK Voice Agent](https://github.com/google/adk-recipes/tree/main/core/python/adk-voice-agent) 🔴📚 - Gemini Live voice agent that stays responsive while coding agents work in the background on a per-user cloud computer, with approval gates and Google Workspace and GitHub access
- 📡 [Ambient Quality Agent (AQuA)](https://github.com/google/adk-recipes/tree/main/core/python/ambient-quality-agent) 🔴📚 - ADK agent that runs beside a production agent, evaluates its conversations in BigQuery, and tracks recurring defects as insights
- 🔭 [Long Horizon Harness](https://github.com/google/adk-recipes/tree/main/core/python/long-horizon-harness) 🔴📚 - Reference agent harness with cross-session memory, per-user sandbox, tool guardrails, sub-agents, and a self-improvement loop

### 🏢 Contributed & Vertical Agents

- 🔍 [LLM Auditor](https://github.com/google/adk-recipes/tree/main/contrib/python/llm-auditor) 🟢📚 - Chatbot response verification and content auditing with Google Search integration
- 💰 [Financial Advisor](https://github.com/google/adk-recipes/tree/main/contrib/python/financial-advisor) 🟡📚 - Multi-agent stock analysis that proposes trading strategies, an execution plan, and a risk assessment using Google Search
- 🎯 [Brand Search Optimization](https://github.com/google/adk-recipes/tree/main/contrib/python/brand-search-optimization) 🟡📚 - Multi-agent workflow that mines BigQuery catalog keywords and uses Gemini Computer Use to study competitor listings, then recommends scored, search-optimized product titles
- 📑 [Brand-Aligned Presentations](https://github.com/google/adk-recipes/tree/main/contrib/python/brand-aligned-presentations) 🔴📚 - Multi-agent system on Vertex AI that generates presentations aligned to brand guidelines, with a pause-and-review step before slide generation
- 🏦 [Small Business Loan Agent](https://github.com/google/adk-recipes/tree/main/contrib/python/small-business-loan-agent) 🔴📚 - Multi-agent loan processing with sequential orchestration, human-in-the-loop approval, LLM-as-Judge validation, and Firestore-backed repair & resume
- 📄 [High-Volume Document Analyzer](https://github.com/google/adk-recipes/tree/main/contrib/python/high-volume-document-analyzer) 🔴📚 - Reads, summarizes, and answers questions over massive collections of unstructured documents in a chunked, iterative manner with Vertex AI and Gemini
- 🧩 [Multi-format Hybrid RAG](https://github.com/google/adk-recipes/tree/main/contrib/python/multiformat-hybrid-rag) 🟡📚 - Production RAG on GCP with contextual chunking, Vector Search 2.0 hybrid search, a REST API, and an MCP server from a single Cloud Run service
- 🎨 [On-Brand GenMedia Agent](https://github.com/google/adk-recipes/tree/main/contrib/python/on-brand-genmedia) 🟡📚 - Generates and evaluates images against brand guidelines, iteratively improving them until policy and quality requirements are met
- 🎓 [Agent Skills Tutorial](https://github.com/google/adk-recipes/tree/main/contrib/python/agent-skills-tutorial) 🟢📚 - Demonstrates four ADK skill patterns: inline, file-based, external, and meta (marked inactive upstream)
- 🛒 [Retail Product Search](https://github.com/google/adk-recipes/tree/main/contrib/python/retail-product-search) 🟡📚 - Semantic product search agent using Vector Search 2.0 and BigQuery, deployable to Agent Runtime, Gemini Enterprise, or Cloud Run
- 👗 [Retail Virtual Try-On](https://github.com/google/adk-recipes/tree/main/contrib/python/retail-virtual-tryon) 🟡📚 - Virtual try-on agent producing still images with Gemini image models and 8-second catwalk videos with Veo
- 🪟 [Staged UI Widgets](https://github.com/google/adk-recipes/tree/main/contrib/python/staged-ui-widgets) 🟡📚 - Shopping agent that renders A2UI widgets (product cards, comparison tables, timelines, charts) by staging payloads in session state and emitting them in one after-agent callback

### 🌐 Other Language Recipes

_Official ADK recipes in Go, Java, Kotlin, and TypeScript_

**Go**

- 💰 [Financial Advisor (Go)](https://github.com/google/adk-recipes/tree/main/contrib/go/financial-advisor) 🟡📚 - Go port of the multi-agent financial advisor: Google Search ticker analysis, trading strategies, execution plan, and risk assessment

**Java**

- 💰 [Financial Advisor (Java)](https://github.com/google/adk-recipes/tree/main/contrib/java/financial-advisor) 🟡📚 - Java port of the multi-agent financial advisor
- 📈 [Time Series Forecasting (Java)](https://github.com/google/adk-recipes/tree/main/contrib/java/time-series-forecasting) 🔴📚 - ADK Java agent using MCP Toolbox and BigQuery `AI.FORECAST` for natural language time series forecasting (marked inactive upstream)

**Kotlin**

- 💰 [Financial Advisor (Kotlin)](https://github.com/google/adk-recipes/tree/main/contrib/kotlin/financial-advisor) 🟡📚 - Kotlin port of the multi-agent financial advisor
- 🔍 [LLM Auditor (Kotlin)](https://github.com/google/adk-recipes/tree/main/contrib/kotlin/llm-auditor) 🟡📚 - Sequential critic and reviser pipeline that fact-checks LLM answers with Google Search

**TypeScript**

- 💰 [Financial Advisor (TypeScript)](https://github.com/google/adk-recipes/tree/main/contrib/typescript/financial-advisor) 🟡📚 - TypeScript port of the multi-agent financial advisor

### 🔌 Agent Skill Plugins

- 🛍️ [Retail AI Plugin](https://github.com/google/adk-recipes/tree/main/plugins/retail) 🟡📚 - Installable retail skills for coding agents: semantic product search over Vector Search 2.0 and BigQuery, plus image and video virtual try-on

---

## 🚀 Getting Started

### Quick Start with Google ADK

Follow the official [Python quickstart](https://adk.dev/get-started/python/) (other languages: [Get Started](https://adk.dev/get-started/)).

```bash
# Python 3.11+ (google-adk 2.x requires it)
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# Install ADK
pip install google-adk

# Create your first agent (the name must be a valid Python identifier: use my_agent, not my-agent)
adk create my_agent

# Run it in the terminal
adk run my_agent

# Or open the dev web UI. Run this from the PARENT folder that contains my_agent/
adk web --port 8000
```

### Using This Repository

This is a **hybrid awesome list** - combining curated resources with featured implementations:

- **Browse & Learn**: Explore categorized projects for inspiration and best practices
- **Clone & Build**: Featured projects in `/my-adk-agents/` are working ADK agents you can clone and run
- **Contribute**: Add your own projects or improve existing ones via [CONTRIBUTING.md](./CONTRIBUTING.md)

### Essential ADK Commands

```bash
adk create my_agent      # Scaffold a new agent project
adk run my_agent         # Interactive CLI
adk web                  # Dev web UI (run from the folder that contains your agent folders)
adk api_server           # Serve agents as a FastAPI API server
adk eval                 # Evaluate an agent against eval sets
adk deploy cloud_run --project=PROJECT --region=REGION path/to/my_agent      # Cloud Run
adk deploy agent_engine --project=PROJECT --region=REGION path/to/my_agent   # Agent Runtime (subcommand keeps the old agent_engine name)
adk deploy gke --project=PROJECT --region=REGION path/to/my_agent            # GKE (also: adk deploy docker)
```

### Resources

- 📖 [Official ADK Documentation](https://adk.dev/)
- 🚀 [Python Quickstart](https://adk.dev/get-started/python/)
- 🆕 [ADK 2.0 Migration Notes](https://adk.dev/2.0/)
- 🛠️ [Third-Party Tools for ADK](https://adk.dev/tools/third-party/) - Official catalog of integrated third-party tools, and the [integrations catalog](https://adk.dev/integrations/)
- 💬 [Community Discussions](https://github.com/google/adk-python/discussions) and [ADK community page](https://adk.dev/community/)
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

**Related Lists:**

- [tsubasakong/awesome-google-adk](https://github.com/tsubasakong/awesome-google-adk) - Another community-curated list of Google ADK resources (last updated May 2025)

## ⭐ Impact

This repository is trusted by a growing community of developers building production AI agents. Help us grow:

- ⭐ **Star** if this helps your development
- 🔗 **Share** with your network
- 🤝 **Contribute** your expertise

## 💚 Sponsors

- [MeterCall](https://metercall.ai/?v=a&src=github) — One metered API gateway. 21M+ endpoints (payments, SMS, AI, CRMs, gov data). Free tier; pay per call.

---

<div align="center">
<strong>Building the future of AI agents, one contribution at a time.</strong><br>
<em>Powered by Google ADK • Curated by the community</em>
</div>
