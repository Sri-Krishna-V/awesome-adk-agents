# Academic Research Assistant 🎓

AI-powered literature review assistant that finds, analyzes, and synthesizes academic papers relevant to your research. Built with Google's Agent Development Kit (ADK).

## ✨ Key Features

### 🔍 Intelligent Research Profile Analysis

- **Profile Extraction** from Google Scholar, ORCID, and other academic platforms
- **Research Identity Recognition** with key concepts and methodologies
- **Semantic Understanding** of your academic specialization
- **Automatic Keyword Generation** for optimized search queries

### 📚 Advanced Academic Search

- **Multi-Database Search** across Google Scholar, arXiv, PubMed, and more
- **Intelligent Query Construction** based on your research profile
- **Recent Publications Filter** for cutting-edge research
- **Adaptive Search Refinement** based on initial results

### 🧠 Research Synthesis & Analysis

- **Thematic Connection** identification between papers and your work
- **Methodological Innovation** spotting for research advancement
- **Supporting & Contradictory Evidence** analysis for comprehensive understanding
- **Quality-Assured Reports** with multi-step critique and refinement

### 📊 Insightful Reporting

- **Annotated Bibliography** with personalized relevance notes
- **Connection Categorization** across themes, methods, and evidence
- **Research Gap Identification** for potential new directions
- **Actionable Insights** tailored to your academic profile

## How It Works

The Academic Research Assistant follows a multi-agent workflow to deliver personalized research insights:

```
Root Agent
   │
   ├─► Profiler Agent (Analyzes researcher profile)
   │       │
   │       ▼
   ├─► Searcher Agent (Finds relevant papers)
   │       │
   │       ▼
   └─► Comparison Root Agent (Analyzes papers)
           │
           ├─► Analysis Generator (Creates detailed analysis)
           │
           └─► Analysis Critic (Reviews and refines analysis)
```

## 🚀 Quick Start Guide

### Prerequisites

- Python 3.9 or newer
- Google ADK installed (`pip install google-adk`)
- Internet connection for academic database access
- Public academic profile (optional but recommended)

### 1. Setup Project

```bash
# Navigate to the academic research assistant directory
cd my-adk-agents/academic-research-assistant

# Install required packages
pip install requests beautifulsoup4 selenium python-dotenv
```

### 2. Setup Gemini API Key

1. Create or use an existing [Google AI Studio](https://aistudio.google.com/) account
2. Get your Gemini API key from the [API Keys section](https://aistudio.google.com/app/apikeys)
3. Create a `.env` file in the project root:

```bash
GOOGLE_API_KEY=your_gemini_api_key_here
MODEL=gemini-2.0-flash
DISABLE_WEB_DRIVER=0
```

### 3. Start the Agent

```bash
# From the academic-research-assistant directory
adk run academic_research_assistant

# Or use the web interface
adk web
```

### 4. Start Researching 🔍

When the agent starts, it will ask for:
1. Your research topic of interest
2. A URL to your public academic profile (Google Scholar, ORCID, etc.)

Example conversation:
> **"I'm researching reinforcement learning for robotics. Here's my profile: https://scholar.google.com/citations?user=..."**

## 💬 Example Interactions

### 🎯 Machine Learning Researcher

```text
You: "I'm researching reinforcement learning for robotics. Here's my profile: 
      https://scholar.google.com/citations?user=..."

Agent: "Analyzing your profile... I've identified keywords: reinforcement learning, 
        robotics, policy gradient methods, multi-agent systems.
        
        Searching for relevant papers... Found 5 recent publications."

[Agent provides annotated bibliography with detailed relevance notes]

Paper 1: "Sample-Efficient Reinforcement Learning for Robot Manipulation Tasks"
Relevance Note: This paper presents a methodological innovation by combining 
contrastive learning with policy gradient methods - directly building on your
work with TRPO algorithms. Their approach achieves 75% faster convergence and
could address the sample efficiency challenges mentioned in your 2022 paper.
```

### 🧬 Biomedical Scientist

```text
You: "I'm interested in CRISPR gene editing techniques. Here's my ORCID: 
      https://orcid.org/..."

Agent: "Based on your profile, I see you focus on CRISPR-Cas9 off-target effects 
        and delivery mechanisms. Searching for relevant papers..."

[Agent provides detailed analysis of new methodologies and contradictory findings]

Paper 3: "Novel delivery vectors for CRISPR-Cas9 with reduced immunogenicity"
Relevance Note: This presents supporting evidence for your hypothesis on 
lipid nanoparticle delivery systems, confirming your findings on reduced
immune response while extending the work to new tissue types not covered
in your research.
```

## ⚙️ Advanced Configuration

### 🔍 Search Engine Customization

Edit `.env` file to customize search behavior:

```bash
# Enable/disable web driver for interactive searches
DISABLE_WEB_DRIVER=0  # 0=enabled, 1=disabled

# Change model for different capabilities
MODEL=gemini-2.0-pro  # For more sophisticated analysis
```

### 📊 Analysis Customization

You can modify the prompts in `academic_research_assistant/sub_agents/comparison_root_agent/prompt.py` to customize analysis focus:

```python
# Customize analysis categories
- **Thematic Overlap**: "This paper addresses the same theme of 'X' seen in your work on 'Y'."
- **Methodological Innovation**: "This is relevant because it uses a novel 'Z' methodology that could be applied to your research."
- **Supporting Evidence**: "Its findings on 'A' provide strong support for your previous conclusions about 'B'."
- **Contradictory Evidence**: "This paper's results challenge your work on 'C' by showing 'D', suggesting a new direction for investigation."
```

## 📁 Project Structure

- `academic_research_assistant/` — Main agent code directory
  - `agent.py` — Root agent definition
  - `prompts.py` — Root agent prompts
  - `sub_agents/` — Specialized sub-agents
    - `profiler_agent/` — Profile analysis agent
    - `searcher_agent/` — Web search agent
    - `comparison_root_agent/` — Analysis orchestration agent
  - `tools/` — Utility functions for web scraping and processing
  - `shared_libraries/` — Constants and shared utilities

## Troubleshooting

**Profile Scraping Issues**: Ensure your profile URL is public and correctly formatted
**Web Search Errors**: Check if `DISABLE_WEB_DRIVER=0` and selenium is properly installed
**API Quota**: Monitor your Gemini API usage in Google Cloud Console
**Browser Driver**: Update to the latest Chrome version if encountering web driver issues

## Support

- [ADK Documentation](https://google.github.io/adk-docs/)
- [Report Issues](https://github.com/awesome-adk-agents/issues)

---

**Accelerate your literature review! Start your research journey now with the Academic Research Assistant.**

## ⚠️ Disclaimer

All recommendations, analyses, and outputs generated by this project are for research and informational purposes only. They do not constitute comprehensive literature reviews or guarantee academic accuracy. Users should verify all information and exercise their own academic judgment before incorporating these outputs into their research work. 