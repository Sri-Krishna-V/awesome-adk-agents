# 🎤 ADK Voice Agent with Google Calendar Integration

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4.svg)](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder)
[![Google Calendar](https://img.shields.io/badge/Google-Calendar-4285F4.svg)](https://developers.google.com/calendar)
[![Speech Recognition](https://img.shields.io/badge/Speech-Recognition-green.svg)](https://pypi.org/project/SpeechRecognition/)

> **🎥 Learn More**: Check out the [ADK Crash Course](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s) by Brandon Hancock for comprehensive ADK learning!

Build a voice-enabled ADK agent that can interact with Google Calendar through natural speech! This project demonstrates how to integrate speech recognition, text-to-speech, and Google Calendar APIs with Google's Agent Development Kit for a complete voice assistant experience.

## 🌟 What You'll Learn

- **Voice Integration**: Implement speech-to-text and text-to-speech capabilities
- **Calendar Management**: Create, read, update, and delete calendar events
- **Natural Language Processing**: Handle voice commands with conversational AI
- **Real-time Interaction**: Build responsive voice-driven user experiences

## ✨ Features

The Voice Agent can handle:

- 🎤 **Speech Recognition** - Convert voice to text commands
- 🔊 **Text-to-Speech** - Provide audio responses
- 📅 **Calendar Operations** - Manage your Google Calendar
- 🗣️ **Natural Conversations** - Understand context and follow-ups
- ⏰ **Smart Scheduling** - Parse dates, times, and event details
- 🔄 **Real-time Updates** - Instant calendar synchronization

## 🚀 Quick Start

### Prerequisites

- **Python 3.9+**
- **Google Cloud Account** with Calendar API access
- **Microphone and speakers** for voice interaction
- **Google API Keys** for Gemini and Calendar APIs

## 📋 Setup Instructions

### 1. Install Dependencies

Create a virtual environment:

```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows
.venv\Scripts\activate

# Activate on macOS/Linux
source .venv/bin/activate
```

Install all required packages:

```bash
pip install -r requirements.txt
```

### 2. Set Up Gemini API Key

1. Create or use an existing [Google AI Studio](https://aistudio.google.com/) account
2. Get your Gemini API key from the [API Keys section](https://aistudio.google.com/app/apikeys)
3. Set the API key as an environment variable

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 3. Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Calendar API for your project:
   - In the sidebar, navigate to "APIs & Services" > "Library"
   - Search for "Google Calendar API" and enable it

### 4. Create OAuth 2.0 Credentials

1. In the Google Cloud Console, navigate to "APIs & Services" > "Credentials"
2. Click "Create Credentials" and select "OAuth client ID"
3. For application type, select "Desktop application"
4. Name your OAuth client (e.g., "ADK Voice Calendar Integration")
5. Click "Create"
6. Download the credentials JSON file
7. Save the file as `credentials.json` in the root directory of this project

### 5. Run the Setup Script

Run the setup script to authenticate with Google Calendar:

```bash
python setup_calendar_auth.py
```

This will:

1. Start the OAuth 2.0 authorization flow
2. Open your browser to authorize the application
3. Save the access token securely for future use
4. Test the connection to your Google Calendar

## 📅 Calendar Features

### Multiple Calendar Support

The Google Calendar integration supports working with multiple calendars:

1. **List all calendars**: "What calendars do I have access to?"
2. **Specify calendar by name**: "Create a meeting in my Work calendar"
3. **Default calendar**: Uses your primary calendar if none specified

### Voice Commands

Once set up, interact with your Google Calendar using natural language:

**Schedule Management:**

- *"What's on my calendar today?"*
- *"Show me my schedule for next week"*
- *"Find a free time slot for a 30-minute meeting tomorrow"*

**Event Creation:**

- *"Create a meeting with John tomorrow at 2 PM"*
- *"Schedule a doctor's appointment for next Friday at 10 AM"*
- *"Set up a team standup every Monday at 9 AM"*

**Event Modification:**

- *"Delete my 3 PM meeting today"*
- *"Reschedule my meeting with Sarah to Thursday at 11 AM"*
- *"Change the title of my dentist appointment to 'Dental Cleaning'"*

**Calendar Discovery:**

- *"Show me all my calendars"*
- *"What's on my Family calendar this weekend?"*

## 🚀 Running the Application

After completing the setup, start the voice assistant:

```bash
# Start the ADK Voice Assistant with hot-reloading
uvicorn main:app --reload
```

This starts the application server with your voice-enabled calendar assistant.

## 📁 Project Structure

```text
adk-voice-agent/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application entry point
│   └── jarvis/                 # Voice assistant implementation
│       ├── __init__.py
│       ├── agent.py            # Main ADK agent
│       ├── voice/              # Speech recognition/synthesis
│       └── tools/              # Calendar integration tools
├── credentials.json            # OAuth 2.0 credentials (create this)
├── setup_calendar_auth.py      # Authentication setup script
├── requirements.txt            # Python dependencies
└── README.md                  # This file
```

## 🐛 Troubleshooting

### Token Errors

If you encounter authentication errors:

1. Delete the token file at `~/.credentials/calendar_token.json`
2. Run `python setup_calendar_auth.py` again

### Permission Issues

If you need additional calendar permissions:

1. Delete the token file at `~/.credentials/calendar_token.json`
2. Edit the `SCOPES` variable in `app/jarvis/tools/calendar_utils.py`
3. Run the setup script again

### API Quota Issues

Google Calendar API has usage quotas. If you hit limits:

1. Check your [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to "APIs & Services" > "Dashboard"
3. Select "Google Calendar API"
4. View quota usage and consider upgrading if necessary

### Package Installation Issues

If you encounter package installation problems:

1. Ensure you're using Python 3.9 or newer
2. Upgrade pip: `pip install --upgrade pip`
3. Install packages individually if needed

### Audio Issues

For speech recognition problems:

1. Check microphone permissions
2. Test audio input/output devices
3. Verify `pyaudio` installation (may require system dependencies)

## 🔒 Security Considerations

- OAuth token is stored securely in your user directory
- Never share your `credentials.json` file or generated tokens
- Application requests minimum permissions needed for calendar operations
- All data processing happens locally on your machine

## 🔗 Navigation

- **[⬅️ Back to AI with Brandon Examples](../README.md)**
- **[🎬 Watch the ADK Tutorial](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s)**
- **[📚 Explore Other Examples](../)**

## 📖 Additional Resources

- **[Google Calendar API Documentation](https://developers.google.com/calendar)**
- **[Google ADK Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder)**
- **[Speech Recognition Library](https://pypi.org/project/SpeechRecognition/)**
- **[OAuth 2.0 for Desktop Apps](https://developers.google.com/identity/protocols/oauth2/native-app)**

## 🙏 Credits

Created by **[Brandon Hancock](https://github.com/bhancockio)** - Thank you for making voice-enabled ADK agents accessible!

## 🚀 Next Steps

- Explore the [ADK Crash Course](../_adk-crash-course/) for more agent patterns
- Try the [RAG Agent](../adk-rag-agent/) for document integration
- Build your own voice assistant with custom APIs

## 📄 License

Please refer to the original creator's licensing terms.

---

**Ready to build your voice assistant?** 🎤 Start by setting up your Google Cloud credentials above!
