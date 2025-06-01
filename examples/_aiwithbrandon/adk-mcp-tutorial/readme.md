# 🤖 ADK Agent MCP Server Integration

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4.svg)](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder)
[![MCP](https://img.shields.io/badge/Protocol-MCP-green.svg)](https://modelcontextprotocol.io/)

> **🎥 Learn More**: Check out the [ADK Crash Course](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s) by Brandon Hancock for comprehensive ADK learning!

This project demonstrates how to integrate Google's Agent Development Kit (ADK) with Model Context Protocol (MCP) servers. Learn how ADK agents can interact with local SQLite databases through MCP, enabling powerful data-driven agent applications.

## 🌟 What You'll Learn

- **MCP Integration**: Connect ADK agents to Model Context Protocol servers
- **Database Operations**: Perform CRUD operations through agent conversations
- **Local & Remote MCP**: Work with both local and remote MCP server configurations
- **Real-world Applications**: Build practical database-driven agent systems

## 📁 Project Structure

```text
adk-mcp-tutorial/
├── local_mcp/
│   ├── agent.py             # The ADK agent for local SQLite DB
│   ├── server.py            # The MCP server exposing database tools
│   ├── create_db.py         # Script to initialize SQLite database
│   ├── database.db          # The SQLite database file
│   └── __init__.py
├── remote_mcp_agent/        # Example agent for remote MCP server
│   ├── agent.py             # The ADK agent for remote MCP
│   └── __init__.py
├── demo_comparison/         # Comparison demos
├── .env                     # Environment variables (create this)
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Google API Key** from [Google AI Studio](https://aistudio.google.com/)
- Terminal or command prompt access

### 1. Set Up Virtual Environment

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

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikeys).

### 4. Initialize Database

```bash
cd local_mcp
python create_db.py
cd ..
```

### 5. Run the Agent

```bash
python local_mcp/agent.py
```

## 🛠️ Available Database Tools

The MCP server exposes these tools for the ADK agent:

| Tool | Description | Parameters |
|------|-------------|------------|
| `list_db_tables` | Lists all database tables | `dummy_param: str` |
| `get_table_schema` | Gets table schema | `table_name: str` |
| `query_db_table` | Queries table data | `table_name: str`, `columns: str`, `condition: str` |
| `insert_data` | Inserts new records | `table_name: str`, `data: dict` |
| `delete_data` | Deletes records | `table_name: str`, `condition: str` |

## 🔧 Advanced Setup (Optional)

### Node.js for External MCP Servers

Some MCP servers require Node.js:

1. Install [Node.js](https://nodejs.org/) (LTS version recommended)
2. Verify installation:

```bash
node -v
npm -v
npx -v
```

### Docker for Containerized MCP Servers

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Verify installation:

```bash
docker --version
```

## 🐛 Troubleshooting

### Common Issues

**File Not Found Errors**
- Ensure `server.py` path is correct in `agent.py`
- Check that you're running from the project root directory

**Database Errors**
- Run `python local_mcp/create_db.py` to create the database
- Verify `database.db` exists in the `local_mcp/` folder

**API Key Issues**
- Check your `.env` file is in the project root
- Ensure `GOOGLE_API_KEY` is set correctly
- Verify your API key is valid at [Google AI Studio](https://aistudio.google.com/)

**MCP Connection Issues**
- Check `local_mcp/mcp_server_activity.log` for detailed logs
- Ensure no other processes are using the same ports

## 💡 Example Interactions

Once running, you can interact with the agent using natural language:

- *"What tables are in the database?"*
- *"Show me all users"*
- *"Add a new user named John with email john@example.com"*
- *"Find all todos that are completed"*
- *"Delete the user with ID 5"*

## 🔗 Navigation

- **[⬅️ Back to AI with Brandon Examples](../README.md)**
- **[🎬 Watch the ADK Tutorial](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s)**
- **[📚 Explore Other Examples](../)**

## 🙏 Credits

Created by **[Brandon Hancock](https://github.com/bhancockio)** - Thank you for making ADK and MCP integration accessible!

## 🚀 Next Steps

- Explore the [ADK Crash Course](../_adk-crash-course/) for more examples
- Try the [RAG Agent](../adk-rag-agent/) for document-based interactions
- Build your own MCP server for custom data sources

## 📄 License

Please refer to the original creator's licensing terms.

---

**Ready to build data-driven agents?** 🗃️ Start by running the setup commands above!
