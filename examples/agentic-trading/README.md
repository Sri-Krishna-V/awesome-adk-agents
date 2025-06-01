# Agentic Trading Simulator

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-ADK-4285F4.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAhGVYSWZNTQAqAAAACAAFARIAAwAAAAEAAQAAARoABQAAAAEAAABKARsABQAAAAEAAABSASgAAwAAAAEAAgAAh2kABAAAAAEAAABaAAAAAAAAAEgAAAABAAAASAAAAAEAA6ABAAMAAAABAAEAAKACAAQAAAABAAAADqADAAQAAAABAAAADgAAAABOylT5AAAACXBIWXMAAAsTAAALEwEAmpwYAAABWWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNi4wLjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgIDwvcmRmOkRlc2NyaXB0aW9uPgogICA8L3JkZjpSREY+CjwveDp4bXBtZXRhPgoZXuEHAAACRUlEQVQoFXVSS2gTQRj+Z3aziUlF1ISkRqqpVpCaixgkkEOaUGktBopuRQXxKF68pIdCpSsYH4gWxINHT8ZmVUR7MaRND4pUFBFfB7GXqt1iAlGS5rn7O7NpFg/6HeZ/zPfN/PMxAOtQFKSd/L8RFYtDOEmWUVBVovM8fgHDDc+iv+I9VxcgAAhdEtUbP16dTL80uRlZUMdUnXREPBb3/7pDm65g1f3iS9094QRjOwBZWwO09REQ3++kD86qY6DLTAydEWOXy8lYqpzjp/4LB+4fzYVmjiXNPTYyVRRi8IIgRijqk4eua65YqnJLzqDA+wPXijdOALpbzocTaHRFeA+IYliPZaVGCD2cHfdVCJRT6lj7zS1dupoGUhCrsREgVc0Ucm1UQXFBIa3IlVJvU5ceiQTmNyPmddR9DbAZur28Wt1xJi4YjiFq2Eeen7q3FM1HGY2DGQPM1dM3C/5izZ6sGdA9Jzm1YAOc2xzfNj3bNfUJ9t2dhj74DRkQgBlk6vhSy+49b8zBG1wBD69xD4wiQI+Zg/dIHUL97Twq8mi9UaSfo03snSXd8HMlkbitBYbGPxyftHHS99HdW0qDkC4MhOIEFlqoALWEhuGoEVia5UQbLCdoffVdcObSV15v1EpPmfdbkWDbVdazhJQ2KwSlx7gIAfeTtz1EEv3F+MFBLqw7nVNIYNoz//oiG5+Cwj4UIpgGYR58tayQwJzLy8kcODxs53E5HN7AI4fy12WW2Nxhy0e5X+rk7Ia286yBMvtq6/gDb7bjW6TkRnEAAAAASUVORK5CYII=)](https://github.com/google/adk-python)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

This project demonstrates an agent-based trading system simulation featuring distinct agents for trading logic and risk management, communicating via the Agent-to-Agent (A2A) protocol. It includes a web-based simulator UI to configure, run, and visualize trading strategy performance.

**Disclaimer:** ⚠️ This application is intended for **educational and demonstration purposes only**. It does not constitute financial, investment, legal, or trading advice. Trading involves significant risk, and you could lose your entire investment. **Do not use this application for actual trading decisions or with real money.** Use at your own risk.

![Agentic Trading Simulator Overview](agentic-trading-simulator.png)

## Features

