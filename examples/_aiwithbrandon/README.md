# AI with Brandon - Agent Development Kit (ADK) Examples

Welcome to the AI with Brandon collection of Google Agent Development Kit (ADK) examples! This folder contains a comprehensive set of tutorials, examples, and practical implementations to help you learn and master the Google ADK framework.

## 🎥 Recommended Learning Resource

**HIGHLY RECOMMENDED**: Before diving into these examples, we strongly recommend watching this excellent ADK crash course video by Brandon Hancock:

[![ADK Crash Course](https://img.youtube.com/vi/P4VFL9nIaIA/maxresdefault.jpg)](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s)

**[🎬 ADK Crash Course - Complete Tutorial](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s)**

This video provides one of the best explanations and practical implementations of Google's Agent Development Kit. It covers everything from basic concepts to advanced multi-agent systems, making it an essential resource for both beginners and experienced developers.

## 📁 Folder Contents

### 1. **_adk-crash-course/**

A progressive learning path with 12 hands-on examples that build from basic to advanced ADK concepts:

- **1-basic-agent/** - Your first simple ADK agent
- **2-tool-agent/** - Adding custom tools and capabilities
- **3-litellm-agent/** - Working with different LLM providers
- **4-structured-outputs/** - Controlling agent output formats
- **5-sessions-and-state/** - Implementing memory and context
- **6-persistent-storage/** - Saving information across sessions
- **7-multi-agent/** - Creating systems with multiple agents
- **8-stateful-multi-agent/** - Building complex agent interactions
- **9-callbacks/** - Adding hooks for monitoring and control
- **10-sequential-agent/** - Implementing step-by-step workflows
- **11-parallel-agent/** - Running multiple agents concurrently
- **12-loop-agent/** - Creating agents with iterative processing

### 2. **adk-mcp-tutorial/**

Learn how to integrate Model Context Protocol (MCP) servers with ADK agents:

- Database interaction through MCP servers
- Local SQLite database management
- Remote MCP server connections
- Tool exposure and agent communication

### 3. **adk-rag-agent/**

Build a Retrieval Augmented Generation (RAG) system using Vertex AI:

- Document corpus management
- Natural language querying
- Google Cloud Vertex AI integration
- Advanced RAG implementations

### 4. **adk-voice-agent/**

Create voice-enabled agents with calendar integration:

- Speech-to-text and text-to-speech capabilities
- Google Calendar API integration
- Voice command processing
- Real-time conversation handling

### 5. **youtube-thumbnail-agent/**

AI-powered YouTube thumbnail generator:

- Style cloning from popular channels
- OpenAI image generation integration
- Automated design workflows
- Professional thumbnail creation

## 🚀 Getting Started

### Prerequisites

- **Python 3.9+** (Python 3.11+ recommended)
- **Google Cloud Account** (for Vertex AI and other Google services)
- **API Keys** for various services (OpenAI, Google, etc.)
- **Basic Python knowledge**

### Quick Setup

1. **Clone or navigate to this folder**

   ```bash
   cd examples/_aiwithbrandon
   ```

2. **Choose your learning path**
   - **Beginners**: Start with `_adk-crash-course/1-basic-agent/`
   - **Intermediate**: Try `adk-mcp-tutorial/` or `adk-rag-agent/`
   - **Advanced**: Explore `adk-voice-agent/` or `youtube-thumbnail-agent/`

3. **Create a virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # macOS/Linux
   ```

4. **Follow the specific README in each project folder**

## 📚 Beginner's Guide

### Step 1: Watch the Video Tutorial

Start with the [ADK Crash Course video](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s) to understand the core concepts and see live implementations.

### Step 2: Set Up Your Environment

1. **Install Google ADK**

   ```bash
   pip install google-adk
   ```

2. **Get your Google API Key**
   - Visit [Google AI Studio](https://aistudio.google.com/)
   - Create an API key for Gemini
   - Set it as an environment variable: `GOOGLE_API_KEY=your_key_here`

3. **Set up Google Cloud (for advanced examples)**
   - Create a Google Cloud project
   - Enable Vertex AI API
   - Set up authentication

### Step 3: Start Learning

Begin with the crash course examples in order:

1. **Basic Agent** - Learn agent fundamentals
2. **Tool Agent** - Add custom capabilities
3. **LiteLLM Agent** - Work with multiple LLM providers
4. Continue through the numbered examples...

### Step 4: Build Your Own Project

Once you've completed the crash course, try building:

- A personal assistant agent
- A domain-specific chatbot
- A multi-agent workflow for your use case

## 🛠️ Common Setup Requirements

Most examples require these dependencies:

```bash
pip install google-adk
pip install python-dotenv
pip install pydantic
```

Additional requirements vary by project - check each folder's `requirements.txt`.

## 🔧 Environment Variables

Create a `.env` file in each project directory with:

```env
GOOGLE_API_KEY=your_google_api_key_here
OPENAI_API_KEY=your_openai_key_here  # (if needed)
GOOGLE_CLOUD_PROJECT=your_project_id  # (for Vertex AI examples)
```

## 🤝 Contributing

These examples are based on the excellent work and tutorials by Brandon Hancock. For questions, improvements, or additional examples, please refer to the original source.

## 📖 Additional Resources

- **[Google ADK Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder)**
- **[Agent Development Kit GitHub](https://github.com/google/agent-development-kit)**
- **[Brandon Hancock's GitHub](https://github.com/bhancockio)** - Original creator of these tutorials
- **[Google AI Studio](https://aistudio.google.com/)** - Get your API keys
- **[Vertex AI Console](https://console.cloud.google.com/vertex-ai)** - Manage your Google Cloud AI resources

## 🙏 Credits

Special thanks to **[Brandon Hancock](https://github.com/bhancockio)** for creating these comprehensive ADK examples and tutorials. His work has made learning Google's Agent Development Kit accessible and practical for developers at all levels.

The video tutorial linked above is an outstanding resource that demonstrates real-world ADK implementations and best practices.

## 📄 License

Please refer to the individual project licenses and respect the original creator's licensing terms.

---

**Ready to build intelligent agents?** Start with the [video tutorial](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s) and then dive into the crash course examples!
