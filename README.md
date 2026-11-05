<div align="center">
  <h1>
    Awesome ADK Agents
    <a href="https://awesome.re">
      <img src="https://awesome.re/badge.svg" alt="Awesome">
    </a>
  </h1>
</div>

<p align="center"><a href="https://adk.dev/"><img src="https://adk.dev/assets/agent-development-kit.png" width="200px" alt="Agent Development Kit"></a></p>

> Google's Agent Development Kit (ADK) is an open-source, code-first framework for building, evaluating and deploying AI agents in Python, TypeScript, Go, Java and Kotlin.

ADK 2.x is current: graph-based Workflows replace `SequentialAgent`, `ParallelAgent` and `LoopAgent` ([migration notes](https://adk.dev/2.0/)).

New to ADK? [Install](#start-install) · [Learn the basics](#start-learn) · [Start from a template](#start-template) · [Browse official recipes](#start-recipes)

## Contents

- [🧰 Official SDKs & Tools](#-official-sdks--tools)
- [🍳 Official Recipes](#-official-recipes)
- [🚀 Templates & Starters](#-templates--starters)
- [🌟 Community Projects](#-community-projects)
- [📚 Learning Resources](#-learning-resources)
- [🏆 ADK Hackathons & Challenges](#-adk-hackathons--challenges)
- [💡 About ADK](#-about-adk)
- [🏁 Getting Started](#-getting-started)

**Legend:** 🟢 Beginner · 🟡 Intermediate · 🔴 Advanced · 🏭 Production-ready (ships deployment code and docs)

## 🧰 Official SDKs & Tools

_Google's official ADK repositories and the protocol ADK builds on_

- [google/adk-python](https://github.com/google/adk-python) - The core open-source Python ADK: graph workflows, skills, plugins, evaluation and A2A.
- [google/adk-go](https://github.com/google/adk-go) - ADK for Go with graph workflows, human-in-the-loop and A2A (module `google.golang.org/adk/v2`).
- [google/adk-java](https://github.com/google/adk-java) - ADK for Java with plugins, event compaction, tool confirmation and A2A.
- [google/adk-js](https://github.com/google/adk-js) - ADK for TypeScript and JavaScript (npm `@google/adk`) with graph workflows.
- [google/adk-kotlin](https://github.com/google/adk-kotlin) - ADK for Kotlin and Android.
- [google/adk-web](https://github.com/google/adk-web) - The developer UI behind `adk web`: chat, traces, evaluation and the visual builder.
- [google/adk-docs](https://github.com/google/adk-docs) - Source of the official documentation at adk.dev.
- [google/adk-recipes](https://github.com/google/adk-recipes) - Official runnable recipes: core patterns, contributed agents in five languages, and vertical skill plugins (formerly adk-samples).
- [google/agents-cli](https://github.com/google/agents-cli) - CLI and skills that let a coding agent scaffold, evaluate, deploy and observe ADK agents on Google Cloud; successor to Agent Starter Pack.
- [google/adk-python-community](https://github.com/google/adk-python-community) - Community-contributed ADK tools, service integrations and deployment scripts (`pip install google-adk-community`).
- [a2aproject/A2A](https://github.com/a2aproject/A2A) - The Agent2Agent open protocol (v1.0) for interoperable agents, supported natively by ADK.

## 🍳 Official Recipes

<a name="start-recipes"></a>

In this section: [Core Recipes](#core-recipes) · [Contributed & Vertical Agents](#contributed--vertical-agents) · [Other Language Recipes](#other-language-recipes) · [Agent Skill Plugins](#agent-skill-plugins)

_Google ADK recipes repository (formerly adk-samples) - educational and demonstration purposes only_

> **⚠️ Important:** These are official Google examples for learning and demonstration purposes only. They are not intended for production use without significant modification. They all live in `google/adk-recipes` (see Official SDKs & Tools).

- 🟡 [ADK Python contributing samples](https://github.com/google/adk-python/tree/main/contributing/samples) - Small feature-focused samples inside the ADK repo, grouped by topic (workflows, A2A, plugins, evaluation, live, MCP, memory and more).

### Core Recipes

- 🔴 [Deep Search ADK Quickstart](https://github.com/google/adk-recipes/tree/main/core/python/deep-search) 🏭 - Official fullstack research agent (formerly Gemini Fullstack) with a React frontend, human-in-the-loop plan approval, autonomous research pipelines, and Cloud Run deployment.
- 🟡 [Ambient Expense Agent](https://github.com/google/adk-recipes/tree/main/core/python/ambient-expense-agent) - Ambient agent processing expense reports via Pub/Sub through an ADK 2.0 graph workflow, auto-approving low-value items and routing high-value ones through LLM risk review and human approval.
- 🔴 [GenMedia for Commerce](https://github.com/google/adk-recipes/tree/main/core/python/genmedia-for-commerce) - Studio agent and Gemini workflows for retail media: photo and video virtual try-on, 360° product spins, and judge-model quality checks, usable as a web app or inside Gemini Enterprise.
- 🟡 [Safety Guardrail Plugins](https://github.com/google/adk-recipes/tree/main/core/python/safety-plugins) - Security filters using Gemini-as-judge and Model Armor plugins for jailbreak protection.
- 🟡 [Cross-Session Memory](https://github.com/google/adk-recipes/tree/main/core/python/cross-session-memory) - ADK agent with Vertex AI Memory Bank that remembers user preferences and facts across sessions, deployable to Agent Runtime or Cloud Run.
- 🔴 [OAuth User Consent Flow (Drive Reader)](https://github.com/google/adk-recipes/tree/main/core/python/oauth-user-consent-flow) - ADK agent on Agent Runtime using OAuth 2.0 to read Google Drive files on behalf of authenticated users, locally via ADK Web UI and in production via Gemini Enterprise.
- 🟡 [RAG Agent: Agent Platform Search](https://github.com/google/adk-recipes/tree/main/core/python/rag-agent-search) - Starter RAG agent grounded on Agent Platform Search (Discovery Engine) with a GCS data connector and Terraform setup.
- 🟡 [RAG Agent: Vector Search](https://github.com/google/adk-recipes/tree/main/core/python/rag-vector-search) - Starter RAG agent grounded on Vector Search 2.0 with a Kubeflow Pipelines ingestion pipeline that loads, chunks, and imports documents.
- 🔴 [ADK Voice Agent](https://github.com/google/adk-recipes/tree/main/core/python/adk-voice-agent) - Gemini Live voice agent that stays responsive while coding agents work in the background on a per-user cloud computer, with approval gates and Google Workspace and GitHub access.
- 🔴 [Ambient Quality Agent (AQuA)](https://github.com/google/adk-recipes/tree/main/core/python/ambient-quality-agent) - ADK agent that runs beside a production agent, evaluates its conversations in BigQuery, and tracks recurring defects as insights.
- 🔴 [Long Horizon Harness](https://github.com/google/adk-recipes/tree/main/core/python/long-horizon-harness) - Reference agent harness with cross-session memory, per-user sandbox, tool guardrails, sub-agents, and a self-improvement loop.

### Contributed & Vertical Agents

- 🟢 [LLM Auditor](https://github.com/google/adk-recipes/tree/main/contrib/python/llm-auditor) - Chatbot response verification and content auditing with Google Search integration.
- 🟡 [Financial Advisor](https://github.com/google/adk-recipes/tree/main/contrib/python/financial-advisor) - Multi-agent stock analysis that proposes trading strategies, an execution plan, and a risk assessment using Google Search.
- 🟡 [Brand Search Optimization](https://github.com/google/adk-recipes/tree/main/contrib/python/brand-search-optimization) - Multi-agent workflow that mines BigQuery catalog keywords and uses Gemini Computer Use to study competitor listings, then recommends scored, search-optimized product titles.
- 🔴 [Brand-Aligned Presentations](https://github.com/google/adk-recipes/tree/main/contrib/python/brand-aligned-presentations) - Multi-agent system on Vertex AI that generates presentations aligned to brand guidelines, with a pause-and-review step before slide generation.
- 🔴 [Small Business Loan Agent](https://github.com/google/adk-recipes/tree/main/contrib/python/small-business-loan-agent) - Multi-agent loan processing with sequential orchestration, human-in-the-loop approval, LLM-as-Judge validation, and Firestore-backed repair & resume.
- 🔴 [High-Volume Document Analyzer](https://github.com/google/adk-recipes/tree/main/contrib/python/high-volume-document-analyzer) - Reads, summarizes, and answers questions over massive collections of unstructured documents in a chunked, iterative manner with Vertex AI and Gemini.
- 🟡 [Multi-format Hybrid RAG](https://github.com/google/adk-recipes/tree/main/contrib/python/multiformat-hybrid-rag) - Production RAG on GCP with contextual chunking, Vector Search 2.0 hybrid search, a REST API, and an MCP server from a single Cloud Run service.
- 🟡 [On-Brand GenMedia Agent](https://github.com/google/adk-recipes/tree/main/contrib/python/on-brand-genmedia) - Generates and evaluates images against brand guidelines, iteratively improving them until policy and quality requirements are met.
- 🟢 [Agent Skills Tutorial](https://github.com/google/adk-recipes/tree/main/contrib/python/agent-skills-tutorial) - Demonstrates four ADK skill patterns: inline, file-based, external, and meta (marked inactive upstream).
- 🟡 [Retail Product Search](https://github.com/google/adk-recipes/tree/main/contrib/python/retail-product-search) - Semantic product search agent using Vector Search 2.0 and BigQuery, deployable to Agent Runtime, Gemini Enterprise, or Cloud Run.
- 🟡 [Retail Virtual Try-On](https://github.com/google/adk-recipes/tree/main/contrib/python/retail-virtual-tryon) - Virtual try-on agent producing still images with Gemini image models and 8-second catwalk videos with Veo.
- 🟡 [Staged UI Widgets](https://github.com/google/adk-recipes/tree/main/contrib/python/staged-ui-widgets) - Shopping agent that renders A2UI widgets (product cards, comparison tables, timelines, charts) by staging payloads in session state and emitting them in one after-agent callback.

### Other Language Recipes

Official ADK recipes in Go, Java, Kotlin and TypeScript.

**Go**

- 🟡 [Financial Advisor (Go)](https://github.com/google/adk-recipes/tree/main/contrib/go/financial-advisor) - Go port of the multi-agent financial advisor: Google Search ticker analysis, trading strategies, execution plan, and risk assessment.

**Java**

- 🟡 [Financial Advisor (Java)](https://github.com/google/adk-recipes/tree/main/contrib/java/financial-advisor) - Java port of the multi-agent financial advisor.
- 🔴 [Time Series Forecasting (Java)](https://github.com/google/adk-recipes/tree/main/contrib/java/time-series-forecasting) - ADK Java agent using MCP Toolbox and BigQuery `AI.FORECAST` for natural language time series forecasting (marked inactive upstream).

**Kotlin**

- 🟡 [Financial Advisor (Kotlin)](https://github.com/google/adk-recipes/tree/main/contrib/kotlin/financial-advisor) - Kotlin port of the multi-agent financial advisor.
- 🟡 [LLM Auditor (Kotlin)](https://github.com/google/adk-recipes/tree/main/contrib/kotlin/llm-auditor) - Sequential critic and reviser pipeline that fact-checks LLM answers with Google Search.

**TypeScript**

- 🟡 [Financial Advisor (TypeScript)](https://github.com/google/adk-recipes/tree/main/contrib/typescript/financial-advisor) - TypeScript port of the multi-agent financial advisor.

### Agent Skill Plugins

- 🟡 [Retail AI Plugin](https://github.com/google/adk-recipes/tree/main/plugins/retail) - Installable retail skills for coding agents: semantic product search over Vector Search 2.0 and BigQuery, plus image and video virtual try-on.

## 🚀 Templates & Starters

<a name="start-template"></a>

_Ready-to-use templates to kickstart your ADK projects_

> Agent Starter Pack is archived. For Google's official scaffolding, use `google/agents-cli` (see Official SDKs & Tools).

- 🟢 [kkdai/linebot-adk](https://github.com/kkdai/linebot-adk) 🏭 - LINE Bot template with Docker, Cloud Run deployment, and security configurations.
- 🟡 [danishi/slack-bot-adk-python-cloudrun](https://github.com/danishi/slack-bot-adk-python-cloudrun) 🏭 - Slack Bolt bot backend powered by ADK and deployed on Cloud Run.
- 🟢 [glaforge/adk-java-maven-template](https://github.com/glaforge/adk-java-maven-template) - Maven project template for a first ADK for Java agent.
- 🟡 [neo4j-labs/create-context-graph](https://github.com/neo4j-labs/create-context-graph) - Neo4j Labs scaffolding CLI that generates domain-specific context-graph agent apps; `--framework google-adk` generates an ADK agent backend.

## 🌟 Community Projects

In this section: [Maintainer's Agents](#maintainers-agents) · [Multi-Agent Systems](#multi-agent-systems) · [Frameworks & Platforms Built on ADK](#frameworks--platforms-built-on-adk) · [UI, Protocols & Runtimes](#ui-protocols--runtimes) · [Observability, Evaluation & Security](#observability-evaluation--security) · [Memory, Session & Storage](#memory-session--storage) · [Domain-Specific Applications](#domain-specific-applications)

_Projects that people outside Google publish and that use ADK_

### Maintainer's Agents

_Agents built by the maintainer of this list._

- 🟡 [Job Interview Agent](./my-adk-agents/job-interview-agent/) 🏭 - HR interview assistant with calendar integration and real-time feedback.
- 🟡 [Education Path Advisor for India](./my-adk-agents/education-path-advisor/) - Multi-agent career advisor for Indian students and parents: personalized pathways, stepwise plans, risk analysis, and region- and reservation-aware guidance.
- 🟡 [Academic Research Assistant](./my-adk-agents/academic-research-assistant/) - Multi-agent literature review assistant with profile analysis, paper search with a SerpAPI fallback, and personalized research synthesis.
- 🟡 [Project Manager Agent](./my-adk-agents/project-manager-agent/) - Automated project management with task tracking and progress monitoring.
- 🟡 [Learning Content System (WIP)](./my-adk-agents/learning-content-system%28WIP%29/) - Multi-agent system that turns source material into lessons with visuals, audio and slides, using Sequential, Parallel and Loop agents, MCP tools and a quality-check loop.
- 🟢 [Local Code Assistant (WIP)](./my-adk-agents/data-analyst/) - Single agent that runs a local model (Ollama `qwen3:8b` via LiteLLM) and suggests React, Vue, Next.js and Node.js code.

### Multi-Agent Systems

- 🟡 [derailed-dash/rickbot-adk](https://github.com/derailed-dash/rickbot-adk) 🏭 - Multi-personality chatbot with FastAPI backend, Next.js UI, OAuth, and multi-agent RAG/search architecture.
- 🔴 [kweinmeister/agentic-trading](https://github.com/kweinmeister/agentic-trading) 🏭 - Trading simulation where an AlphaBot trading agent and a RiskGuard risk agent talk over A2A, with Dockerfiles and Cloud Build configs. Informational only.
- 🔴 [vladkol/crm-data-agent](https://github.com/vladkol/crm-data-agent) 🏭 - Multi-agent RAG and NL2SQL over Salesforce data with Cloud Run scripts. Reference only: pinned to ADK 1.3 and old Gemini models (June 2025).
- 🟡 [seehiong/adk-web-multi-agent](https://github.com/seehiong/adk-web-multi-agent) - Multi-agent system with Google ADK and OpenRouter models coordinating specialist agents to query PostgreSQL (via MCP Toolbox) and Data Commons.

### Frameworks & Platforms Built on ADK

- 🔴 [antiv/mate](https://github.com/antiv/mate) 🏭 - Production-ready multi-agent orchestration engine built on Google ADK with database-driven agent config, 50+ LLM providers, MCP protocol, persistent memory, web dashboard, and RBAC.
- 🔴 [apowerb/apowerb](https://github.com/apowerb/apowerb) 🏭 - Open-source platform that builds ADK agents from a web UI or REST API, with LiteLLM models, RAG, Text-to-SQL, MCP tools, quotas, audit, Docker Compose and Helm.
- 🔴 [volcengine/veadk-python](https://github.com/volcengine/veadk-python) 🏭 - Volcengine's agent development kit layered on Google ADK, with Volcengine model, memory, tracing and AgentKit deployment integrations; Go port: [volcengine/veadk-go](https://github.com/volcengine/veadk-go).
- 🔴 [yaalalabs/agent-kernel](https://github.com/yaalalabs/agent-kernel) 🏭 - Runtime that runs Google ADK, LangGraph, CrewAI, OpenAI Agents SDK and others side by side, adding governance, pause/resume, sessions and multi-cloud deployment.
- 🔴 [opensage-agent/opensage-adk](https://github.com/opensage-agent/opensage-adk) - Research kit on ADK where the model creates its own agent topology, synthesizes toolsets and manages structured memory at runtime (paper and docs linked; pinned to ADK 1.x).

### UI, Protocols & Runtimes

- 🟡 [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) - The AG-UI agent-to-frontend protocol; its ADK middleware (Python, JS, TypeScript) streams ADK agents to AG-UI clients.
- 🟡 [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) - Frontend stack for agents and generative UI, with an ADK + Angular starter (`examples/integrations/adk-angular`).
- 🟡 [trendmicro/adk-agui-middleware](https://github.com/trendmicro/adk-agui-middleware) - Python middleware bridging Google ADK agents with the AG-UI protocol via Server-Sent Events for real-time agent interactions in frontend applications.
- 🟡 [neo-fetch/draw-your-agents](https://github.com/neo-fetch/draw-your-agents) - Browser-based visual builder that compiles drag-and-drop agent graphs (or draw.io XML) into runnable ADK 2.0 graph-workflow projects, or LangGraph (AGPL-3.0).
- 🔴 [Atmosphere/atmosphere](https://github.com/Atmosphere/atmosphere) - Portable JVM agent runtime whose `atmosphere-adk` module bridges ADK Java agent streams to WebSocket, SSE and gRPC clients.
- 🔴 [Temporal ADK agent samples](https://github.com/temporalio/samples-python/tree/main/google_adk_agents) - Run ADK agents durably inside Temporal workflows; the integration ships as the `temporalio-google-adk` package.
- 🔴 [lemony-ai/cascadeflow](https://github.com/lemony-ai/cascadeflow) 🏭 - Cascading runtime that optimizes cost, latency, quality, and policy decisions inside the agent loop, with a Google ADK integration and support for 17+ model providers.

### Observability, Evaluation & Security

- 🟡 [Arize-ai/openinference](https://github.com/Arize-ai/openinference) - OpenTelemetry instrumentation for AI apps with ADK support (Python instrumentor and an ADK Java example) for any OTel backend.
- 🟡 [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) - AI observability and evaluation platform with ADK integration guides for Python and Java.
- 🟡 [langfuse/langfuse](https://github.com/langfuse/langfuse) - Open-source LLM observability that traces ADK agents via OpenTelemetry.
- 🟡 [comet-ml/opik](https://github.com/comet-ml/opik) - Debug, evaluate and monitor LLM apps and agents, with a native ADK integration.
- 🟡 [mlflow/mlflow](https://github.com/mlflow/mlflow) - AI engineering platform with ADK tracing and `mlflow.genai.scorers.google_adk` scorers for evaluating ADK agents.
- 🟡 [AgentOps-AI/agentops](https://github.com/AgentOps-AI/agentops) - Agent monitoring and cost tracking with a built-in ADK instrumentor.
- 🟡 [monocle2ai/monocle](https://github.com/monocle2ai/monocle) - OpenTelemetry-based GenAI tracing framework with ADK support and a sample ADK travel agent.
- 🟡 [grafana/agento11y](https://github.com/grafana/agento11y) - Grafana Agent Observability SDK with ADK helpers for Python, TypeScript, Go and Java that map ADK callbacks to generation and tool recordings.
- 🟡 [arklexai/arksim](https://github.com/arklexai/arksim) - Multi-turn simulation testing where LLM-driven synthetic users converse with your agent to find failures before production; includes an ADK example.
- 🟡 [trustabl/agent-reliability-analyzer](https://github.com/trustabl/agent-reliability-analyzer) - Local, deterministic static scanner (340+ rules) that finds and fixes agent reliability failures, with deep Google ADK coverage.
- 🟡 [ThreeMoonsLab/agents-shipgate](https://github.com/ThreeMoonsLab/agents-shipgate) - Deterministic merge gate performing local-first, static Tool-Use Readiness review for MCP, OpenAPI, and SDK tool surfaces, including Google ADK Python and YAML configs (CLI + GitHub Action).
- 🟡 [pipelab-org/pipelock](https://github.com/pipelab-org/pipelock) - Open-source agent firewall for MCP and agent egress (exfiltration, SSRF and prompt-injection scanning, signed action receipts) with a Google ADK guide.
- 🟡 [sondera-ai/sondera-harness-python](https://github.com/sondera-ai/sondera-harness-python) - Deterministic guardrails for agents with native ADK middleware (also LangGraph and Strands).
- 🔴 [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) 🏭 - Microsoft agent governance toolkit with policy enforcement, zero-trust identity, sandboxing and OWASP Agentic Top 10 coverage (7 full, 3 partial), plus an ADK adapter. Successor to the archived `imran-siddique/agent-os`.
- 🔴 [Idun-Group/idun-agent-platform](https://github.com/Idun-Group/idun-agent-platform) 🏭 - Open-source Agent Governance Platform that turns any LangGraph or ADK agent into a production-ready service with AG-UI, OpenTelemetry, MCP, memory, guardrails, SSO, and RBAC.
- 🔴 [RubensZimbres/Agent-to-Agent-Security-Pipeline](https://github.com/RubensZimbres/Agent-to-Agent-Security-Pipeline) - Security-focused multi-agent pipeline using ADK + A2A + MCP: natural-language salary-database queries pass through threat-detection, SQL-execution, and PII-masking agents (requires `google-adk>=1.0,<2.0`).
- 🟡 [ceodaradigu/proofline-agent](https://github.com/ceodaradigu/proofline-agent) 🏭 - Evidence-first Google ADK agent that blocks external action until fresh authoritative evidence passes a deterministic four-state gate and explicit human approval, with Cloud Run deployment and unit tests.
- 🟢 [Vulnify ADK tool-approval example](https://github.com/vulnify/vulnify-examples/tree/main/google-adk) - A `before_tool_callback` that checks each tool call with Vulnify: allow, hold for human review, or block. Runs offline in mock mode without API keys, with pytest tests.
- 🟡 [Cygnux-Labs/Tracekit](https://github.com/Cygnux-Labs/Tracekit) - ADK plugin that sends every tool call to a separate signer to allow, deny or hold for a person, logged in a signed, offline-verifiable hash chain.

### Memory, Session & Storage

- 🟡 [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) - Agent memory that learns; its ADK integration implements `BaseMemoryService` (retain on session end, recall on search) plus explicit tool wrappers.
- 🟡 [Memanto ADK memory service](https://github.com/moorcheh-ai/memanto/tree/main/integrations/google-adk) - Drop-in ADK memory service that extracts typed memories (preferences, facts, decisions) from turns, replacing `InMemoryMemoryService`.
- 🟡 [achetronic/adk-utils-go](https://github.com/achetronic/adk-utils-go) 🏭 - Go utilities for ADK: OpenAI and Anthropic model clients, Redis sessions, PostgreSQL + pgvector long-term memory, filesystem artifacts and a context-window guard plugin.
- 🟡 [edu010101/adk-extra-services](https://github.com/edu010101/adk-extra-services) - Python package with extra ADK session (Redis, MongoDB) and artifact (S3, Azure, Supabase, local) backends. Last updated October 2025: lacks `list_artifact_versions` and `get_artifact_version`.

### Domain-Specific Applications

- 🟡 [dandye/adk_runbooks](https://github.com/dandye/adk_runbooks) - Manager-orchestrated multi-agent security operations system (incident response, threat hunting, detection engineering, alert triage) with a progressive-disclosure skills architecture.
- 🟡 [hastimal/gemini-healthcare-agentic-platform](https://github.com/hastimal/gemini-healthcare-agentic-platform) 🏭 - Agentic healthcare search with a three-agent ADK workflow, MCP, FHIR interoperability, grounding and citations; Streamlit demo, Docker and GKE deployment.
- 🔴 [RubensZimbres/Financial-Multi-Agents-Graph-Databasee](https://github.com/RubensZimbres/Financial-Multi-Agents-Graph-Databasee) 🏭 - Multi-agent financial analytics with Neo4j graph database, SEC filings RAG, and ML stock predictions (requires `google-adk>=1.0,<2.0`).
- 🔴 [ntg2208/production-ai-customer-support](https://github.com/ntg2208/production-ai-customer-support) - Multi-agent customer-support system with Policy Agent, Ticket Agent, and Master orchestrator featuring location intelligence, RAG knowledge base, guardrails, evaluation code, and step-by-step tutorials.
- 🔴 [Mongoose Migration Agent System](https://gist.github.com/codeninja/a6e117a3480de8d32dd9ef01b519cdae) - Multi-agent system for automated Mongoose database migration (v6→v8) with specialized agents and MCP integration.
- 🟡 [AI Trends Analysis Pipeline](https://github.com/Astrodevil/ADK-Agent-Examples/tree/main/analyzer_agent) - Comprehensive AI analysis pipeline using Exa Search, Tavily Search, Firecrawl and Nebius AI.
- 🟡 [Job Finder Agent](https://github.com/Astrodevil/ADK-Agent-Examples/tree/main/jobfinder_agent) - Sequential Agent using Mistral OCR, Linkup API and Nebius AI.
- 🟢 [Email ADK Agent](https://github.com/Astrodevil/ADK-Agent-Examples/tree/main/email_adk_agent) - Email management and automation agent using Resend API.
- 🟡 [serkanh/sre-bot](https://github.com/serkanh/sre-bot) 🏭 - SRE/DevOps bot built on Google ADK for intelligent infrastructure management and incident response.
- 🟡 [sreekarrs/JobSearch-Agent](https://github.com/sreekarrs/JobSearch-Agent) 🏭 - Job search automation built around a LinkedIn scraper, with ADK agents that parse job details and generate tailored CVs and cover letters; Docker and deploy workflow included.
- 🟡 [akajammythakkar/adk_hiring_agent](https://github.com/akajammythakkar/adk_hiring_agent) - AI-powered hiring agent using Google ADK and Gemini to analyze resumes, assess skills, and match candidates via multi-agent collaboration.
- 🟡 [Anubhob435/Ai-Agents-EditorHouse](https://github.com/Anubhob435/Ai-Agents-EditorHouse) - Multi-agent book creation system using Google ADK that plans, writes, edits, illustrates, and compiles complete books from a single topic prompt with MongoDB metadata tracking.
- 🟡 [B4K2/WhatsApp-agent](https://github.com/B4K2/WhatsApp-agent) - Intelligent WhatsApp agent built with MCP + Google ADK for conversational automation.
- 🟡 [Beever-AI/beever-atlas](https://github.com/Beever-AI/beever-atlas) - Conversational wiki knowledge base with Slack/Teams/Discord bots, RAG, and MCP integration built on Google ADK.
- 🟡 [anxuanzi/bua](https://github.com/anxuanzi/bua) - AI-powered browser automation for Go — describe tasks in plain English and let the ADK-powered agent handle the clicks via vision-language models.

## 📚 Learning Resources

In this section: [Community Training Platforms](#community-training-platforms) · [Courses & Certifications](#courses--certifications) · [Quickstart Courses](#quickstart-courses) · [Official Hands-on Learning](#official-hands-on-learning) · [Tutorials & Walkthroughs](#tutorials--walkthroughs) · [Articles & Best Practices](#articles--best-practices) · [Video Content](#video-content)

_Comprehensive guides, tutorials, and educational content_

### Community Training Platforms

- [r/agentdevelopmentkit](https://www.reddit.com/r/agentdevelopmentkit/) - Community subreddit for ADK questions, project showcases and release news.
- [DeepWiki: google/adk-python](https://deepwiki.com/google/adk-python) - AI-generated wiki of the adk-python source code that answers questions about how ADK works.
- 🟡 [mauripsale/doc-adk-training](https://github.com/mauripsale/doc-adk-training) - "ADK: From Zero to Hero": 45-module ADK 2.0 curriculum by GDE and Google Cloud trainer Maurizio Ipsale with labs, quizzes, a solution vault and a Codespaces/Cloud Shell setup ([site](https://mauripsale.github.io/doc-adk-training/)).
- 🟢 [Google ADK Training Hub](https://raphaelmansuy.github.io/adk_training/) - Community-run training site with 35 tutorials covering ADK agents, tools, multi-agent patterns, deployment, and React/Next.js integration. Written for ADK 1.x (1.16+); check the ADK 2.0 migration notes linked at the top of this list before following the code.

### Courses & Certifications

- 🟡 [Building Live Voice Agents with Google's ADK (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/building-live-voice-agents-with-googles-adk/) - Short course by Google engineers: voice agent, sessions, state and memory, tools, callback guardrails, multi-agent orchestration, and a Gemini TTS podcast capstone.
- 🟡 [A2A: The Agent2Agent Protocol (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) - Course with Google Cloud and IBM Research: wrap agents built on ADK and other frameworks in A2A servers and orchestrate them in a healthcare multi-agent system.
- 🟢 [Develop Agents with Agent Development Kit (ADK) track (DataCamp x Google Cloud)](https://www.datacamp.com/tracks/develop-agents-with-agent-development-kit-adk) - Five Google-created courses: build agents, optimize agent behavior, add tools, and manage memory and state.
- 🟢 [Build Your First Agent with Agent Development Kit (Google Skills)](https://www.skills.google/course_templates/1563) - Introductory Google Skills course for building and running an ADK agent in Python and YAML.
- 🟢 [5-Day AI Agents Intensive on Kaggle](https://www.kaggle.com/learn-guide/5-day-agents) - Free, self-paced guide from Google and Kaggle's November 2025 course: whitepapers, podcasts, livestreams and ADK codelabs on agent foundations, tools, memory, evaluation and production.

### Quickstart Courses

- 🟡 [bhancockio/agent2agent](https://github.com/bhancockio/agent2agent) - Brandon Hancock's crash course on agent-to-agent (A2A) communication with ADK with [YouTube](https://www.youtube.com/watch?v=mFkw3p5qSuA&t=172s) tutorial.
- 🟢 [chongdashu/adk-made-simple](https://github.com/chongdashu/adk-made-simple) - From basics to A2A integration with real world applications and projects.
- 🟡 [arjunprabhulal/google-adk-masterclass](https://github.com/arjunprabhulal/google-adk-masterclass) - 20-module masterclass covering ADK basics through advanced topics including MCP, Vertex AI, and production deployment.
- 🟡 [omerbsezer/Fast-LLM-Agent-MCP](https://github.com/omerbsezer/Fast-LLM-Agent-MCP) - Comprehensive resource covering LLMs, RAG, fine-tuning, agents, MCP, and Google ADK both theoretically and practically with reference documents.

### Official Hands-on Learning

<a name="start-learn"></a>

- 🟢 [Google ADK Codelabs](https://codelabs.developers.google.com/?text=ADK) - Interactive, guided tutorials with hands-on coding exercises from Google.
- 🟡 [ADK 2 Orchestration: Graph, Collaborative & Dynamic Workflows](https://codelabs.developers.google.com/adk2/instructions) - About 50-minute Colab codelab teaching ADK 2.0 graph, collaborative (chat, single-turn, task) and dynamic workflows by building a race-day coach, one runnable step at a time.
- 🟢 [Build Your First ADK Agent Workforce](https://cloud.google.com/blog/topics/developers-practitioners/build-your-first-adk-agent-workforce) - Learning path with 3 official codelabs: building autonomous agents, empowering agents with tools, and orchestrating multi-agent systems.
- 🟡 [Building ADK Agents with Skills and Tools (Next '26 Developer Keynote)](https://codelabs.developers.google.com/next26/dev-keynote/building-agents-with-skills) - Codelab building a marathon-planner agent with a modular prompt, `SkillToolset` and Google Maps MCP tools, tested in `adk web` and deployed to Agent Runtime.
- 🟡 [Building a Multi-Agent System using Gemini and Gemma models](https://codelabs.developers.google.com/next26/multi-agent-system) - Researcher, Judge, Content Builder and Orchestrator agents wired with workflow agents, `RemoteA2aAgent` and a Gemma model on a Cloud Run GPU.
- 🟡 [Stateful Data Science Agent on Agent Runtime](https://codelabs.developers.google.com/next26/adk-deploy-scale) 🏭 - Codelab deploying a BigQuery data-science agent with Memory Bank and Cloud Trace to Agent Runtime with `adk deploy`.
- 🟡 [Frontend Experiences with ADK and A2UI](https://codelabs.developers.google.com/next26/adk-a2ui) - Short codelab where an ADK agent replies with A2UI JSON that `adk web` renders as cards, lists and buttons.
- 🟢 [Build AI Agents with ADK for Java](https://codelabs.developers.google.com/adk-java-getting-started) - Codelab building persona, tool, sub-agent and workflow agents in Java.
- 🔴 [GoogleCloudPlatform/race-condition](https://github.com/GoogleCloudPlatform/race-condition) - Multi-agent marathon simulation (ADK, Gemini, A2A, Go/Python/Angular) from the Google Cloud Next '26 Developer Keynote.
- 🟡 [Building GraphRAG Agents with ADK and Neo4j](https://codelabs.developers.google.com/neo4j-adk-graphrag-agents) - Official codelab building a multi-agent investment research system with Neo4j, MCP Toolbox, and GraphRAG for multi-hop reasoning (uses `google-adk>=1.21.0` and preview Gemini 3.x models).

### Tutorials & Walkthroughs

- 🟡 [chongdashu/adk-mcp-a2a-crash-course](https://github.com/chongdashu/adk-mcp-a2a-crash-course) - Complete multi-agent system with ADK + A2A + MCP integration, featuring Notion and ElevenLabs with full architecture, testing, and [YouTube](https://www.youtube.com/watch?v=s6-Ofu-uu2k) tutorial (pinned to ADK 1.2).
- 🟡 [mongodb-developer/MongoDB-ADK-Agents](https://github.com/mongodb-developer/MongoDB-ADK-Agents) - Official MongoDB grocery shopping agent with Atlas Vector Search, updated for ADK 2.x, with a complete dataset and step-by-step setup ([companion article](https://medium.com/google-cloud/build-a-python-ai-agent-in-15-minutes-with-google-adk-and-mongodb-atlas-vector-search-groceries-b6c4af017629)).
- 🟡 [kweinmeister/agent-design-patterns](https://github.com/kweinmeister/agent-design-patterns) - Executable cookbook of agent architecture patterns using ADK and Gemini, with a published guide.
- 🟡 [Datascale agent docs tutorial](https://github.com/datascalehq/datascale/tree/main/cookbook/tutorials/agent_docs) - Multi-agent documentation builder with planner and writer agents that analyze codebases and generate structured knowledge bases ([companion article](https://medium.com/gitconnected/building-a-knowledge-base-from-your-codebase-using-google-adk-7508e845bdc1)).
- 🟢 [meteatamel/adk-demos](https://github.com/meteatamel/adk-demos/) - Collection of demos and tutorials for Google's Agent Development Kit.
- 🟡 [sokart/adk-walkthrough](https://github.com/sokart/adk-walkthrough) - Step-by-step guides and examples using the open-source Python ADK framework.
- 🟡 [bhancockio/adk-mcp-tutorial](https://github.com/bhancockio/adk-mcp-tutorial) - Model Context Protocol (both local and remote) with ADK with [YouTube](https://www.youtube.com/watch?v=HkzOrj2qeXI&t=2362s) tutorial.
- 🟡 [thomas-chong/google-adk-visual-agent-builder-demo](https://github.com/thomas-chong/google-adk-visual-agent-builder-demo) - Complete demo of Google ADK Visual Agent Builder with a multi-agent research system walkthrough.
- 🟡 [lavinigam-gcp/build-with-adk](https://github.com/lavinigam-gcp/build-with-adk) 🏭 - Design patterns and production-ready architectures for building multi-agent AI systems with Google ADK on Cloud Run, Vertex AI, and AI Studio.
- 🟡 [Give a Google ADK agent per-user OAuth tools with Scalekit](https://docs.scalekit.com/agentkit/examples/google-adk/) - Scalekit guide to a Gmail-reading ADK agent with per-user OAuth tools, from native ADK tools or a Scalekit MCP server through `McpToolset`. Sample code: [scalekit-inc/google-adk-agent-example](https://github.com/scalekit-inc/google-adk-agent-example).

<details>
<summary><b>Google ADK crash course and apps from awesome-llm-apps</b> · 21 lessons and 9 apps</summary>

Tutorial examples from [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) that demonstrate ADK patterns and capabilities.

**Fundamentals:**

- 🟢 [Starter Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/1_starter_agent) - Your first ADK agent: basic agent creation, the ADK workflow, and simple text processing.
- 🟢 [Model-Agnostic Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/2_model_agnostic_agent) - Running ADK with non-Gemini models, with OpenAI and Anthropic Claude integration sub-examples.
- 🟢 [Memory Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/5_memory_agent) - Memory and session management with in-memory conversation handling and persistent SQLite storage.
- 🟢 [Simple Multi-Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/8_simple_multi_agent) - Multi-agent orchestration via a researcher pipeline of specialized agents in a sequential workflow.
- 🟢 [ADK YAML Examples](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/adk_yaml_examples) - Config-driven agent definitions using ADK's YAML format.

**Structured Output Agents:**

- 🟢 [Customer Support Ticket Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/3_structured_output_agent/3_1_customer_support_ticket_agent) - Generates structured support tickets with Pydantic schemas.
- 🟢 [Email Generator Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/3_structured_output_agent/3_2_email_agent) - Creates formatted emails with structured output.

**Tool-Using Agents:**

- 🟢 [Code Execution Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/4_tool_using_agent/4_1_builtin_tools/code_exec_agent) - Built-in code execution tools.
- 🟢 [Google Search Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/4_tool_using_agent/4_1_builtin_tools/search_agent) - Web search capabilities.
- 🟢 [Function Tools](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/4_tool_using_agent/4_2_function_tools) - Custom Python functions as agent tools, with calculator and utility agent examples.
- 🟢 [Filesystem Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/4_tool_using_agent/4_4_mcp_tools/filesystem_agent) - MCP filesystem tools integration.
- 🟢 [Firecrawl Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/4_tool_using_agent/4_4_mcp_tools/firecrawl_agent) - Web scraping, site crawling and structured extraction through the Firecrawl MCP server.
- 🟢 [LangChain Integration Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/4_tool_using_agent/4_3_thirdparty_tools/langchain_agent) - Third-party tool integration with LangChain.
- 🟢 [CrewAI Integration Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/4_tool_using_agent/4_3_thirdparty_tools/crewai_agent) - Third-party tool integration with CrewAI.

**Callback Agents:**

- 🟢 [Agent Lifecycle Callbacks](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/6_callbacks/6_1_agent_lifecycle_callbacks) - Monitoring agent execution lifecycle.
- 🟢 [LLM Interaction Callbacks](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/6_callbacks/6_2_llm_interaction_callbacks) - Tracking LLM calls and responses.
- 🟢 [Tool Execution Callbacks](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/6_callbacks/6_3_tool_execution_callbacks) - Monitoring tool usage and execution.

**Plugin Agents:**

- 🟢 [Plugin-based Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/7_plugins) - Extensible plugin architecture for modular agent design.

**Multi-Agent Systems:**

- 🟢 [Sequential Multi-Agent Pattern](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/9_multi_agent_patterns/9_1_sequential_agent) - Step-by-step multi-agent coordination (uses `SequentialAgent`, deprecated in ADK 2.x in favor of `Workflow`; still runs).
- 🟢 [Loop Multi-Agent Pattern](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/9_multi_agent_patterns/9_2_loop_agent) - Iterative multi-agent workflows (uses `LoopAgent`, deprecated in ADK 2.x in favor of `Workflow`; still runs).
- 🟢 [Parallel Multi-Agent Pattern](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/ai_agent_framework_crash_course/google_adk_crash_course/9_multi_agent_patterns/9_3_parallel_agent) - Concurrent multi-agent execution (uses `ParallelAgent`, deprecated in ADK 2.x in favor of `Workflow`; still runs).

**Multi-Agent Applications:**

- 🟡 [AI Financial Coach Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/ai_financial_coach_agent) - Financial advisory system with specialized agent teams.
- 🟡 [AI Home Renovation Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/ai_home_renovation_agent) - Home improvement planning with multi-agent coordination.
- 🟡 [AI SEO Audit Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_seo_audit_team) - Website SEO analysis with specialized agent teams.
- 🟡 [Multimodal UI/UX Feedback Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_uiux_feedback_agent_team) - Design review system with multimodal capabilities.
- 🟡 [AI Negotiation Battle Simulator](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/ai_negotiation_battle_simulator) - Buyer, seller, and orchestrator agents simulate negotiations with an AG-UI frontend (ag_ui_adk).
- 🟡 [AI Sales Intelligence Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_sales_intelligence_agent_team) - Sequential research agents that generate competitive battle cards and comparison charts.
- 🟡 [AI VC Due Diligence Agent Team](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/multi_agent_apps/agent_teams/ai_vc_due_diligence_agent_team) - Sequential agents producing HTML reports, infographics, and financial charts for VC due diligence.

**Single-Agent Applications:**

- 🟡 [Earnings Call Analyst Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/earnings_call_analyst_agent) - Ingests and analyzes earnings calls with transcription, research, and analyst agents.
- 🟡 [AI Consultant Agent](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/advanced_ai_agents/single_agent_apps/ai_consultant_agent) - Business consulting agent using Google Search grounding and session management.

</details>

### Articles & Best Practices

**Official Google posts:**

- 🟡 [Announcing ADK for Go 2.0](https://developers.googleblog.com/announcing-adk-go-20) - Clearest official explanation of the ADK 2.0 model: graph-based workflow engine, human-in-the-loop pause/resume, dynamic nodes, retries, and Chat/Task/SingleTurn agent modes.
- 🟡 [Hill-Climbing Agent Quality with Agents CLI Evaluation](https://developers.googleblog.com/hill-climbing-agent-quality-with-agents-cli-evaluation/) - Baseline evals, regression checks, model comparison, nightly runs and automated prompt tuning with Agents CLI.
- 🟡 [Build Cross-Language Multi-Agent Team with ADK and A2A](https://developers.googleblog.com/build-cross-language-multi-agent-team-with-google-agent-development-kit-and-a2a/) - Python extraction agent plus Go compliance validator orchestrated over A2A with a manual-review fallback.
- 🔴 [Build zero-trust AI agents with Google's Agent Development Kit](https://developers.googleblog.com/build-zero-trust-ai-agents-with-googles-agent-development-kit/) - Prompt-injection-resistant agent with signed database writes, gVisor sandboxing and deterministic checks in CI.
- 🟢 [Building Collaborative AI: A Developer's Guide to Multi-Agent Systems with ADK](https://cloud.google.com/blog/topics/developers-practitioners/building-collaborative-ai-a-developers-guide-to-multi-agent-systems-with-adk) - LLM, workflow and custom agents, sub-agents vs AgentTool, and state, with companion videos and a sample repo.
- 🟡 [ADK Architecture: When to Use Sub-Agents versus Agents as Tools](https://cloud.google.com/blog/topics/developers-practitioners/where-to-use-sub-agents-versus-agents-as-tools) - Essential architectural guide with decision matrix for choosing between sub-agents and agent tools, featuring real-world use cases (data agents, travel planners) and best practices for multi-agent systems.

**Community articles:**

- 🔴 [Ralph Loop with Google ADK: AI Agents That Verify, Not Guess](https://medium.com/google-cloud/ralph-loop-with-google-adk-ai-agents-that-verify-not-guess-b41f71c0f30f) - Advanced guide to implementing Ralph Loop pattern for external verification-driven workflows, featuring multi-agent Dockerfile generation with Docker-based validation and iterative refinement until objective success criteria are met ([demo repo](https://github.com/thomas-chong/google-adk-ralph-loop-demo)).
- 🟡 [Choosing the Right Deployment Path for Your Google ADK Agents](https://medium.com/google-cloud/choosing-the-right-deployment-path-for-your-google-adk-agents-86c89c251ab5) - Google Cloud guide comparing deployment strategies (Cloud Run vs Vertex AI vs GKE) for production ADK agents.
- 🟡 [Announcing a Datastore-Backed Session Service for the ADK](https://medium.com/google-cloud/announcing-a-new-datastore-backed-session-service-for-the-adk-d14596ae28df) 🏭 - Google Cloud solution for persistent agent sessions in serverless environments using Cloud Datastore instead of SQLite.
- 🟡 [Drawing Charts in Your AI Agent Frontend with Google ADK](https://medium.com/@dconsonni/drawing-charts-in-your-ai-agent-frontend-with-google-adk-9c74a4a98931) - Guide to agent-generated visualizations using ADK Artifacts with Apache ECharts/vis-network, featuring FastAPI integration and session-scoped artifact management.
- 🟡 [Building Next-Gen AI Agents with Google ADK, MCP, RAG and Ollama](https://medium.com/@tam.tamanna18/building-next-gen-ai-agents-with-google-adk-mcp-rag-and-ollama-ca3c1e5002da) - Comprehensive tutorial on building multi-agent chatbots integrating ADK + MCP + RAG + Ollama with step-by-step code and architecture diagrams.
- 🟡 [Google ADK + LM Studio: The Power Couple of Local Agent Development](https://medium.com/@c-damien/google-adk-lm-studio-the-power-couple-of-local-agent-development-2dd225bae36f) - Complete guide to running ADK agents locally with LM Studio, featuring setup instructions, model configuration, and privacy-focused development without cloud dependencies.
- 🔴 [Optimize Your Google ADK Agent's SOP with GEPA](https://raphaelmansuy.github.io/adk_training/blog/gepa-optimization-tutorial/) - Walkthrough of prompt optimization with GEPA (reflective prompt evolution) on a small 5-scenario demo, with sample code.

### Video Content

- 🟢 [Introducing Agent Development Kit (ADK)](https://www.youtube.com/watch?v=zgrOwow_uTQ) - 3-minute product overview shown at launch.
- 🟢 [Getting started with ADK](https://www.youtube.com/watch?v=44C8u0CDtSo) - "Hello-world" coding session from pip install to first agent.
- 🟡 [Google Launches an Agent SDK – ADK Deep Dive](https://www.youtube.com/watch?v=G9wnpfW6lZY) - Independent review comparing ADK to other agent SDKs.
- 🟡 [ADK Community Calls playlist](https://www.youtube.com/playlist?list=PLwi6PfxEP7zZbBPmWiZ8QbPcuKyAY5RR3) - Official monthly ADK community calls: release news, demos and Q&A (latest: [July 2026 – ADK Go 2.0, Agents CLI GA, Managed Agents](https://www.youtube.com/watch?v=-L8ys-nKCWc)).
- 🟡 [Agent Factory: Agent Evaluation, Practical Tooling, and Multi-Agent Systems](https://cloud.google.com/blog/topics/developers-practitioners/agent-factory-recap-a-deep-dive-into-agent-evaluation-practical-tooling-and-multi-agent-systems) - Google Cloud episode recap on four-layer agent evaluation, golden test cases and the Trace tab in `adk web`, with the [full episode](https://youtu.be/vTjlLiFgFno).
- 🟢 [Google ADK Course (theailanguage playlist)](https://www.youtube.com/playlist?list=PL6tW9BrhiPTAZts0W5nQS9dbW6VMnLKab) - Community video course ("End-to-end Course 2026") covering ADK fundamentals and advanced topics.

## 🏆 ADK Hackathons & Challenges

In this section: [ADK-Focused Hackathons](#adk-focused-hackathons) · [Hackathons Where ADK Was Optional](#hackathons-where-adk-was-optional)

_Winners of hackathons where teams built with ADK. Each list comes from the organizer's own announcement. Where ADK was optional, only winners whose code or project page shows ADK are listed._

### ADK-Focused Hackathons

<details>
<summary><b>Agent Development Kit Hackathon with Google Cloud</b> · Google Cloud, 2025 · 477 submissions · 8 winners</summary>

_The first hackathon built around ADK, with 10,400+ participants from 62 countries. Source: [winners announcement](https://cloud.google.com/blog/products/ai-machine-learning/adk-hackathon-results-winners-and-highlights). Also see [all submissions](https://googlecloudmultiagents.devpost.com/project-gallery)._

- 🥇 **Grand Prize ($15,000)**: [SalesShortcut](https://devpost.com/software/salesshortcut) - AI-powered Sales Development Representative system with a multi-agent architecture for automated lead generation, research, proposal generation, and outreach. ([source](https://github.com/merdandt/SalesShortcut))
- 🌎 **North America ($8,000)**: [Energy Agent AI](https://devpost.com/software/energy-agent-ai) - Multi-agent AI transforming energy customer management through Google ADK orchestration. ([source](https://github.com/hazardscarn/energyagentai))
- 🌍 **Europe, Middle East & Africa ($8,000)**: [Nexora-AI](https://devpost.com/software/teachai-upzofa) - Next-gen personalized education with interactive lessons, visuals, quizzes, and smart AI support. ([source](https://github.com/M4RKUS28/Nexora))
- 🌏 **Asia Pacific ($8,000)**: [GreenOps](https://devpost.com/software/greenops-gzp4aj) - AI team that continuously audits, forecasts, and optimizes cloud infrastructure for sustainability. ([source](https://github.com/niksm7/GreenOps))
- 🌎 **Latin America ($8,000)**: [Edu.AI](https://devpost.com/software/edu-ai-multi-agent-educational-system-for-brazil) - Brazilian education system with agents that evaluate essays, generate personalized study plans, and create interdisciplinary mock exams. ([source](https://github.com/giovannamoeller/edu-ai-adk-version))
- 🎖️ **Honorable Mention ($1,000)**: [Particle Physics Agent](https://devpost.com/software/particle-physics-agent) - Physics AI agent converting natural language into validated Feynman diagrams using real physical laws. ([source](https://github.com/bee4come/Particle-Physics-Agent))
- 🎖️ **Honorable Mention ($1,000)**: [TradeSage AI](https://devpost.com/software/tradesage-ai) - Multi-agent financial analysis platform for evaluating trading hypotheses with ADK, Agent Engine, Cloud Run and Vertex AI. ([source](https://github.com/sudsk/tradesage-mvp))
- 🎖️ **Honorable Mention ($1,000)**: [Bleach](https://devpost.com/software/bleach-7tqdmo) - Visual AI agent builder for Google ADK: describe agents in plain English, design them visually, and test instantly. ([source](https://github.com/vivek100/bleachAgentBuilder))

</details>

<details>
<summary><b>Cloud Run Hackathon</b> · Google Cloud, Oct–Nov 2025 · ADK-only AI Agents category · 3 ADK winners</summary>

_Serverless build contest on Cloud Run with an ADK-only AI Agents category. Source: [winners announcement](https://run.devpost.com/updates/38848-a-big-congrats-to-the-winners)_

- 🥇 **Grand Prize**: [Storytopia](https://devpost.com/software/storytopia-bu917p) - Making screen time less passive - and more creative. ([source](https://github.com/Harpita-P/Storytopia))
- 🎖️ **Honorable Mentions**: [Piatto](https://devpost.com/software/piatto) - Meet Piatto - the AI chef that designs recipes just for you and cooks along, step by step. ([source](https://github.com/M4RKUS28/Piatto))
- 🏆 **Best of AI Agents**: [PermitScan AI](https://devpost.com/software/permitflow-ai) - Automates hazard discovery → permit creation → permit validation → permit refinement for oil & gas Work Orders (WOs). ([source](https://github.com/sagban/permitflowAI))

</details>

<details>
<summary><b>HackUSF 2026</b> · GDG on Campus USF, March 2026 · Google ADK sponsor track · 6 ADK winners</summary>

_Student hackathon with a Google ADK and A2A sponsor track. Source: [winners announcement](https://hackusf-2026.devpost.com/updates/42587-and-the-winner-is)_

- 🏆 **Best Overall 1st**: [A.N.R (Agentic Nuclear Reactor)](https://devpost.com/software/regenerative-agentic-nuclear-reactor) - Can you imagine having a proper AI being able to help streamline efficiencies, not just in everyday, but in complex tasks such as running a fusion reactor? ([source](https://github.com/morallyearlgrey/demo-fusion-reactor))
- 🏆 **Most Innovative Hack**: [Guido](https://devpost.com/software/guido-k7f5ei) - Getting where you need to go should never be the hard part. ([source](https://github.com/kwaiidev/guido))
- 🏆 **Best Design Hack**: [DontCollapse](https://devpost.com/software/dontcollapse) - Uses AI to identify high-risk urban zones by analyzing flood, infrastructure, and social data, delivering fragility scores and clear actions to prevent disaster impact. ([source](https://github.com/narcistiq/DontCollapse))
- 🏆 **Google Cloud: Building a Self-Healing World with Google ADK**: [T.I.T.A.N. - Tampa Intelligent Threat Analysis Network](https://devpost.com/software/t-i-t-a-n-tampa-intelligent-threat-analysis-network) - TITAN is an AI emergency system using parallel agents for floods, roads, and risk. It self-corrects with QA loops and shares real-time updates for faster, equitable disaster response.
- 🏆 **Google Cloud: Building a Self-Healing World with Google ADK**: [Bowser](https://devpost.com/software/bowser-d0nvh4) - Turning rehab into heroic play. ([source](https://github.com/Akhileshreddym/Bowser))
- 🏆 **\[MLH] Best Use of .Tech**: [Crisis-Net](https://devpost.com/software/crisis-net) - Real-time disaster response dashboard that utilizes AI agents to detect threats, record severity, map impact, locate shelter, and send targeted alerts when minutes matter. ([source](https://github.com/hackusf-2026-crisis-net/crisis-net))

</details>

### Hackathons Where ADK Was Optional

<details>
<summary><b>All Things Agentic Hackathon</b> · Google, Aug 2026 · $180K · 13 ADK winners</summary>

_Autonomous agents on Gemini 3.5 and Google Cloud in three tracks; ADK was one of four allowed frameworks, and these winners used it. Source: [winners announcement](https://allthingsagentichackathon.devpost.com/updates/45669-the-moment-you-ve-long-awaited-winners-are-here)_

- 🥇 **Grand Prize**: [Plant Debugger: Agentic Field Partner for Brownfield Ops](https://devpost.com/software/plant-debugger) - For brownfield plants where the last meter has no API, Google ADK leads diagnostic loops while operators provide physical reach and site facts, verified by deterministic plant telemetry.
- 🏆 **The Taskmaster**: [Latch](https://devpost.com/software/latch-d8u6of) - Gemini evolves verified observers on five FPGAs for instruments producing up to 6.5 Tb/s. Blind tests matched three spacecraft; Latch also preserved a Fermi event NASA’s systems missed.
- 🏆 **The Collaborative Partner**: [UpRabbit](https://devpost.com/software/thought-visualized) - Collaborative Knowledge Building with Agents.A learning session with someone asking guiding questions, watching your misconceptions, uncovering unknown unknowns, and visualizing connections.
- 🏆 **The Fortified Enterprise Fleet**: [EIR: Healthcare Agent Fleet](https://devpost.com/software/eir-healthcare-agent-fleet) - EIR is a secure hospital agent fleet that coordinates patient access, recovery, scheduling and supply workflows, with persistent memory, managed guardrails and human approval for critical actions. ([source](https://github.com/ybedoyab/eir))
- 🏆 **Individual/Hobbyist (Best Team/Solo Build)**: [ShipGaurd](https://devpost.com/software/shipgaurd) - From iOS App TestFlight Crash feedback to Xcode validated pull requests.
- 🏆 **Best Architectural Design**: [Leadsy](https://devpost.com/software/leadsy) - We are an autonomous premium content engine for Indian SMBs who can't afford Ad agencies. We take in a single business/shop url and produce a complete content kit in less than 15 mins. ([source](https://github.com/vn-envy/leadsy-flock))
- 🏆 **Best Architectural Design**: [Helixstreet — autonomous genomic fleet](https://devpost.com/software/helixstreet-autonomous-genomic-fleet) - Drop raw DNA in a bucket and walk away: five Gemini+Gemma agents screen PII, call variants with DeepVariant, flag drug-gene risks, and file an auditable digital twin. No chat. No clicks. No human.
- 🏆 **Best Multimodal UX**: [Overturn](https://devpost.com/software/overturn-bu5imz) - Seven agents that appeal wrongful insurance denials on their own: they cite the payer's own policy, verify every citation before a human sees it, and keep escalating for weeks unasked. ([source](https://github.com/Rickygole/overturn))
- 🏆 **Best Multimodal UX**: [AnbuCare](https://devpost.com/software/anbucare) - My mother is 71 and lives in Thoothukudi. I don't. Anbu Care coordinates her care at 3am: triage, insurance, bookings, payments, with the guardrails in code where no prompt can reach them. ([source](https://github.com/4KInc/anbu-care))
- 🎖️ **Honorable Mentions**: [Shoots](https://devpost.com/software/shoots) - You take the photos. Shoots does the learning bookkeeping. ([source](https://github.com/fikri2992/shoots))
- 🎖️ **Honorable Mentions**: [Migration Control Tower](https://devpost.com/software/migration-control-tower) - A governed fleet of AI agents that discovers a legacy data estate, plans its migration to BigQuery, proves every row actually moved, and cuts over only with human approval. ([source](https://github.com/Nikhil0075/MIGRATION-CONTROL-TOWER))
- 🎖️ **Honorable Mentions**: [EduAgent — Collaborative Partner Socratic Mentor](https://devpost.com/software/eduagent-collaborative-partner-socratic-mentor) - EduAgent goes beyond a chatbot: it challenges student reasoning, remembers progress across essays, and autonomously turns those insights into prioritized, teacher-approved actions. ([source](https://github.com/francisnguyenanh/EduAgent))
- 🎖️ **Honorable Mentions**: [Groom](https://devpost.com/software/todogs) - Curating a training set means reviewing hundreds of images by hand. Groom inspects every one with Gemini, files the keepers, and refuses to guess when the answer isn't clear. ([source](https://github.com/hackaprende/groom))

</details>

<details>
<summary><b>Agentic Cinema: The Blockbuster Hackathon</b> · Google, Jul–Sep 2026 · $75K · 12 ADK winners</summary>

_Film-production agents on Gemini and Google Cloud with partner tracks; ADK was one accepted package, and these winners used it. Source: [winners announcement](https://agentic-cinema.devpost.com/updates/45318-and-the-winner-is)_

- 🏆 **IBM - 1st Place**: [Eyeline — Autonomous On-Set Continuity Copilot](https://devpost.com/software/eyeline-autonomous-on-set-continuity-copilot) - Autonomous multimodal continuity copilot for film script supervisors: catches prop, wardrobe, and blocking breaks in the 2-minute on-set window, backed by Gemini 3.8 Flash adjudication and Veo 3.1. ([source](https://github.com/helenkwok/eyeline))
- 🏆 **IBM - 3rd Place**: [HOLD](https://devpost.com/software/hold-wrp4nq) - Watch HOLD reduce paid waiting in a film schedule, inspect modeled child-performer limits with citations, and re-solve after a confirmed change. ([source](https://github.com/StephenSook/hold))
- 🏆 **Grafana Labs - 1st Place**: [The Media Customs](https://devpost.com/software/the-media-customs) - Clears your commercial for markets before it airs. A Google Agent watches it with you, judges it against each country's law, cites the statute, and re-renders the shots that fail. ([source](https://github.com/tdries/devpost-hackathon-agentic-cinema))
- 🏆 **Grafana Labs - 2nd Place**: [Raccord - Accessible Experience Reliability for live media.](https://devpost.com/software/raccord-accessible-experience-reliability-for-live-media) - Raccord certifies, monitors, diagnoses, repairs and proves the accessibility of a live media experience. ([source](https://github.com/Marc-Dvci/Raccord))
- 🏆 **Grafana Labs - 3rd Place**: [Shot Clock](https://devpost.com/software/shot-clock) - A crew of Gemini agents watches a VFX render farm in Grafana, works out which shots miss the delivery date, proves why, looks at the frame, and prices it. ([source](https://github.com/biyonjose10/shot-clock))
- 🏆 **Parallel - 1st Place**: [CurrentCut](https://devpost.com/software/currentcut) - The overnight AI edit desk for factual TV. Hand over the night's rushes; wake up to a first cut whose every factual line names the source it was checked against, or says why it has none. ([source](https://github.com/tanaka-cell/currentcut))
- 🏆 **Parallel - 2nd Place**: [Consentinel](https://devpost.com/software/consentinel) - One registry, two directions hunting unauthorized AI clones of performers worldwide in five languages, clearing studio deliveries before ship. AI finds evidence; humans decide. ([source](https://github.com/PRACHIT27/Consentinel))
- 🏆 **Parallel - 3rd Place**: [The Boxes](https://devpost.com/software/the-boxes) - Stanley Kubrick's boxes in your pocket. ([source](https://github.com/rapha18th/agentic-cinema-boxes))
- 🏆 **Clickhouse - 1st Place**: [THE GATE](https://devpost.com/software/the-gate-yx5z2b) - Drop a day's footage in. It finds what coverage you're missing, works out if there's time to get it, and tells you what each answer costs. ([source](https://github.com/javaonboard/the-gate))
- 🏆 **Clickhouse - 2nd Place**: [Retention Room](https://devpost.com/software/retention-room) - Which scene lost them? Retention Room puts playback telemetry and scripts in one room: a Gemini agent queries ClickHouse, rules out a CDN problem, then tells the editor what to trim.
- 🏆 **Clickhouse - 3rd Place**: [Locaish](https://devpost.com/software/locaish) - The location scout you can send anywhere. ([source](https://github.com/JoshuaA1292/Locaish))
- 🏆 **Replit - 2nd Place**: [FrameKind](https://devpost.com/software/framekind-tz85od) - An accessibility review agent for film editors. Find missing sound captions, rushed dialogue and timing errors, review each proposed repair against the picture, then export a better caption file. ([source](https://github.com/Abhinav0905/Google_All_Agentic_Cinema))

</details>

<details>
<summary><b>AI Agents: Intensive Vibe Coding Capstone</b> · Kaggle & Google, Jun–Jul 2026 · 10 ADK winners</summary>

_Capstone of Google and Kaggle's AI Agents: Intensive Vibe Coding course (6,033 submissions); ADK was one of the course concepts. Source: [winners](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project/hackathon-winners)_

- 🏅 **Agents for Good, Award 2**: [CritiqAI](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project/writeups/new-writeup-1781911352583) - AI debate coach that teaches students not to depend on AI. ([source](https://github.com/francisnguyenanh/CritqAI))
- 🏅 **Agents for Good, Award 3**: [AccessPilot](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project/writeups/accesspilot-autonomous-accessibility-repair-agent) - Turns web accessibility audits into verified repairs, built on ADK 2. ([source](https://github.com/joinarun/accesspilot))
- 🏅 **Agents for Business, Award 1**: [Chance Electro](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project/writeups/chance-electro-draft) - Estimator for electrical contractors: from a sketch to a priced proposal with A2A agents, an MCP pricing server and skills. ([source](https://github.com/barmanoff/chance-electro-capstone))
- 🏅 **Agents for Business, Award 2**: [Trajectory Auditor](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project/writeups/new-writeup-1783355733656) - Multi-agent ADK pipeline that grades how a coding agent reached its result. ([source](https://github.com/ShayIsso/trajectory-auditor))
- 🏅 **Agents for Business, Award 3**: [ReviewOps Agent](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project/writeups/new-writeup-1783340134268) - Drafts fair, cited performance reviews from employee-approved evidence, with access control before the model. ([source](https://github.com/mkiselyow/ReviewOps-Agent))
- 🏅 **Concierge Agents, Award 1**: [BiteBudget](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project/writeups/bitebudget-an-intelligent-cooking-and-grocery-exp) - ADK Workflow state machine for meal plans, shopping lists and receipt logging with Gemini OCR. ([source](https://github.com/crisstugui-png/cooking-shopping-assistant))
- 🏅 **Concierge Agents, Award 2**: [TripWeaver](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project/writeups/tripweaver-a-multi-agent-travel-planner-that-fix) - Multi-agent travel planner with a self-correcting budget and schedule loop. ([source](https://github.com/VenuAIAgenticDev/TripWeaver))
- 🏅 **Concierge Agents, Award 3**: [KinKeeper](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project/writeups/kinkeeper-never-forget-to-remember-the-people-yo) - Memory concierge for birthdays and family moments hidden in chats. ([source](https://github.com/gpshalini/KinKeeper))
- 🏅 **Freestyle, Award 1**: [Palimpsest](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project/writeups/palimpsest) - Multi-agent pipeline for historical manuscript transcription with an ADK agent skill. ([source](https://github.com/carlosapsa/palimpsest))
- 🏅 **Freestyle, Award 2**: [Project A.R.I.E.S.](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project/writeups/project-aries) - Space-weather assistant that fetches NASA data and writes structured reports. ([source](https://github.com/N-Garai/Project-A.R.I.E.S))

</details>

<details>
<summary><b>Google Cloud Rapid Agent Hackathon</b> · Google, May–Jun 2026 · $60K · 16 ADK winners</summary>

_Partner-track agent contest on Gemini 3 and Agent Builder; ADK was not required, but these winners built on it. Source: [winners announcement](https://rapid-agent.devpost.com/updates/43725-and-the-winner-is)_

- 🏆 **Arize - 1st Place**: [Cassandra](https://devpost.com/software/cassandra-jilmgy) - AI agents fail silently, confidently wrong, and nobody notices. Cassandra is an AI that watches your AIs. It catches every lie, diagnoses why, ships a proven fix, and even grades its own accuracy. ([source](https://github.com/SirjanSingh/cassandra))
- 🏆 **Arize - 2nd Place**: [ComplianceOS](https://devpost.com/software/compilanceos) - A compliance agent that audits your code against real law, writes the fixes, and reads its own Phoenix traces through MCP to get better after every scan. ([source](https://github.com/bhupenbandi/compliance-os))
- 🏆 **Elastic - 2nd Place**: [BLUEPRINT: AI Property Due Diligence](https://devpost.com/software/blueprint-ai-property-due-diligence) - Seven AI agents read public records on any US address, permits, flood zones, EPA data, then run an adversarial AI debate before delivering a buyer risk score. Powered by Elastic Agent Builder MCP. ([source](https://github.com/usv240/blueprint))
- 🏆 **Arize - 3rd Place**: [ClinTrace](https://devpost.com/software/clintrace) - AI agent that assists in emergency department triage — severity scoring, red-flag detection, specialist routing — with every reasoning step traced and auditable via Arize Phoenix. ([source](https://github.com/Reuben-Alex/ClinTrace))
- 🏆 **Fivetran - 1st Place**: [Unravel](https://devpost.com/software/unravel-7ak8lf) - Five agents watch evolving variant evidence, re-score a clinic's uncertain DNA findings with a calibrated Bayesian model, and draft family recontact the moment one turns actionable. Draft-only. ([source](https://github.com/faith-ogun/Unravel))
- 🏆 **GitLab - 1st Place**: [mnemosyne](https://devpost.com/software/mnemosyne-ubotlw) - The AI that remembers every failure — predicts outages, annotates risky code inline, gates CI pipelines, auto-blocks critical MRs, and diagnoses failures. Powered by Gemini and GitLab on Google Cloud.
- 🏆 **Fivetran - 2nd Place**: [TruthKeeper](https://devpost.com/software/truthkeeper) - Your stack is lying to itself. TruthKeeper is the agent that listens. ([source](https://github.com/gangix/truthkeeper))
- 🏆 **GitLab - 2nd Place**: [STYLOMETRY](https://devpost.com/software/stylometry) - The forensic guardrail for your GitLab pipeline. ([source](https://github.com/annatchijova/stylometry))
- 🏆 **Fivetran - 3rd Place**: [How Did I?](https://devpost.com/software/how-did-i) - Agentic ecommerce operator that diagnoses daily revenue leaks across carts, ads, inventory, and support—then drafts owner-approved fixes in one tap.
- 🏆 **GitLab - 3rd Place**: [ContribPilot](https://devpost.com/software/contribpilot) - Finding an open source issue is easy. Contributing successfully is hard. ContribPilot bridges that gap with personalized guidance powered by Gemini and GitLab MCP. ([source](https://github.com/NiloySaha84/ContribPilot_Google_Rapid_Agent_Hackathon_Proj))
- 🏆 **MongoDB - 1st Place**: [Epiq](https://devpost.com/software/epiq-1ubx5q) - Intelligent A.I Outbreak Tracker.
- 🏆 **Dynatrace - 1st Place**: [AutoSRE: The Autonomous On-Call Engineer](https://devpost.com/software/autosre-the-autonomous-on-call-engineer) - AutoSRE is an autonomous on-call agent that diagnoses Dynatrace incidents in seconds and queues up the fix, but cannot touch production without your one-tap approval. ([source](https://github.com/thylinao1/autosre))
- 🏆 **MongoDB - 2nd Place**: [KickOff](https://devpost.com/software/trustos) - Seven Gemini 3 agents move 82,500 World Cup fans to MetLife Stadium — reasoning over live MongoDB Atlas via MCP, every decision a database write streamed onto a photorealistic 3D map.
- 🏆 **Dynatrace - 2nd Place**: [Karma — The Reincarnation Agent for Deprecated Services](https://devpost.com/software/karma-the-reincarnation-agent-for-deprecated-services) - A multi-agent system that learns a deprecated service's hidden contracts and haunts its replacement, catching silent regressions every test misses. Gemini + Vertex AI Agent Builder + Dynatrace. ([source](https://github.com/rogerjeasy/karma))
- 🏆 **MongoDB - 3rd Place**: [Sentinel Flood-Watch Agent](https://devpost.com/software/sentinel-flood-watch-agent) - An AI agent that proactively monitors Accra's ecological sites using remote sensing data and advanced analytics, and alerts authorities and stakeholders to potential environmental threats. ([source](https://github.com/Hou-dini/sentinel-flood-watch))
- 🏆 **Dynatrace - 3rd Place**: [Heimdall: Autonomous Incident Response for Dynatrace](https://devpost.com/software/project-hpfwsu51xila) - Autonomous SRE that watches your Dynatrace tenant 24/7, diagnoses production incidents from real spans and Davis CoPilot, and opens a pull request before your phone stops ringing.

</details>

<details>
<summary><b>AI Agent Hackathon with Google Cloud, 4th edition</b> · Google Cloud Japan on Zenn, March 2026 · 1 ADK winner</summary>

_Japanese hackathon where ADK was one accepted option, not required. Only winners shown that use ADK. Source: [winners on Zenn](https://zenn.dev/hackathons/google-cloud-japan-ai-hackathon-vol4?tab=projects)_

- 🏅 **Encouragement Award**: [COCO](https://zenn.dev/takoeno/articles/ae8e042de0fb62) - AI partner that helps find lost items around the room. ([source](https://github.com/h4ckberry/coco-gcaihack4))

</details>

<details>
<summary><b>Gemini Live Agent Challenge</b> · Google, Feb–Mar 2026 · $80K · 9 ADK winners</summary>

_Real-time voice, vision and storytelling agents on Gemini Live; ADK or the GenAI SDK was allowed. Source: [winners announcement](https://cloud.google.com/blog/topics/developers-practitioners/winners-and-highlights-of-the-gemini-live-agent-challenge)_

- 🥇 **Grand Prize**: [ORION - Operating Room Intelligent Orchestration Node](https://devpost.com/software/orion-operating-room-intelligent-orchestration-node) - A voice-directed surgical co-pilot for robotic surgery. Surgeons can speak naturally & instantly receive answers, live data on display, and real-time visual assistance - all without breaking scrub.
- 🏆 **Best of Creative Storytellers**: [Sankofa](https://devpost.com/software/sankofa-y47f9p) - Transforming fragmented family history into living, breathing, multimodal stories. ([source](https://github.com/Jeremiah-Sakuda/Sankofa))
- 🏆 **Best Multimodal Integration & User Experience**: [Wand -- A live agent that sees, browses, and clicks with you](https://devpost.com/software/wand-a-live-agent-that-sees-browses-and-clicks-with-you) - Wand turns the web into something you can talk to and point at. It’s a live AI agent that sees your screen and acts in real time as you speak and point — no typing, no mouse.
- 🏆 **Best Technical Execution & Agent Architecture**: [JohnKeats.AI](https://devpost.com/software/johnkeats-ai) - A voice-first AI companion that holds uncertainty instead of solving it. Built on Gemini 2.5 Flash Native Audio with a governed calibration pipeline that learns from every conversation. ([source](https://github.com/johnkeats-ai/johnkeats-ai))
- 🏆 **Best Innovation & Thought Leadership**: [Rayan Memory](https://devpost.com/software/rayan-memory) - Point your camera at life. Rayan builds a 3D palace from everything you see and hear, rooms you can walk through, memories you can talk to. Your AI that remembers, so you don't have to. ([source](https://github.com/yelnady/rayan))
- 🎖️ **Honorable Mentions**: [Ekaette](https://devpost.com/software/ekaette) - Configurable AI voice and messaging assistant for customer-facing businesses across multiple industries.
- 🎖️ **Honorable Mentions**: [Call My Parts](https://devpost.com/software/call-my-parts) - Sit back and relax while our agent help find the right fit. ([source](https://github.com/Top-Notch-X/C2B-Concierge))
- 🎖️ **Honorable Mentions**: [Relay — Real-Time Voice & Vision Lab Tutor for Electronics](https://devpost.com/software/relay-real-time-voice-vision-lab-tutor-for-electronics) - Relay watches your breadboard through your webcam and talks you through building circuits in real time. It sees wiring, catches errors, generates code, and turns builds into 3D digital twins. ([source](https://github.com/faith-ogun/Relay))
- 🎖️ **Honorable Mentions**: [VibeCat](https://devpost.com/software/vibecat) - Your proactive desktop companion. VibeCat watches your screen via Gemini Live API, suggests actions before you ask, and executes with self-healing navigation. Built with GenAI SDK + ADK on Cloud Run. ([source](https://github.com/Two-Weeks-Team/vibeCat))

</details>

<details>
<summary><b>Agents Intensive Capstone Project</b> · Kaggle & Google, Nov–Dec 2025 · 10 ADK winners</summary>

_Capstone of Google and Kaggle's 5-Day AI Agents Intensive (11,453 submissions); ADK was the course framework but not required. Source: [winners](https://www.kaggle.com/competitions/agents-intensive-capstone-project/hackathon-winners)_

- 🥇 **Agents for Good, 1st**: [Carbon Footprint Optimization Engine (CfoE)](https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/carbon-footprint-optimization-engine-cfoe) - Multi-agent procurement compliance with carbon-footprint analysis and human-in-the-loop review. ([notebook](https://www.kaggle.com/code/sumitkumarguha/global-cfoe))
- 🥉 **Agents for Good, 3rd**: [Parallel Scholar](https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/parallel-scholar) - Research assistant with parallel paper discovery, trend analysis, citation management and persistent memory. ([source](https://github.com/emansarahafi/Research-Assistant-Agent))
- 🥇 **Enterprise Agents, 1st**: [Chaos Playbook Engine](https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/new-writeup-1763223319877) - Reproducible chaos lab that tests and compares agent resilience with RAG playbooks, from tools to MCP/A2A. ([source](https://github.com/alberto-martinez-zurita/chaos-playbook-engine))
- 🥈 **Enterprise Agents, 2nd**: [Coderama](https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/coderama-reimagining-enterprise-software-deliver) - A2A agents that plan, build, test and deploy software. ([source](https://github.com/debasisdwivedy/Coderama))
- 🥉 **Enterprise Agents, 3rd**: [VeganFlow](https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/veganflow-autonomous-supply-chain-intelligence) - Supply-chain intelligence for plant-based retail micro-vendors. ([source](https://github.com/karthick-sothivelr/Autonomous_Supply_Chain_Intelligence))
- 🥇 **Concierge Agents, 1st**: [NewsPulse AI Agent](https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/NewsPulse-AI-Agent) - Self-correcting multi-agent news digest tailored to executives. ([source](https://github.com/azhang6-nlp/NewsPulse_AI_Agent))
- 🥈 **Concierge Agents, 2nd**: [FIL Content Agent System](https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/fil-content-agent-system) - Agents that draft website content from natural-language requests. ([source](https://github.com/jasononaquest/fil-agent))
- 🥇 **Freestyle, 1st**: [Daedalus](https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/daedalus) - Self-expanding agent system that designs, tests and registers its own tools and agent pipelines. ([source](https://github.com/jovanovic-milos/daedalus))
- 🥈 **Freestyle, 2nd**: [AI Stock Prediction System](https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/ai-stock-prediction-system-multi-agent-a2a-archit) - Six parallel agents with an A2A architecture for stock analysis. ([source](https://github.com/nishapp/agents-5days-kaggle-competition))
- 🥉 **Freestyle, 3rd**: [StoryLand AI](https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/storyland-agent) - Turns favorite books into themed travel itineraries. ([source](https://github.com/o-ostrovskiy/storyland-ai))

</details>

<details>
<summary><b>AI Agent Hackathon with Google Cloud, 2nd edition</b> · Google Cloud Japan on Zenn, August 2025 · 2 ADK winners</summary>

_Japanese hackathon where ADK was one accepted option, not required. Only winners shown that use ADK. Source: [winners on Zenn](https://zenn.dev/hackathons/google-cloud-japan-ai-hackathon-vol2?tab=projects)_

- 🥈 **2nd Place**: [学校だよりAI](https://zenn.dev/gakkoudayoriai/articles/d7c61ec828913d) - Two-agent Google ADK system for school newsletters.
- 🏅 **Moonshot Award**: [KnockAI](https://zenn.dev/enostech/articles/8a4a3f2589afd7) - ADK agent that passes on craftsmen's tacit estimating knowledge, deployed on Cloud Run.

</details>

<details>
<summary><b>GKE Turns 10 Hackathon</b> · Google Cloud, Aug–Sep 2025 · $50K · 7 ADK winners</summary>

_Add agentic AI to Bank of Anthos or Online Boutique on GKE; ADK was recommended, and these winners used it. Source: [winners announcement](https://cloud.google.com/blog/topics/developers-practitioners/winners-and-highlights-from-gke-hackathon)_

- 🥇 **Grand Prize**: [The Cart-to-Kitchen AI Assistant on GKE](https://devpost.com/software/cart-to-kitchen-gke-ai-assistant) - An AI assistant to spice up your online grocery shopping experience!
- 🎖️ **Honorable Mentions**: [Vigil AI](https://devpost.com/software/vigil-ai) - Securing financial microservices with autonomous, real-time fraud mitigation. ([source](https://github.com/ayanliger/gke-turns10-hackathon-vigil))
- 🎖️ **Honorable Mentions**: [Voice Teller - Dial ADK + MCP](https://devpost.com/software/voice-teller-dial-adk-mcp) - Changing how we call. Intelligent phone bots instead of clunky IVR. ([source](https://github.com/julian-hecker/gke-hackathon))
- 🎖️ **Honorable Mentions**: [CO2‑Aware Shopping Assistant](https://devpost.com/software/co2-aware-shopping-assistant) - Get what you want for less CO2. We optimize products and shipping to lower emissions and cost while meeting your delivery. ([source](https://github.com/prabhakaran-jm/co2-shopping-assistant))
- 🏆 **Regional Prize: North America**: [CardOS](https://devpost.com/software/cardos) - Applying for a credit card is painful & most rewards don’t fit individual needs. We’re solving this with AI agents that analyze transaction history, tailor terms & perks, & balance bank profitability.
- 🏆 **Regional Prize: Europe, Middle East, Africa**: [Cartmate](https://devpost.com/software/cartmate-mygdtk) - An Ai-powered shopping experience. ([source](https://github.com/victorbash400/Cartmate))
- 🏆 **Regional Prize: Asia Pacific**: [V-Commerce Studio](https://devpost.com/software/v-commerce-studio) - Redefines e-commerce with AI personalized chat, proactive engagement, virtual try-ons, and instant ad generation, built on Google’s ecosystem for intelligent retail automation. ([source](https://github.com/mvp-ing/v-commerce-studio))

</details>

## 💡 About ADK

<details>
<summary>What ADK is, its key features, and what's new in ADK 2.x</summary>

**What ADK is**

- Google's open-source, code-first framework for building, evaluating and deploying AI agents, launched in 2025.
- Optimized for Gemini but model-agnostic: Gemini, Gemma, Claude, OpenAI, Ollama, vLLM, LiteLLM and more.
- Deployment-agnostic: any container, Cloud Run, GKE, or Agent Runtime on Google Cloud.
- Built for deployment from day one, with evaluation, tracing and managed hosting options.
- Integrates deeply with Agent Platform (formerly Vertex AI), Cloud Run, GKE, BigQuery and the wider Google AI ecosystem.
- Third-party integrations include MongoDB, MCP and the A2A protocol, and the project ships frequent releases.
- Official SDKs exist for Python, TypeScript, Go, Java and Kotlin. ADK 2.0 reached general availability for Python on 2026-05-19, and the current Python release is v2.13.0.

**Key features**

- Graph-based workflows (ADK 2.0): deterministic execution with routing, fan-out/fan-in, loops, retries, state, human-in-the-loop and nested workflows.
- Rich tool ecosystem: pre-built tools, custom functions, OpenAPI specs, MCP tools and Google ecosystem integration.
- Code-first development: agents are defined in code (Python, TypeScript, Go, Java, Kotlin) with full testability and version control.
- Multi-agent orchestration: specialized agents compose into scalable hierarchies and delegate with the Task API.
- Deploy anywhere: Agent Runtime, Cloud Run, GKE, or any containerized environment.

**What's new in ADK 2.x**

- Workflow runtime: graph-based execution with routing, fan-out/fan-in, loops, retries, human-in-the-loop and nested workflows. `Workflow` replaces the now-deprecated `SequentialAgent`, `ParallelAgent` and `LoopAgent` (see the migration notes linked at the top of this list).
- Five official SDKs: Python 2.0 (May 2026), Go 2.0 (June 2026), TypeScript 2.0 (August 2026), Java 1.0 (March 2026) and Kotlin 1.0 (September 2026).
- Skills, plugins and evaluation: `SkillToolset`, a plugin system, a user simulator, and `adk optimize` for prompt optimization.
- A2A: agents can expose or consume other agents over the Agent2Agent protocol, which reached v1.0 in March 2026.
- Renames: the docs moved to adk.dev; Vertex AI Agent Engine is now Agent Runtime on Gemini Enterprise Agent Platform; `google/adk-samples` is now `google/adk-recipes`; Agent Starter Pack is archived in favor of `google/agents-cli`.

</details>

## 🏁 Getting Started

<a name="start-install"></a>

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

This is a **hybrid awesome list**: curated resources plus the maintainer's own agents. Browse the sections for projects and patterns, clone the working ADK agents in `/my-adk-agents/` to run them, and see Contributing below to add your own projects or improve existing ones.

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

- [Official ADK Documentation](https://adk.dev/)
- [Third-Party Tools for ADK](https://adk.dev/tools/third-party/) - Official catalog of integrated third-party tools, and the [integrations catalog](https://adk.dev/integrations/).
- [ADK Python Discussions](https://github.com/google/adk-python/discussions) - GitHub Discussions on the adk-python repository for questions and ideas.
- [ADK community page](https://adk.dev/community/) - Official page listing community groups, calls, courses and contributed resources.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](./CONTRIBUTING.md) for the entry format and the rules an entry must meet.

Questions and ideas go to [Discussions](https://github.com/Sri-Krishna-V/awesome-adk-agents/discussions). Report broken links and other problems as an [issue](https://github.com/Sri-Krishna-V/awesome-adk-agents/issues).

## Footnotes

Entries were last re-checked against ADK 2.x in November 2026.

Related lists:

- [tsubasakong/awesome-google-adk](https://github.com/tsubasakong/awesome-google-adk) - Another community-curated list of Google ADK resources (last updated May 2025).

Credits: the Google ADK team for the framework, Brandon Hancock for educational content and tutorials, and community contributors for projects and improvements.
