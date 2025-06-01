# 🔍 Brand Search Optimization Agent

## Overview

A powerful AI-driven solution designed to enhance e-commerce product data and boost search performance! This intelligent agent tackles the common retail challenges of "Null & low recovery" and "Zero Results" searches by analyzing and enriching product information through competitive intelligence.

**What it does:**

- 🎯 **Keyword Generation**: Creates targeted keywords based on product titles, descriptions, and attributes
- 🌐 **Competitive Analysis**: Visits competitor websites and analyzes top search results
- 💡 **Data Enrichment**: Provides smart suggestions for improving product titles, descriptions, and attributes
- 📊 **Gap Identification**: Identifies missing data elements that impact search performance
- 🤖 **Web Automation**: Uses computer vision and web crawling for real-time competitive intelligence

Perfect for e-commerce retailers looking to optimize product discoverability and reduce search abandonment!

## Agent Details

| Feature | Description |
|---|---|
| **Interaction Type** | Workflow |
| **Complexity** | Advanced |
| **Agent Type** | Multi Agent |
| **Multi Agent Design Pattern** | Router Agent |
| **Components** | BigQuery Connection, Computer Use, Web Crawling, Tools, Evaluation |
| **Vertical** | Retail / E-commerce |

### 🏗️ Agent Architecture

![Brand Search Optimization Architecture](./brand_search_optimization.png)

### ✨ Key Features

#### 🛠️ Core Tools

- **`function_calling`**: Intelligent data retrieval from product catalogs via BigQuery based on brand parameters
- **`load_artifacts_tool`**: Advanced web page analysis for actionable insights like search button interactions
- **`computer_use`**: Automated web browsing and competitive analysis
- **`bigquery_connector`**: Real-time product data access and enrichment

#### 🚀 Capabilities

- **Smart Keyword Generation**: AI-powered keyword creation from product attributes
- **Competitive Intelligence**: Real-time analysis of competitor search results  
- **Data Gap Analysis**: Identifies missing product information affecting discoverability
- **Automated Enrichment**: Suggests improvements for titles, descriptions, and attributes

  - `Website crawling`: Achieved through several individual tools such as `go_to_url`,`take_screenshot`,`find_element_with_text`, `click_element_with_text`,`enter_text_into_element`, `scroll_down_screen`,`get_page_source`,`analyze_webpage_and_determine_action`

- **Evaluation:** The agent uses OOTB evaluation provided by the ADK and it can be run using `sh deployment/eval.sh` script.

## Setup and Installation

