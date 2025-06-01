# 📈 Time Series Forecasting Agent

## Overview

An AI-powered agent specializing in time series analysis and forecasting. This agent uses historical data to predict future trends, making it invaluable for applications like sales forecasting, stock market analysis, and resource planning.

**What it does:**
- 📊 **Analyzes time series data**: Identifies trends, seasonality, and patterns in historical data.
- 🔮 **Generates forecasts**: Predicts future values using statistical models and machine learning.
- 📈 **Visualizes results**: Creates plots and charts to illustrate forecasts and data insights.
- ⚙️ **Adaptable models**: Can be configured to use various forecasting techniques (e.g., ARIMA, Exponential Smoothing, Prophet).

Perfect for businesses and analysts needing to make data-driven decisions based on future projections!

## Agent Details

| Feature | Description |
| --- | --- |
| **Interaction Type** | Workflow / Conversational |
| **Complexity** | Medium to Advanced |
| **Agent Type** | Single Agent (can incorporate specialized sub-agents) |
| **Components** | LLM, Data Analysis Libraries (e.g., Pandas, NumPy), Forecasting Libraries (e.g., Statsmodels, Prophet), Plotting Libraries (e.g., Matplotlib, Seaborn) |
| **Vertical** | Finance, Retail, Operations, Economics (any field with time series data) |

### 🏗️ Architecture (Conceptual)

*(A detailed architecture diagram would show data input, preprocessing, model selection, training, forecasting, and output visualization components.)*

**Conceptual Flow:**
1.  User provides time series data (e.g., CSV file with date/time and value columns).
2.  Agent ingests and preprocesses the data (handles missing values, resampling, etc.).
3.  Agent performs exploratory data analysis (identifies trends, seasonality).
4.  User (or agent automatically) selects a forecasting model.
5.  Agent trains the model on historical data.
6.  Agent generates forecasts for a specified future period.
7.  Agent presents forecasts and visualizations to the user.

### ✨ Key Features

- **🕰️ Comprehensive Time Series Analysis**: Handles various data characteristics.
- **🤖 Multiple Forecasting Models**: Supports a range of statistical and ML techniques.
- **📊 Rich Visualizations**: Clear charts for understanding data and forecast results.
- **💾 Data Input Flexibility**: Accepts common data formats (e.g., CSV).
- **⚙️ Customizable Parameters**: Allows tuning of model parameters for specific datasets.

## Setup and Installation

### Prerequisites

*   Python 3.10+
*   Poetry: [https://python-poetry.org/docs/](https://python-poetry.org/docs/)
*   Access to a Large Language Model (optional, for conversational interaction or model selection guidance).

### Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/google/adk-samples.git
    cd adk-samples/python/agents/time-series-forecasting
    ```

2.  **Install Dependencies:**
    ```bash
    poetry install
    ```
    (This will install common libraries like `pandas`, `statsmodels`, `prophet`, `matplotlib`. Add others to `pyproject.toml` as needed.)

3.  **Configure Environment Variables (if using an LLM):**
    Create a `.env` file in the `time-series-forecasting` directory if you plan to use an LLM for advanced features.
    Example for Vertex AI:
    ```env
    GOOGLE_GENAI_USE_VERTEXAI=true
    GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
    GOOGLE_CLOUD_LOCATION="YOUR_PROJECT_LOCATION"
    ```
    Authenticate if necessary:
    ```bash
    gcloud auth application-default login
    gcloud auth application-default set-quota-project YOUR_PROJECT_ID
    ```

## Running the Agent

**Using ADK CLI (Workflow Example):**

(The exact command will depend on how the agent is structured. It might involve pointing to a data file and specifying forecast parameters.)

Example (conceptual - actual implementation will vary):
```bash
poetry run adk run time_series_forecasting --data_file path/to/your/data.csv --date_column Date --value_column Sales --forecast_periods 12 --model ARIMA
```

**Using ADK Web UI (for conversational interaction or simpler workflows):**

1.  Start the ADK web server:
    ```bash
    poetry run adk web
    ```
2.  Open the provided URL in your browser.
3.  Select `time_series_forecasting_agent` (or similar name) from the agent dropdown.
4.  Interact with the agent, potentially uploading data or specifying analysis parameters through the chat interface or session parameters.

### Example Interaction (Conversational Style)

**User:** I have a CSV file with monthly sales data for the last 3 years. Can you help me forecast sales for the next 6 months?
*(User uploads `sales_data.csv`)*

**Agent:** Certainly! I've loaded `sales_data.csv`. It has columns: `Month` and `Sales`.
I see a clear upward trend and some seasonality in your sales data.

I can use a model like SARIMA or Prophet. Which would you prefer, or shall I pick one based on the data characteristics?

**User:** Use Prophet.

**Agent:** Okay, I'm training a Prophet model on your sales data...
Training complete. Here is the forecast for the next 6 months:

| Month      | Forecasted Sales |
|------------|------------------|
| 2025-07-01 | 12500            |
| 2025-08-01 | 12800            |
| ...        | ...              |

Here is a plot showing the historical data, the forecast, and the confidence intervals:
*(Agent displays a plot)*

Would you like to see the component plot showing trend and seasonality?

## Testing

(Test cases would involve using sample time series datasets and verifying the accuracy/reasonableness of the forecasts and the correctness of visualizations.)

To run tests (once implemented):
```bash
poetry install --with dev
poetry run pytest tests/
```

## Customization

*   **Add More Models**: Integrate other forecasting libraries or custom model implementations.
*   **Advanced Preprocessing**: Include more sophisticated data cleaning and feature engineering steps.
*   **Model Evaluation Metrics**: Implement various metrics (RMSE, MAE, MAPE) for evaluating forecast accuracy.
*   **Hyperparameter Tuning**: Add capabilities for automatic hyperparameter optimization.
*   **Anomaly Detection**: Extend the agent to identify outliers or anomalies in the time series.

## Troubleshooting

*   **Library Installation Issues**: Ensure all dependencies in `pyproject.toml` are compatible and install correctly. Some libraries might have system-level dependencies.
*   **Data Format Errors**: Verify your input data is in a supported format (e.g., CSV with clear date/time and value columns) and that column names are correctly specified.
*   **Model Training Failures**: Check for issues like insufficient data, non-stationarity (for models like ARIMA), or incorrect model parameters.

## Disclaimer

This Time Series Forecasting Agent is a sample. Forecasting is a complex field; always validate model outputs and consider the assumptions and limitations of the chosen forecasting methods before making critical decisions based on its predictions.
