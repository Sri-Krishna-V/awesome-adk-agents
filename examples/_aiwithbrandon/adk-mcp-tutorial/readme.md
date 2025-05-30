# ADK Agent MCP Server

This project demonstrates an Agent Development Kit (ADK) agent that interacts with a local SQLite database. The interaction is facilitated by a Model Context Protocol (MCP) server that exposes tools to query and modify the database.

## Project Structure

```
adk-mcp/
├── local_mcp/
│   ├── agent.py             # The ADK agent for the local SQLite DB
│   ├── server.py            # The MCP server exposing database tools
│   ├── create_db.py         # Script to initialize the SQLite database
│   ├── database.db          # The SQLite database file
│   └── __init__.py
├── remote_mcp_agent/        # Example agent for connecting to a remote MCP server
│   ├── agent.py             # The ADK agent configured for a remote MCP
│   └── __init__.py
├── .env                   # For GOOGLE_API_KEY (ensure it's in .gitignore if repo is public)
├── requirements.txt       # Python dependencies
└── readme.md              # This file
```

## Setup Instructions

### 1. Prerequisites
- Python 3.8 or newer
- Access to a terminal or command prompt

### 2. Create and Activate Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
# Create a virtual environment (e.g., named .venv)
python3 -m venv .venv
```

Activate the virtual environment:

On macOS/Linux:
```bash
# Activate virtual environment
source .venv/bin/activate
```

On Windows:
```bash
# Activate virtual environment
.venv\Scripts\activate
```

### 3. Install Dependencies

Install all required Python packages using pip:

```bash
# Install all dependencies from requirements.txt
pip install -r requirements.txt
```

### 4. Set Up Gemini API Key (for the ADK Agent)

The ADK agent in this project uses a Gemini model. You'll need a Gemini API key.

1.  Create or use an existing [Google AI Studio](https://aistudio.google.com/) account.
2.  Get your Gemini API key from the [API Keys section](https://aistudio.google.com/app/apikeys).
3.  Set the API key as an environment variable. Create a `.env` file in the **root of the `adk-mcp` project** (i.e., next to the `local_mcp` folder and `readme.md`):

    ```env
    # .env
    GOOGLE_API_KEY=your_gemini_api_key_here
    ```
    The `server.py` and `agent.py` will load this key.

### 5. Create the SQLite Database and Tables

The project includes a script to create and populate the SQLite database (`database.db`) with some initial tables (`users`, `todos`) and dummy data.

Navigate to the `local_mcp` directory and run the script:
```bash
cd local_mcp
python3 create_db.py
cd ..
```
This will create `local_mcp/database.db` if it doesn't already exist.

## Running the Agent and MCP Server

The ADK agent (`local_mcp/agent.py`) is configured to automatically start the MCP server (`local_mcp/server.py`) when it initializes its MCP toolset.

To run the agent:

1.  Ensure your virtual environment is active and you are in the root directory of the `adk-mcp` project.
2.  Execute the agent script:

    ```bash
    python3 local_mcp/agent.py
    ```

This will:
- Start the `agent.py` script.
- The agent, upon initializing the `MCPToolset`, will execute the `python3 local_mcp/server.py` command.
- The `server.py` (MCP server) will start and listen for tool calls from the agent via stdio.
- The agent will then be ready to process your instructions (which you would typically provide in a client application or test environment that uses this agent).

You should see log output from both the agent (if any) and the MCP server (in `local_mcp/mcp_server_activity.log`, and potentially to the console if you uncommented the stream handler in `server.py`).

## Additional Setup for Other MCP Servers (Node.js & Docker)

While the local SQLite MCP server in this specific project (`local_mcp/server.py`) only requires Python for its own execution, you might want to use this ADK agent to connect to *other* MCP servers that have different runtime dependencies. Two common dependencies for such external MCP servers are Node.js (which provides `npx` for running JavaScript-based servers) and Docker (for servers distributed as Docker images).

If you plan to use MCP servers requiring these, here's how to set them up:

### Node.js and npx

`npx` is a package runner tool that comes with `npm` (Node Package Manager), which is included with Node.js. It's often used to run MCP servers built with Node.js without needing to install them globally.

-   **Installation**: Download and install Node.js (which includes `npm` and `npx`) from the [official Node.js website](https://nodejs.org/). It is recommended to install the LTS (Long Term Support) version.
-   **Verification**: After installation, open a new terminal or command prompt window and verify the installations by typing:
    ```bash
    node -v
    npm -v
    npx -v
    ```
    You should see version numbers printed for each command, confirming they are installed and in your system's PATH.

### Docker

Docker allows applications to be packaged and run in isolated environments called containers. Some MCP servers are distributed as Docker images, making them easy to run across different operating systems.

-   **Installation**: Download and install Docker Desktop from the [official Docker website](https://www.docker.com/products/docker-desktop/). Docker Desktop is available for Windows, macOS, and Linux and provides a graphical interface as well as command-line tools.
-   **Post-Installation**: Ensure Docker Desktop is running after installation, as this starts the Docker daemon (the background service that manages containers).
-   **Verification**: Open a terminal or command prompt and verify the Docker installation by typing:
    ```bash
    docker --version
    # You can also run a test container to ensure Docker is working correctly:
    # docker run hello-world
    ```
    The first command should display your Docker version. Running `docker run hello-world` will download and run a small test image, confirming Docker is operational.

Setting up these tools will broaden the range of MCP servers your ADK agent can potentially interact with.

## Available Database Tools (Exposed by MCP Server)

The `local_mcp/server.py` exposes the following tools for the ADK agent to use:

-   **`list_db_tables(dummy_param: str) -> dict`**: Lists all tables in the database.
    *   *Note*: Requires a `dummy_param` string due to current ADK schema generation behavior; the agent's instructions guide it to provide a default.
-   **`get_table_schema(table_name: str) -> dict`**: Retrieves the schema (column names and types) for a specified table.
-   **`query_db_table(table_name: str, columns: str, condition: str) -> list[dict]`**: Queries a table.
    *   `columns`: Comma-separated list of columns (e.g., "id, username") or "*" for all.
    *   `condition`: SQL WHERE clause (e.g., "email LIKE '%@example.com'"). The agent is instructed to use "1=1" if no condition is implied.
-   **`insert_data(table_name: str, data: dict) -> dict`**: Inserts a new row into a table.
    *   `data`: A dictionary where keys are column names and values are the corresponding data for the new row.
-   **`delete_data(table_name: str, condition: str) -> dict`**: Deletes rows from a table based on a condition.
    *   *Note*: The condition cannot be empty as a safety measure.

The agent (`local_mcp/agent.py`) has specific instructions on how to use these tools effectively, including using smart defaults for parameters if not explicitly provided by the end-user's request.

## Troubleshooting

-   **`No such file or directory` for `server.py`**:
    *   Ensure `PATH_TO_YOUR_MCP_SERVER_SCRIPT` in `local_mcp/agent.py` correctly points to `local_mcp/server.py`. The current setup uses `(Path(__file__).parent / "server.py").resolve()`, which should be correct after the folder consolidation.
-   **`McpError: Input must be an instance of Schema, got <class 'NoneType'>` (Client-side Error)**:
    *   This error might occur if `adk_to_mcp_tool_type` in `server.py` generates a `None` input schema for a tool. The `list_db_tables` tool in `server.py` includes a `dummy_param` as a workaround for this known issue with parameter-less functions. The server also has a patch to provide a default schema if one is `None`.
-   **Database Errors (e.g., "no such table")**:
    *   Ensure you have run `python3 local_mcp/create_db.py` to create the `database.db` file and its tables.
    *   Verify the `DATABASE_PATH` in `local_mcp/server.py` correctly points to `local_mcp/database.db`.
-   **API Key Issues**:
    *   Make sure your `GOOGLE_API_KEY` is correctly set in the `.env` file in the project root and that the file is being loaded.
-   **MCP Server Log**:
    *   Check `local_mcp/mcp_server_activity.log` for detailed logs from the MCP server, which can help diagnose issues with tool calls or database operations.

## Future Enhancements (Ideas)
- Add an "update_data" tool to the MCP server.
- Implement more sophisticated error handling and reporting in the server tools.
- Develop a simple client application (e.g., a CLI or basic web UI) to interact with the ADK agent.
