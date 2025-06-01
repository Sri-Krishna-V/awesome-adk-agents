# 📚 Vertex AI RAG Agent with ADK

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4.svg)](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder)
[![Vertex AI](https://img.shields.io/badge/Vertex-AI-4285F4.svg)](https://cloud.google.com/vertex-ai)

> **🎥 Learn More**: Check out the [ADK Crash Course](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s) by Brandon Hancock for comprehensive ADK learning!

This project demonstrates a Google Agent Development Kit (ADK) implementation of a Retrieval Augmented Generation (RAG) agent using Google Cloud Vertex AI. Build intelligent agents that can interact with document collections and provide accurate, context-aware responses.

## 🌟 What You'll Learn

- **RAG Implementation**: Build production-ready RAG systems with Vertex AI
- **Document Management**: Create and manage document corpora programmatically
- **Natural Language Queries**: Query documents using conversational AI
- **Google Cloud Integration**: Leverage enterprise-grade AI infrastructure

## ✨ Features

The Vertex AI RAG Agent enables you to:

- 🔍 **Query document corpora** with natural language questions
- 📋 **List available document corpora** in your project
- 📁 **Create new document corpora** for different use cases
- 📄 **Add new documents** to existing corpora
- 🔧 **Get detailed information** about specific corpora
- 🗑️ **Delete corpora** when they're no longer needed

## 🚀 Prerequisites

- **Google Cloud Account** with billing enabled
- **Google Cloud Project** with Vertex AI API enabled
- **Python 3.9+** environment
- Appropriate access to create and manage Vertex AI resources

## 🔧 Setting Up Google Cloud Authentication

Before running the agent, set up authentication with Google Cloud:

### 1. Install Google Cloud CLI

Visit [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) for installation instructions for your OS.

### 2. Initialize the Google Cloud CLI

```bash
gcloud init
```

This will guide you through logging in and selecting your project.

### 3. Set up Application Default Credentials

```bash
gcloud auth application-default login
```

This opens a browser window for authentication and stores credentials in:
`~/.config/gcloud/application_default_credentials.json`

### 4. Verify Authentication

```bash
gcloud auth list
gcloud config list
```

### 5. Enable Required APIs

```bash
gcloud services enable aiplatform.googleapis.com
```

## ⚡ Installation

### 1. Set up Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows
.venv\Scripts\activate

# Activate on macOS/Linux
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Agent

```bash
python rag_agent/agent.py
```

## 🛠️ Available RAG Tools

The agent provides these tools for document management and querying:

| Tool | Description | Use Cases |
|------|-------------|-----------|
| **Query Documents** | Ask questions and get answers from corpus | Research, Q&A, document analysis |
| **List Corpora** | Show all available document collections | Discovery, corpus management |
| **Create Corpus** | Create new empty document corpus | New project setup, data organization |
| **Add Documents** | Add files to existing or new corpora | Content ingestion, data updates |
| **Get Corpus Info** | Detailed information about specific corpus | Monitoring, debugging, analysis |
| **Delete Corpus** | Remove corpora that are no longer needed | Cleanup, project management |

## 💡 Usage Examples

Once running, interact with the agent using natural language:

- *"What documents do I have available?"*
- *"Create a new corpus called 'company-policies'"*
- *"Add this PDF to my research corpus"*
- *"What are the main points in the quarterly report?"*
- *"Show me information about the marketing corpus"*
- *"Delete the old training materials corpus"*

## 🔧 Tool Details

### Query Documents

- Automatically retrieves relevant information from specified corpus
- Generates informative responses based on retrieved content
- Supports complex queries and follow-up questions

### Create Corpus

- Specify custom name for your corpus
- Sets up corpus with recommended embedding model configuration
- Prepares corpus for document ingestion

### Add Documents

- Supports Google Drive URLs and GCS (Google Cloud Storage) paths
- Automatically creates new corpora if they don't exist
- Handles various document formats (PDF, TXT, DOCX, etc.)

### Get Corpus Information

- Shows document count, file metadata, and creation time
- Useful for understanding corpus contents and structure
- Provides embedding model and configuration details

### Delete Corpus

- Requires confirmation to prevent accidental deletion
- Permanently removes corpus and all associated files
- Cannot be undone - use with caution

## 🐛 Troubleshooting

### Authentication Problems

- Run `gcloud auth application-default login` again
- Check if your service account has necessary permissions
- Verify you're using the correct Google Cloud project

### API Errors

- Ensure Vertex AI API is enabled: `gcloud services enable aiplatform.googleapis.com`
- Verify your project has billing enabled
- Check API quotas in Google Cloud Console

### Quota Issues

- Check Google Cloud Console for quota limitations
- Request quota increases if needed
- Monitor usage patterns to optimize requests

### Missing Dependencies

- Ensure all requirements are installed: `pip install -r requirements.txt`
- Check Python version compatibility (3.9+)
- Verify virtual environment is activated

## 📁 Project Structure

```text
adk-rag-agent/
├── rag_agent/
│   ├── __init__.py
│   ├── agent.py            # Main RAG agent implementation
│   └── tools/              # RAG-specific tools
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔗 Navigation

- **[⬅️ Back to AI with Brandon Examples](../README.md)**
- **[🎬 Watch the ADK Tutorial](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s)**
- **[📚 Explore Other Examples](../)**

## 📖 Additional Resources

- **[Vertex AI RAG Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/rag-overview)**
- **[Google ADK Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder)**
- **[Google Cloud Authentication Guide](https://cloud.google.com/docs/authentication)**
- **[Vertex AI Console](https://console.cloud.google.com/vertex-ai)**

## 🙏 Credits

Created by **[Brandon Hancock](https://github.com/bhancockio)** - Thank you for making advanced RAG systems accessible with ADK!

## 🚀 Next Steps

- Explore the [ADK Crash Course](../_adk-crash-course/) for foundational concepts
- Try the [MCP Tutorial](../adk-mcp-tutorial/) for database integration
- Build your own RAG system with custom document sources

## 📄 License

Please refer to the original creator's licensing terms.

---

**Ready to build intelligent document agents?** 📚 Start by setting up your Google Cloud authentication above!