* **Modular Agent Architecture:** Separates concerns into distinct services:
  * **AlphaBot:** Implements a trading strategy (Simple Moving Average - [SMA crossover](https://en.wikipedia.org/wiki/Moving_average_crossover)) and proposes trades. Built using the [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/).
  * **RiskGuard:** Evaluates trade proposals from AlphaBot against configurable risk rules (max position size, max portfolio concentration). Also built using ADK.
  * **Simulator UI:** A [FastAPI](https://fastapi.tiangolo.com/)-based web application to configure simulation parameters, run the simulation, and visualize results using [Plotly](https://plotly.com/python/).
* **Agent-to-Agent (A2A) Communication:** Leverages the open [A2A protocol](https://github.com/google/A2A) for standardized, interoperable communication between the AlphaBot and RiskGuard agents. This allows agents built with different frameworks (like ADK in this case) to discover capabilities and interact securely.
* **Configurable Simulation:** Adjust parameters for market conditions (initial price, volatility, trend), trading strategy (SMA periods, trade quantity), and risk rules.
* **Portfolio Tracking:** Simulates portfolio changes (cash, shares, total value) based on executed trades.
* **Visualization:** Displays simulation results, including price action, SMA indicators, portfolio value, and trade execution markers on interactive charts.
* **Local & Cloud Deployment:** Includes scripts for easy local execution and deployment to [Google Cloud Run](https://cloud.google.com/run/docs).
* **Containerized Services:** Dockerfiles provided for building container images for each service, facilitated by [Google Cloud Build](https://cloud.google.com/build/docs).

## Architecture

The system consists of three main services interacting via HTTP and the A2A protocol:

1. **Simulator UI (FastAPI):**
    * Serves the web interface to the user.
    * Takes simulation parameters from the user.
    * Runs the market simulation loop.
    * For each step, it calls the **AlphaBot** service (A2A `tasks/send`) with current market data and portfolio state.
    * Receives trade decisions (approved/rejected trades or status updates) back from AlphaBot.
    * Updates the portfolio state based on executed trades.
    * Visualizes the results.

2. **AlphaBot (ADK/Python):**
    * Receives A2A requests from the Simulator.
    * Analyzes market data (calculates SMAs) to determine a potential trade signal (BUY/SELL).
    * If a trade is proposed, it calls the **RiskGuard** service (A2A `tasks/send` via `a2a_risk_tool.py`) with the trade proposal and portfolio state.
    * Receives the risk assessment result (approved/rejected) from RiskGuard.
    * Updates its internal state (`_should_be_long`).
    * Returns the final trade decision (including risk assessment outcome) back to the Simulator via an A2A response, potentially using artifacts.

3. **RiskGuard (ADK/Python):**
    * Receives A2A requests from AlphaBot containing a trade proposal and portfolio state.
    * Evaluates the proposal against configured risk rules (`rules.py`).
    * Returns the risk assessment result (approved/rejected with reason) back to AlphaBot via an A2A response, typically within an artifact.

```mermaid
graph LR
    User[Browser User] -- HTTP --> SimUI(Simulator UI<br>FastAPI);
    SimUI -- A2A (tasks/send) --> AlphaBot(AlphaBot Agent<br>ADK);
    AlphaBot -- A2A (tasks/send) --> RiskGuard(RiskGuard Agent<br>ADK);
    RiskGuard -- A2A Response --> AlphaBot;
    AlphaBot -- A2A Response --> SimUI;
```

### A2A Protocol in Action

This project utilizes the A2A protocol for the critical communication link between the trading logic (AlphaBot) and the risk assessment logic (RiskGuard). Here's how it applies the core A2A concepts:

*   **A2A Server:** Both AlphaBot and RiskGuard act as A2A Servers, exposing HTTP endpoints defined by the A2A specification.
*   **A2A Client:**
    *   The Simulator UI acts as a client when initiating a task with AlphaBot (`tasks/send`).
    *   AlphaBot acts as a client when sending a trade proposal task to RiskGuard (`tasks/send`).
*   **Task:** The primary unit of work.
    *   The Simulator sends a task to AlphaBot containing market/portfolio data.
    *   AlphaBot sends a sub-task to RiskGuard containing the proposed trade details.
*   **Message/Part:** Data like market state, portfolio details, and trade proposals are exchanged within A2A Messages using appropriate Parts (likely `DataPart` for structured JSON).
*   **Artifact:** RiskGuard returns its assessment (approved/rejected with reason) as an Artifact within the A2A response to AlphaBot. AlphaBot may also use artifacts to return structured results to the Simulator.
*   **Agent Card:** While not explicitly fetched dynamically in this simplified local setup, in a real-world scenario, AlphaBot could discover RiskGuard's capabilities and endpoint URL by fetching its `agent.json` file (Agent Card). The ADK framework handles much of the underlying A2A protocol implementation details.

This demonstrates how A2A enables modularity, allowing specialized agents to collaborate effectively.

## Getting Started

### Prerequisites

* [Python](https://www.python.org/downloads/) (Version 3.11+ recommended)
* [Google Cloud SDK (`gcloud`)](https://cloud.google.com/sdk/docs/install) (Required for Cloud Run deployment)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/kweinmeister/agentic-trading
    cd agentic-trading
    ```

2. **Install Python dependencies:**
    Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```
    Install all requirements for local development and testing:
    ```bash
    pip install -r requirements.txt
    ```

### Running Locally

The easiest way to run all services locally is using the provided script:

```bash
./deploy_local.sh
```

This script will:

* Start the **RiskGuard** service (Default: `http://127.0.0.1:8080`)
* Start the **AlphaBot** service (Default: `http://127.0.0.1:8081`)
* Start the **Simulator UI** service (Default: `http://127.0.0.1:8000`)

Wait for the script to report that all services have started, then access the Simulator UI in your browser at `http://127.0.0.1:8000`.

To stop the services, use the `kill` command shown in the script's output or `Ctrl+C` if you run the commands manually.

### Running Tests

Ensure development dependencies are installed:

```bash
pip install -r requirements-dev.txt
```

Run tests using pytest:

```bash
pytest tests/
```

## Deployment

This application includes scripts and configuration for deployment to [Google Cloud Run](https://cloud.google.com/run/docs).

### Cloud Run (Publicly Accessible)

The `deploy_cloud_run.sh` script automates the deployment of all three services to Cloud Run, making them publicly accessible.

**Before running:**

1. **Set your Google Cloud Project ID:** Edit the script and replace `"your-gcp-project-id"` with your actual project ID, or set the `PROJECT_ID` environment variable.
2. **Authenticate `gcloud`:** Ensure you are logged in with the necessary permissions (`gcloud auth login`, `gcloud config set project YOUR_PROJECT_ID`).
3. **Enable APIs:** The script attempts to enable required APIs (Cloud Run, Cloud Build, Artifact Registry). Ensure your account has permission to do this.

**Run the script:**

```bash
./deploy_cloud_run.sh
```

The script will:

1. Create a [Google Artifact Registry](https://cloud.google.com/artifact-registry/docs) repository (if it doesn't exist).
2. Build container images for RiskGuard, AlphaBot, and Simulator using [Google Cloud Build](https://cloud.google.com/build/docs) (`cloudbuild-*.yaml` files) and push them to Artifact Registry.
3. Deploy each service to Cloud Run, configuring necessary environment variables (`RISKGUARD_SERVICE_URL`, `ALPHABOT_SERVICE_URL`) for inter-service communication.
4. Output the final URL for the Simulator UI.

**Important Security Note:** The public deployment script makes your services accessible to anyone on the internet. For production or sensitive environments, you **must** secure your deployment. Consider using [Google Cloud Identity-Aware Proxy (IAP)](https://cloud.google.com/iap/docs) or other authentication/authorization mechanisms to control access.

## Configuration

* **Default Parameters:** Default settings for SMA periods, risk limits, simulation parameters, and local service URLs are defined in `common/config.py`.
* **Service URLs (Deployment):** When deploying to Cloud Run, the deployment scripts automatically pass the necessary service URLs (`RISKGUARD_SERVICE_URL`, `ALPHABOT_SERVICE_URL`) as environment variables to the dependent services (AlphaBot needs RiskGuard's URL, Simulator needs both).
* **Environment Variable `PORT`:** The Dockerfiles and Cloud Run use the standard `PORT` environment variable (automatically provided by Cloud Run) to determine the listening port.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE file](LICENSE) for details.
