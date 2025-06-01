# ✈️ Travel Concierge Agent

## Overview

Your personal AI travel assistant, designed to make trip planning seamless and enjoyable. This agent helps users discover destinations, find flights and accommodations, and create personalized itineraries.

**What it does:**
- 🌍 **Destination Discovery**: Suggests travel locations based on user preferences (e.g., interests, budget, travel dates).
- ✈️ **Flight & Hotel Search**: Integrates with travel APIs to find flight and accommodation options (conceptual).
- 🗺️ **Itinerary Planning**: Helps create detailed daily schedules with activities and bookings.
- 💡 **Local Recommendations**: Provides suggestions for restaurants, attractions, and local experiences.

Perfect for travelers looking for a hassle-free way to plan their next adventure!

## Agent Details

| Feature | Description |
| --- | --- |
| **Interaction Type** | Conversational |
| **Complexity** | Medium to Advanced (depending on API integrations) |
| **Agent Type** | Single Agent (can be extended with specialized sub-agents for booking, etc.) |
| **Components** | LLM, Tools (e.g., Travel APIs for flights, hotels, activities - conceptual), Session Memory |
| **Vertical** | Travel & Hospitality |

### 🏗️ Architecture (Conceptual)

*(A detailed architecture would show integration points with external travel APIs, a user preference store, and an itinerary management module.)*

**Conceptual Flow:**
1.  User expresses travel intent (e.g., "I want to plan a beach vacation in July").
2.  Agent asks clarifying questions (budget, duration, interests).
3.  Agent suggests destinations.
4.  User selects a destination.
5.  Agent (via tools) searches for flight and hotel options.
6.  User makes selections.
7.  Agent helps build a daily itinerary with activities and recommendations.
8.  Agent can provide booking links or (in advanced versions) make bookings.

### ✨ Key Features

- **💬 Personalized Planning**: Tailors suggestions to individual user needs.
- **🔍 Comprehensive Search**: Accesses a wide range of travel options (conceptual via API tools).
- **📅 End-to-End Itinerary Creation**: From initial ideas to a full schedule.
- **📍 Local Insights**: Offers recommendations for an authentic travel experience.
- **🤖 Conversational Ease**: Plan your trip through natural language interaction.

## Setup and Installation

### Prerequisites

*   Python 3.10+
*   Poetry: [https://python-poetry.org/docs/](https://python-poetry.org/docs/)
*   Access to a Large Language Model (e.g., via Vertex AI API).
*   (Optional) API keys for travel service providers (e.g., flight search, hotel booking, mapping services). These would be integrated as tools.

### Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/google/adk-samples.git
    cd adk-samples/python/agents/travel-concierge
    ```

2.  **Install Dependencies:**
    ```bash
    poetry install
    ```

3.  **Configure Environment Variables:**
    Create a `.env` file in the `travel-concierge` directory. Add your LLM API keys and any travel API keys.
    Example for Vertex AI:
    ```env
    GOOGLE_GENAI_USE_VERTEXAI=true
    GOOGLE_CLOUD_PROJECT="YOUR_PROJECT_ID"
    GOOGLE_CLOUD_LOCATION="YOUR_PROJECT_LOCATION"

    # Example for conceptual travel APIs (replace with actual keys if integrated)
    # FLIGHT_API_KEY="YOUR_FLIGHT_API_KEY"
    # HOTEL_API_KEY="YOUR_HOTEL_API_KEY"
    ```
    Authenticate if necessary (e.g., for Vertex AI):
    ```bash
    gcloud auth application-default login
    gcloud auth application-default set-quota-project YOUR_PROJECT_ID
    ```

## Running the Agent

**Using ADK CLI:**

```bash
poetry run adk run travel_concierge_agent
```

**Using ADK Web UI:**

1.  Start the ADK web server:
    ```bash
    poetry run adk web
    ```
2.  Open the provided URL in your browser.
3.  Select `travel_concierge_agent` (or similar name) from the agent dropdown.
4.  Start planning your trip by chatting with the agent.

### Example Interaction

**User:** Hi! I want to plan a 7-day trip to Europe in September. I like history and good food. My budget is around $3000 for flights and hotels.

**Agent:** Hello! A 7-day trip to Europe in September sounds wonderful. Given your interest in history and food, and a budget of around $3000, how about considering Rome, Italy, or Lisbon, Portugal? Both cities are rich in history and have amazing culinary scenes.

**User:** Rome sounds great!

**Agent:** Excellent choice! Rome is fantastic. Let me look into some flight options for you for September from your typical departure city (you can tell me if it's different).

*(Conceptual: Agent uses a flight tool)*
I found a few round-trip flights to Rome (FCO) in September for around $700-$900.

For accommodation, are you looking for a hotel, Airbnb, or something else? And what's your preferred style (e.g., boutique, budget-friendly, luxury)?

**User:** A mid-range hotel near the city center would be perfect.

**Agent:** Okay, searching for mid-range hotels in central Rome for 7 nights in September...
*(Conceptual: Agent uses a hotel tool)*
I have a few options ranging from $150-$250 per night. For example, Hotel Artemide and The Fifteen Keys Hotel have great reviews and are centrally located.

Shall we start building an itinerary? We can include visits to the Colosseum, Roman Forum, Vatican City, and of course, some amazing pasta-making classes or food tours!

## Testing

(Test cases would involve various travel planning scenarios, checking the relevance of suggestions, and verifying the conceptual integration with travel APIs.)

To run tests (once implemented):
```bash
poetry install --with dev
poetry run pytest tests/
```

## Customization

*   **Integrate Real APIs**: The core of this agent would involve integrating actual flight, hotel, and activity booking APIs as ADK Tools.
*   **User Profiles**: Store user preferences (e.g., home airport, travel style, loyalty programs) for more personalized planning.
*   **Booking Capabilities**: Extend the agent to handle actual bookings (requires robust API integration and payment processing considerations).
*   **Mapping & Navigation**: Integrate mapping services to show locations and provide directions.
*   **Price Tracking**: Add features to monitor flight or hotel price changes.

## Troubleshooting

*   **API Key Errors**: Ensure all API keys (LLM, travel services) are correctly configured in `.env` and have the necessary permissions/quotas.
*   **Tool Integration Issues**: If integrating real APIs, debugging tool calls and responses will be crucial. Check ADK tool documentation and API provider docs.
*   **Outdated Information**: Travel information (prices, availability) is highly dynamic. Real-world implementations need strategies for handling this.

## Disclaimer

This Travel Concierge Agent is a conceptual sample. A production-ready version would require robust integration with multiple third-party travel APIs, secure handling of user data and payments, and extensive testing. Always double-check information and bookings made through any automated system.