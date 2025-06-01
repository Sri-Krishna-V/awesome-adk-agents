# 📚 RAG Agent

## Overview

This agent enhances Large Language Models (LLMs) by integrating external knowledge through Retrieval Augmented Generation (RAG). It dynamically fetches relevant information from specified data sources (text, PDF, Google Drive) to provide more accurate, up-to-date, and context-aware responses.

**What it does:**

- 📖 **Indexes diverse data sources**: Supports text files, PDFs, and Google Drive documents.
- 🔍 **Retrieves relevant information**: Dynamically fetches context based on user queries.
- 💬 **Augments LLM responses**: Provides LLMs with external knowledge for richer, more accurate answers.
- 🛠️ **Flexible and extensible**: Easily adaptable to various data sources and LLM models.

Perfect for applications requiring LLMs to access and utilize specific domain knowledge or real-time information!

## Agent Details

| Feature | Description |
| --- | --- |
| **Interaction Type** | Conversational |
| **Complexity** | Medium |
| **Agent Type** | Single Agent |
| **Components** | RAG, Tools, Google Drive API |
| **Vertical** | All Industries (Knowledge Augmentation) |

### 🏗️ Architecture

<img src="rag-architecture.png" alt="RAG Agent Architecture" width="800"/>

### ✨ Key Features

- **🔌 Dynamic Knowledge Integration**: Seamlessly connects LLMs to external data.
- **📚 Multi-Source Support**: Handles text, PDF, and Google Drive for comprehensive knowledge access.
- **🎯 Contextual Accuracy**: Improves response relevance by grounding LLMs in specific information.
- **⚙️ Customizable Retrieval**: Fine-tune retrieval strategies for optimal performance.
- **🚀 Scalable Design**: Built to handle growing knowledge bases and user demands.

## Setup and Installation

### Prerequisites

- Python 3.10+
- Poetry: [https://python-poetry.org/docs/](https://python-poetry.org/docs/)
- Google Cloud SDK: [https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)
- A Google Cloud Project with the Vertex AI API and Google Drive API enabled.

### Installation Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/google/adk-samples.git
    cd adk-samples/python/agents/RAG
    ```

2. **Install Dependencies:**

    ```bash
    poetry install
    ```

3. **Authenticate Google Cloud:**

    ```bash
    gcloud auth application-default login
    gcloud auth application-default set-quota-project YOUR_PROJECT_ID
    ```

4. **Configure Environment Variables:**
    Create a `.env` file in the `RAG` directory and add the following:

    ```env
    GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
    GOOGLE_CLOUD_LOCATION="YOUR_PROJECT_LOCATION" # e.g., us-central1
    # Optional: Specify a GCS bucket for RAG data
    # GOOGLE_CLOUD_STORAGE_BUCKET="YOUR_GCS_BUCKET_NAME"

    # For Google Drive Integration (Optional)
    # Follow instructions in "Enable Google Drive API" section below
    # GOOGLE_DRIVE_FOLDER_ID="YOUR_GOOGLE_DRIVE_FOLDER_ID"
    # GOOGLE_DRIVE_CREDENTIALS_FILE="path/to/your/credentials.json"
    ```

### Enable Google Drive API (Optional)

If you want to use Google Drive as a data source:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Select your project.
3. Go to "APIs & Services" > "Enabled APIs & services".
4. Click "+ ENABLE APIS AND SERVICES" and search for "Google Drive API". Enable it.
5. Go to "APIs & Services" > "Credentials".
6. Click "+ CREATE CREDENTIALS" > "OAuth client ID".
    - If prompted, configure the OAuth consent screen. Select "Desktop app" for Application type.
    - Name your OAuth client ID (e.g., "RAG Agent Desktop Client").
7. Download the JSON credentials file. Save it (e.g., as `credentials.json`) and update `GOOGLE_DRIVE_CREDENTIALS_FILE` in your `.env` file with its path.
8. Share the Google Drive folder you want to use with the client email address found in your `credentials.json` file. Get the Folder ID from the URL of the Google Drive folder (it's the last part of the URL). Update `GOOGLE_DRIVE_FOLDER_ID` in your `.env`.

    The first time you run the agent with Google Drive enabled, you will be prompted to authorize access via a URL in your browser.

## Running the Agent

### Indexing Data

Before running the agent for conversation, you need to index your data sources.

**1. Local Files (Text/PDF):**

- Place your `.txt` or `.pdf` files in a directory (e.g., `data/local_files/`).
- Run the indexing script:

    ```bash
    poetry run python rag_agent/indexing/index_local_files.py --data_path data/local_files/ --collection_name local_knowledge
    ```

    (Replace `data/local_files/` with your data directory and `local_knowledge` with your desired collection name).

**2. Google Drive:**

- Ensure you have configured Google Drive API access and environment variables.
- Run the indexing script:

    ```bash
    poetry run python rag_agent/indexing/index_google_drive.py --collection_name drive_knowledge
    ```

    (Replace `drive_knowledge` with your desired collection name).

You can create multiple collections for different datasets.

### Starting the Conversational Agent

Once your data is indexed, you can run the agent:

**Using ADK CLI:**

```bash
poetry run adk run rag_agent --collection_name YOUR_COLLECTION_NAME
```

(Replace `YOUR_COLLECTION_NAME` with the name of the collection you want to use, e.g., `local_knowledge` or `drive_knowledge`).

**Using ADK Web UI:**

1. Start the ADK web server:

    ```bash
    poetry run adk web
    ```

2. Open the provided URL in your browser.
3. Select `rag_agent` from the agent dropdown.
4. In the "Session Params" section, provide the `collection_name` you want to use (e.g., `{"collection_name": "local_knowledge"}`).
5. Start chatting!

### Example Interaction

**User:** What are the key features of the new Alpha Product? (Assuming 'Alpha Product' details are in your indexed documents)

**Agent:** (After retrieving relevant chunks from the indexed data) The new Alpha Product features include an enhanced AI-powered analytics engine, a redesigned user interface for better usability, and seamless integration with existing enterprise systems. It also offers advanced security protocols and scalable performance for growing data needs.

## Testing

To run the tests:

```bash
poetry install --with dev
poetry run pytest tests/
```

## Customization

- **LLM Model**: Change the underlying LLM in `rag_agent/agent.py`.
- **Embedding Model**: Modify the embedding model in `rag_agent/vector_store.py`.
- **Chunking Strategy**: Adjust text splitting parameters in the indexing scripts (`rag_agent/indexing/`).
- **Number of Chunks Retrieved**: Modify the `num_chunks` parameter in `rag_agent/agent.py` to control how many relevant pieces of information are passed to the LLM.

## Troubleshooting

- **Authentication Errors**: Double-check your Google Cloud project ID, location, and that the necessary APIs are enabled. Ensure `gcloud auth application-default login` was successful.
- **Google Drive Access Denied**: Verify that the Google Drive API is enabled, credentials are correct, the folder ID is accurate, and the folder is shared with the client email from `credentials.json`.
- **No Relevant Information Found**:
  - Ensure your data was indexed correctly into the specified collection.
  - Try different phrasing for your queries.
  - Adjust chunking strategy or embedding model for better relevance.
- **Poetry Issues**: Ensure Poetry is installed correctly and you are in the `RAG` directory when running `poetry install`.

## Disclaimer

This RAG agent is a sample and should be adapted and tested thoroughly for production use. Consider aspects like data security, error handling, and scalability based on your specific requirements.
