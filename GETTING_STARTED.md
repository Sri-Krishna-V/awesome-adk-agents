# 🚀 Getting Started with Awesome ADK Agents

This guide will help you get started with the agents in this repository quickly and efficiently.

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.11+** installed ([Download Python](https://python.org/downloads/))
- **Git** for cloning repositories ([Download Git](https://git-scm.com/))
- **Basic understanding** of AI agents and the Google ADK framework

## 🎯 Choose Your Path

### 👋 New to ADK?
Start with these beginner-friendly agents:

1. **[Basic Agent](./examples/_aiwithbrandon/_adk-crash-course/1-basic-agent/)** - Learn ADK fundamentals
2. **[Tool Integration Agent](./examples/_aiwithbrandon/_adk-crash-course/2-tool-agent/)** - Integrate external tools
3. **[RAG Agent](./examples/_aiwithbrandon/adk-rag-agent/)** - Build a knowledge retrieval system

### 🔥 Ready for Advanced Projects?
Try these production-ready agents:

1. **[Agentic Trading Simulator](./examples/agentic-trading/)** - Multi-agent trading system with risk management
2. **[Academic Research Agent](./examples/google_agent_garden/academic-research/)** - Comprehensive research assistant
3. **[Data Science Agent](./examples/google_agent_garden/data-science/)** - Automated data analysis workflows

### 🛠️ Want to Build Something Specific?
Browse by domain:

- **📊 Business & Productivity**: Project Manager, Customer Service, Financial Advisor
- **🔬 Research & Analysis**: Academic Research, Data Science, Time Series Forecasting
- **🛍️ E-commerce & Marketing**: Personalized Shopping, Marketing Agency, Travel Concierge
- **🧠 AI & Development**: RAG Systems, LLM Auditor, Software Bug Assistant

## 🏃‍♂️ Quick Start Steps

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/awesome-adk-agents.git
cd awesome-adk-agents
```

### 2. Choose an Agent

Navigate to the agent directory you want to try:

```bash
# Example: Try the Agentic Trading Simulator
cd examples/agentic-trading

# Example: Try a basic agent  
cd examples/_aiwithbrandon/_adk-crash-course/1-basic-agent

# Example: Try the Academic Research Agent
cd examples/google_agent_garden/academic-research
```

### 3. Follow Agent-Specific Setup

Each agent has its own `README.md` with specific setup instructions. Generally:

**For Windows users:**
```powershell
# Many agents include automated setup scripts
.\setup.ps1  # If available

# Or manual setup:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**For Linux/Mac users:**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Run the Agent

Most agents can be started with:

```bash
# Using ADK CLI
adk web

# Or custom scripts
./start.sh          # Linux/Mac
.\start.ps1         # Windows

# Or direct Python execution
python main.py
```

## 📚 Learning Resources

### Official Documentation
- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [ADK Python GitHub](https://github.com/google/adk-python)
- [A2A Protocol](https://github.com/google/A2A)

### Community Resources
- [Reddit: r/agentdevelopmentkit](https://www.reddit.com/r/agentdevelopmentkit/)
- [ADK GitHub Discussions](https://github.com/google/adk-python/discussions)

## 🔧 Common Commands

Once you're in an agent directory:

```bash
# Start agent with web UI (most common)
adk web

# Start agent with API only
adk api_server

# Run agent in CLI mode
adk run

# Create a new agent
adk create my-new-agent

# Run tests (if available)
pytest tests/
```

## 💡 Tips for Success

1. **Read the README**: Each agent has unique setup requirements
2. **Check Dependencies**: Install agent-specific requirements before running
3. **Environment Variables**: Many agents require API keys (OpenAI, Google, etc.)
4. **Virtual Environments**: Always use virtual environments to avoid conflicts
5. **Port Conflicts**: If ports are in use, check for other running services
6. **Windows Users**: Use PowerShell instead of Command Prompt for better compatibility

## 🆘 Getting Help

### Common Issues
- **Import Errors**: Ensure virtual environment is activated and dependencies installed
- **Port Conflicts**: Check if other services are using the same ports (8000, 8080, etc.)
- **API Key Errors**: Verify environment variables are set correctly
- **Permission Errors**: On Windows, run PowerShell as administrator if needed

### Where to Get Support
- Check the agent's specific `README.md` and documentation
- Look for `TROUBLESHOOTING.md` files in agent directories
- Search [GitHub Issues](https://github.com/your-username/awesome-adk-agents/issues)
- Ask questions in [GitHub Discussions](https://github.com/your-username/awesome-adk-agents/discussions)

## 🎉 What's Next?

After successfully running your first agent:

1. **Experiment**: Modify parameters and see how behavior changes
2. **Explore**: Try different agents to understand various use cases
3. **Learn**: Study the code to understand ADK patterns and best practices
4. **Build**: Create your own agent using the patterns you've learned
5. **Contribute**: Share your improvements or new agents with the community

Happy agent building! 🤖✨
