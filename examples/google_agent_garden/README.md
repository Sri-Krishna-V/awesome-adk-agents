# Agent Garden: Sample Agents

This directory provides a collection of sample agents built using the
[Python Agent Development Kit](https://github.com/google/adk-python) (Python ADK).

Each folder contains a distinct agent sample.

## Getting Started

1. **Prerequisites:**

    * The Python Agent Development Kit. Refer to the
        [ADK Quickstart Guide](https://google.github.io/adk-docs/get-started/quickstart/).
    * Python 3.9+ and [Poetry](https://python-poetry.org/docs/#installation).
    * Access to Google Cloud (Vertex AI) and/or a Gemini API Key (depending on
        the agent - consult individual agent READMEs).

2. **Running a Sample Agent:**

    * Navigate to the specific agent's directory (e.g., `cd academic-research`).
    * Copy the `.env.example` file to `.env` and configure the necessary
        environment variables (API keys, project IDs, etc.). See the agent's
        specific README for details on required variables.
    * Install dependencies using Poetry: `poetry install`
    * Consult the agent's specific `README.md` for detailed instructions on running it (e.g.,
        using `adk run .` or `adk web`).

## Agent Categories

Explore the agent samples below, categorized for your convenience:

| Agent Name                                  | Use Case                                                                                                                              | Tag | Interaction Type | Complexity | Agent Type   | Vertical                      |
| :------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------- | :-: | :--------------- | :--------- | :----------- | :---------------------------- |
| [Academic Research](academic-research) | Assists researchers in identifying recent publications and discovering emerging research areas. |   Multi-agent, Custom tool, Evaluation | Workflow | Easy | Multi Agent | Academia                        |
| [Auto Insurance Agent](auto-insurance-agent) | Streamlines auto insurance claims processing, policy inquiries, and quote generation using a multi-agent system. | Multi-agent, Workflow, Document Analysis, Customer Service, Forms | Conversational / Workflow | Advanced | Multi Agent | Insurance                     |
| [Brand Search Optimization](brand-search-optimization) | Enrich e-commerce product data by analyzing and comparing top search results. Useful for addressing issues like "Null & low recovery" / "Zero Results" searches and identifies gaps in product data.                                 |   Multi-agent, Custom tool, BigQuery connection, Evaluation, Computer use   | Workflow | Easy | Multi Agent | Retail                        |
| [Cymbal Home & Garden Customer Service Agent](customer-service) | Customer service, product selection, order management for home improvement, gardening, and related supplies                                |  Custom tool, Async tool, External system calls, Live streaming, Multimodal   | Conversational         | Advanced     | Single Agent       | Retail                        |
| [Data Science Agent](data-science) | A multi-agent system designed for sophisticated data analysis                                                                          |  Function tool (Python), Agent tool, NL2SQL, Structured data, Database   | Conversational | Advanced | Multi Agent | Horizontal                    |
| [Financial Advisor](financial-advisor) |  Assists human financial advisors by providing educational content about topics related to finance and investments.  |   Risk Analysis, Strategy Generation, Summarization, Report generation  | Workflow | Easy | Multi Agent | Financial Services            |
| [FOMC Research Agent](fomc-research) | Market event analysis                                                                                                                   |   Summarization, Report generation  | Workflow | Advanced | Multi Agent | Financial Services            |
| [LLM Auditor](llm-auditor)                   | Chatbot Response Verification, Content Auditing                                                                                         |   Gemini with Google Search, Multi-agent  | Workflow         | Easy       | Multi Agent  | Horizontal                    |
| [Marketing Agency](marketing-agency)                   | Streamlines new website and product launches. Identifies optimal DNS domains, generates entire websites, develops marketing strategies, and designs brand assets. | Content generation, Website creation, Code generation, Strategy development  | Workflow         | Easy       | Multi Agent  | Horizontal                    |
| [Personalized Shopping](personalized-shopping) | Product Recommendations                                                                                                               | E-commerce, Personalized agent, Shopping assistant, Single-agent, Product recommendation, Product discovery, Chatbot    | Conversational         | Easy        | Single Agent     | E-commerce                    |
| [Software Bug Assistant](software-bug-assistant) | Helps developers identify, analyze, and resolve software bugs by understanding reports and suggesting causes/solutions. | Conversational, Code Analysis (conceptual), Developer Tool | Conversational / Workflow | Medium | Single Agent | Software Development          |
| [Time Series Forecasting Agent](time-series-forecasting) | Analyzes historical time series data to predict future trends for sales, stock markets, resource planning etc. | Data Analysis, Forecasting, Visualization, Statistical Models | Workflow / Conversational | Medium to Advanced | Single Agent | Finance, Retail, Operations   |
| [Travel Concierge](travel-concierge) | Travel Concierge, Digital Tasks Assistant                                                                                               |   Function tool (Python), Custom tool, Agent tool, Input and output schema, Updatable context, Dynamic instructions  | Conversational | Advanced | Multi Agent | Travel                        |
| [Vertex AI Retrieval Agent](RAG) | RAG Powered Agent / Answering questions related to documents uploaded to Vertex AI RAG Engine, providing informative responses with citations to source materials.                              |  RAG engine   | Workflow              | Intermediate        | Single Agent       | Horizontal                    |

## Using the Agents in this Repository

This section offers general guidance on running, testing, evaluating, and deploying the agent samples in this collection. While the core steps are similar, **each agent has its own specific requirements and detailed instructions within its dedicated `README.md` file.**

**Always consult the `README.md` inside the specific agent's directory (e.g., `fomc-research/README.md`) for the most accurate and detailed steps.**

Below is a general workflow:

1. **Choose an Agent:** Select an agent from the table above that aligns with your interests or use case.
2. **Navigate to the Agent Directory:** In your terminal, change to the
    agent's main directory. Assuming you are in the `examples/google_agent_garden/` directory:

    ```bash
    cd <agent-name>
    # Example: cd fomc-research
    ```

3. **Review the Agent's README:** **This is the most crucial step.** Open the
    `README.md` file within this directory. It will contain:
    * A detailed overview of the agent's purpose and architecture.
    * Specific prerequisites (e.g., API keys, cloud services, database setup).
    * Step-by-step setup and installation instructions.
    * Commands for running the agent locally.
    * Instructions for running evaluations (if applicable).
    * Instructions for running tests (if applicable).
    * Steps for deployment (if applicable).

4. **Setup and Configuration:**
    * **Prerequisites:** Ensure you meet both the general prerequisites (see "Getting Started" above) *and* any agent-specific prerequisites detailed in its README.
    * **Dependencies:** Install the agent's specific Python dependencies using
        Poetry (this command is usually run from the agent's main directory):

        ```bash
        poetry install
        ```

    * **Environment Variables:** Most agents require configuration via
        environment variables. Copy the `.env.example` file to `.env` within the
        agent's directory and populate it with your specific values (API keys,
        project IDs, etc.). Consult the agent's README for details on required
        variables. You may need to load these variables into your shell
        environment (e.g., using `source .env` or, for bash/zsh: `set -o allexport; source .env; set +o allexport`).

5. **Running the Agent Locally:**
    * Agents can typically be run locally for testing and interaction using
        the ADK CLI or ADK Dev UI. The specific command might vary slightly
        (e.g., the exact directory to run from), so check the agent's README.
        * **CLI:** Often involves running `adk run .` from within the agent's
            *core code* directory (e.g., `<agent-name>/<agent_name_core_python_package>/`).

            ```bash
            # Example (assuming you are in examples/google_agent_garden/):
            cd fomc-research/fomc_research/
            adk run .
            ```

        * **ADK Dev UI:** Often involves running `adk web .` from the agent's
            *main* directory (e.g., `<agent-name>/`).

            ```bash
            # Example (assuming you are in examples/google_agent_garden/):
            cd fomc-research/
            adk web .
            # Or, if you were in the core code directory like fomc-research/fomc_research/:
            # cd .. 
            # adk web .
            ```

            Then, open the provided URL in your browser and select the agent from the dropdown menu.

6. **Evaluating the Agent:**
    * Many agents include an `eval/` directory containing scripts and data to assess performance.
    * The agent's README will explain how to run these evaluations (e.g.,
        `python eval/test_eval.py`). This helps verify the agent's effectiveness
        on specific tasks.

7. **Testing the Agent Components:**
    * A `tests/` directory often contains unit or integration tests (e.g., for custom tools).
    * These ensure the individual code components function correctly.
    * The agent's README may provide instructions on how to run these tests,
        often using a framework like `pytest`.

8. **Deploying the Agent:**
    * Some agents are designed for deployment, typically to
        [Vertex AI Agent Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview).
    * The `deployment/` directory contains the necessary scripts (like
        `deploy.py`) and configuration files.
    * Deployment usually requires specific Google Cloud setup (Project ID,
        enabled APIs, permissions). The agent's README and the scripts within
        the `deployment/` folder provide detailed instructions, similar to the
        example shown in the `fomc-research` agent's documentation.

By following the specific instructions in each agent's `README.md`, you can effectively set up, run, evaluate, test, and potentially deploy these diverse examples.

## Directory Structure of Agents

Each agent in this collection typically follows this directory structure:

```bash
agent-name/                             # Root directory for the agent (e.g., llm-auditor/)
├── agent_name/                         # Core Python package for the agent (e.g., llm_auditor/)
│   ├── shared_libraries/               # Optional: Helper functions for tools
│   ├── sub_agents/                     # Optional: For multi-agent setups
│   │   ├── sub_agent_one/
│   │   │   ├── tools/                  # Tools specific to sub_agent_one
│   │   │   ├── agent.py                # Core logic of sub_agent_one
│   │   │   └── prompt.py               # Prompt for sub_agent_one
│   │   └── ...                         # Additional sub-agents
│   ├── __init__.py                     # Makes agent_name a Python package
│   ├── tools/                          # Tools used by the main agent or router
│   ├── agent.py                        # Core logic of the main agent
│   └── prompt.py                       # Prompts for the main agent
├── deployment/                         # Scripts for deployment (e.g., to Vertex AI Agent Engine)
├── eval/                               # Evaluation scripts and data
├── tests/                              # Unit and integration tests
├── agent_pattern.png                   # Optional: Diagram of the agent's architecture
├── .env.example                        # Example environment variable configuration
├── pyproject.toml                      # Project configuration for Poetry
└── README.md                           # Agent-specific documentation
```

### General Structure

The root of each agent is in its own directory within this `google_agent_garden` folder. For example, the `llm-auditor` agent is located at `llm-auditor/`.

### Directory Breakdown

1. **`agent_name/` (Core Agent Code)**:
    * This directory contains the core logic of the agent.
    * **`shared_libraries/`**: (Optional) Contains code that is shared among multiple sub-agents.
    * **`sub_agents/`**: Contains the definitions and logic for sub-agents.
        * Each sub-agent has its own directory (e.g., `critic/`, `reviser/` in `llm-auditor`).
        * **`tools/`**: Contains any custom tools specific to the sub-agent.
        * **`agent.py`**: Defines the sub-agent's behavior, including its model, tools, and instructions.
        * **`prompt.py`**: Contains the prompts used to guide the sub-agent's behavior.
    * **`__init__.py`**: An initialization file that imports the `agent.py` from the folder for marking the `agent_name` directory as a Python package.
    * **`tools/`**: Contains any custom tools used by the main agent.
    * **`agent.py`**: Defines the main agent's behavior, including its sub-agents, model, tools, and instructions.
    * **`prompt.py`**: Contains the prompts used to guide the main agent's behavior.

    Note: The top-level agent directory often uses hyphens (e.g., `llm-auditor`), while the inner Python package directory containing the core logic uses underscores (e.g., `llm_auditor`). This convention is often influenced by Python packaging standards and tools like Poetry.

2. **`deployment/`**

    * Contains scripts and files necessary for deploying the agent to a
        platform like Vertex AI Agent Engine.
    * The `deploy.py` script is often found here, handling the deployment process.

3. **`eval/`**

    * Contains data and scripts for evaluating the agent's performance.
    * Test data (e.g., `.test.json` files) and evaluation scripts (e.g.,
        `test_eval.py`) are typically located here.

4. **`tests/`**

    * Contains unit and integration tests for the agent.
    * Test files (e.g., `test_agents.py`) are used to verify the agent's functionality.

5. **`agent_pattern.png`**

    * A visual diagram illustrating the agent's architecture, including its sub-agents and their interactions.

6. **`.env.example`**

    * An example file showing the environment variables required to run the agent.
    * Users should copy this file to `.env` and fill in their specific values.

7. **`pyproject.toml`**

    * Contains project metadata, dependencies, and build system configuration.
    * Managed by Poetry for dependency management.

8. **`README.md`**

    * Provides detailed documentation specific to the agent, including its purpose, setup instructions, usage examples, and customization options.

## Example: `llm-auditor`

The `llm-auditor` agent demonstrates this structure effectively. It has:

* A core `llm_auditor/` directory.
* Sub-agents in `llm_auditor/sub_agents/`, such as `critic/` and `reviser/`.
* Deployment scripts in `deployment/`.
* Evaluation data and scripts in `eval/`.
* Tests in `tests/`.
* An `.env.example` file.
* A `pyproject.toml` file.
* A `README.md` file.