1. **Prerequisites:**
    - Python 3.11+
    - Poetry
        - For dependency management and packaging. Please follow the instructions on the official [Poetry website](https://python-poetry.org/docs/) for installation.
    - A project on Google Cloud Platform
    - Get your API key from [here](https://aistudio.google.com).(Not needed if you want to use Gemini from Vertex AI)

2. **Configuration:**
    - Env file setup
        - Copy example env file `cp env.example .env`
        - Set `DISABLE_WEB_DRIVER=1`
        - Add values for following variables in the `.env` file
            - `GOOGLE_CLOUD_PROJECT=<YOUR_PROJECT>`
            - `GOOGLE_CLOUD_LOCATION=<YOUR_LOCATION>`

    - **API Keys:**
        - Your API key should be added under `.env` in `GOOGLE_API_KEY` variable
        - You don't need both Google API key and the Vertex AI setup. Either set up will work.
    - **BigQuery Setup**
        - BigQuery DATASET_ID should be under `.env` in `DATASET_ID`
        - BigQuery TABLE_ID should be under `.env` in `TABLE_ID`
        - BigQuery table setup can be done using automatically following the `sh deployment/run.sh` below or manually by following steps in `BigQuery Setup` section.

    - **Other Configuration:**
        - You can change Gemini Model by changing `MODEL` under `.env`
        - `DISABLE_WEB_DRIVER` when set to `1`, will enable you to run unit tests. See `Unit Tests` section below for details. **NOTE** keep this flag to 0 by default when not testing.

3. **Authenticate with your Google Cloud account:**

    ```bash
    gcloud auth application-default login
    ```

4. **Installation:**

    - Install dependencies and populate database using  `deployment/run.sh`

        `````bash
        # Clone this repository.
        git clone https://github.com/google/adk-samples.git
        cd adk-samples/python/agents/brand-search-optimization

        # Run This script
        # 1. Creates and activates a new virtual env
        # 2. Installs python packages
        # 3. Populates BigQuery data using variables set in `.env` file
        sh deployment/run.sh
        `````

    - Set `DISABLE_WEB_DRIVER=0`

## Running the Agent

You have to run the `adk run brand_search_optimization` to make the agent run.

You may also run the web app using `adk web`.

The command `adk web` will start a web server on your machine and print the URL. You may open the URL and interact with the agent in a chatbot interface. The UI is initially blank.

Select "brand-search-optimization" from the drop-down menu.

> **NOTE** This should open a new chrome window through web-driver. If it doesn't, please make sure `DISABLE_WEB_DRIVER=0` in the `.env` file.

### Brand Name

- If you ran the `deployment/run.sh` script. The agent will be pre-configured for the brand `BSOAgentTestBrand`. When the agent asks for a brand name, please provide `BSOAgentTestBrand` as your brand name.
- For custom data, please modify the brand name.
- The agent flow triggers when you provide a brand name.

> **NOTE**
>
> - Don't close the extra chrome window opened by the agent.
> - After the agent provides a list of keywords, ask the agent to search a website. e.g. "Can you search website?", "Can you search of keywords on website?", "Help me search for keywords on website" etc.
> - While visiting Google Shopping website, you'll need to complete the captcha for the first run. After completing the captcha, the agent should run in the subsequent runs.

### Example Interaction

One example session is provided to illustrate how the Brand Search Optimizer operates for the brand BSOAgentTestBrand with Google Shopping - [`example_interaction.md`](tests/example_interaction.md)

This file contains a full dialog history between the user and various agents and tools, from keyword finding to a full comparison report between titles of the top search 3 results.

> **Disclaimer** This sample uses Google Shopping website for demonstration purposes, but it is up to you to ensure you are following the website's terms of service.

## Evaluating the Agent

This uses ADK's evaluation component to evaluate brand search optimization agent with evalset inside `eval/data/` with configs defined in `eval/data/test_config.json`

You must be inside `brand-search-optimization` dir and then run

```bash
sh deployment/eval.sh
```

## Unit Tests

Run unit test using `pytest` by following these steps

1. Modify this in `.env` `DISABLE_WEB_DRIVER=1`

2. Run `sh deployment/test.sh`

This script runs unit test with a mock BQ client for BigQuery tool in `tests/unit/test_tools.py`.

## Deploying the Agent

The Agent can be deployed to Vertex AI Agent Engine using the following
command:

Modify this in `.env` -> `DISABLE_WEB_DRIVER=1`

```bash
python deployment/deploy.py --create
```

You may also modify the deployment script for your use cases.

## Customization

How to customize

- **Modifying the Conversation Flow:** To ask the agent to compare descriptions instead of titles, you can change the prompt in `brand_search_optimization/sub_agents/search_results/prompt.py` specifically, `<Gather Information>` section under `SEARCH_RESULT_AGENT_PROMPT` can be changed.
- **Changing the Data Sources:** BigQuery table can be configured to point to a table by changing values inside `.env` file
- **Changing website:** Example website here is Google Shopping, please replace with your own, and modify any code accordingly.

### BigQuery Setup

#### Automation

`sh deployment/run.sh` runs a script that populates BigQuery table with sample data. It calls `python tools/bq_populate_data.py` script behind the scene.

#### Dataset and Table permissions

If you want to run the agent on a BigQuery Table NOT owned by you,
See instructions [here](./customization.md) to grant necessary permissions.

#### Manual Steps

Check the SQL queries inside `deployment/bq_data_setup.sql` for manually adding data

## Troubleshooting and Common Issues

### BigQuery data not present

This relates to - Data set not found, data set not found in the location, User doesn't have permission for the bigquery dataset

Error:

```bash
google.api_core.exceptions.NotFound: 404 Not found: Dataset ...:products_data_agent was not found in location US; reason: notFound, message: Not found: Dataset ...:products_data_agent was not found in location US
```

Fix:
Make sure you follow the `BigQuery Setup` section

### Selenium issues

This relates to Selenium / Webdriver issues

Error:

```bash
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: probably user data directory is already in use, please specify a unique value for --user-data-dir argument, or don't use --user-data-dir
```

Fix: Remove the data directory

```bash
rm -rf /tmp/selenium
```

### Agent flow issues

#### Known Issues

- Agent doesn't run reliably when website enforces checks for bots and when the search element is hidden.
- Agent doesn't suggest next step - This happens after keyword finding stage. Ask the agent to search for the top keyword in this case. e.g. "can you search for keyword?" or more explicitly "transfer me to web browser agent"
- Agent asks for the keyword again - e.g. `Okay, I will go to XYZ.com. What keyword do you want to search for on XYZ?`. Please provide the keyword again.

## Disclaimer

This agent sample is provided for illustrative purposes only and is not intended for production use. It serves as a basic example of an agent and a foundational starting point for individuals or teams to develop their own agents.

This sample has not been rigorously tested, may contain bugs or limitations, and does not include features or optimizations typically required for a production environment (e.g., robust error handling, security measures, scalability, performance considerations, comprehensive logging, or advanced configuration options).

Users are solely responsible for any further development, testing, security hardening, and deployment of agents based on this sample. We recommend thorough review, testing, and the implementation of appropriate safeguards before using any derived agent in a live or critical system.
