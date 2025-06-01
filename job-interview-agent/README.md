# Job Interview Roleplay Agent 🎯

 A powerful multi-job Interview coaching AI agent built with Google's Agent Development Kit (ADK). To practice realistic interviews with **natural voice conversations**, real-time feedback, and progress tracking.

## Key Features

### Natural Voice Interaction

- **Real-time voice conversations** with WebSocket streaming
- **Automatic transcription** and intelligent responses
- **Natural conversation flow** with interruption handling
- **Voice + text mode** support

### Interview Types

- **Behavioral**: STAR method coaching, experience-based questions
- **Technical**: Coding challenges, system design discussions
- **Role-specific**: Tailored questions for different positions
- **Real-time feedback** with detailed scoring and recommendations

### Smart Features

- Google Calendar integration for scheduling
- Progress analytics and performance tracking
- Custom question banks and scoring criteria
- Session history and improvement recommendations

## Quick Start

### Prerequisites

- Python 3.8 or newer
- Microphone and speakers for voice interaction
- Google account (for Calendar integration - optional)

### 1. Setup Project

```bash
# Navigate to the job interview agent directory
cd job-interview-agent

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### 2. Setup Gemini API Key

1. Create or use an existing [Google AI Studio](https://aistudio.google.com/) account
2. Get your Gemini API key from the [API Keys section](https://aistudio.google.com/app/apikeys)
3. Create a `.env` file in the project root:

```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 3. Setup Google Calendar Integration (Optional)

#### Create Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Calendar API:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Google Calendar API" and enable it

#### Create OAuth 2.0 Credentials

1. In Google Cloud Console, go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth client ID"
3. Select "Desktop application" as application type
4. Name it "Job Interview Agent Calendar"
5. Download the credentials JSON file
6. Save as `credentials.json` in the project root

#### Run Calendar Setup

```bash
# Authenticate with Google Calendar
python setup_calendar_auth.py
```

This will:

- Open your browser for OAuth authorization
- Save access token securely
- Test calendar connection
- Grant access to schedule interview practice sessions

### 4. Start the Agent

```bash
# Navigate to app directory
cd app

# Start the server
python main.py

# Start hot-reloading server
uvicorn main:app --reload --host
```

### 5. Start Practicing 🎙️

Open your browser and go to: **`http://localhost:8000`**

Click the microphone icon and say:
> **"Hi, I'd like to practice for a software engineer interview"**

Or try calendar commands:
> **"Schedule a practice interview for tomorrow at 3 PM"**

That's it! You're now ready for voice-powered interview practice with calendar scheduling.

## Voice Interview Examples

### Product Manager Interview

```text
You: "Hi, I'd like to practice behavioral questions for a product manager role"

Agent: "Excellent! Let's start with a leadership scenario. Tell me about a time when you had to influence a team without having direct authority over them."

You: "Well, in my previous role as a senior analyst..."

Agent: [Real-time feedback] "Great start! I can hear you're structuring this well using the STAR method. Please continue with the specific actions you took..."
```

### Entry-Level Software Developer

```text
You: "I'm preparing for my first software developer interviews. Can you help me practice?"

Agent: "Absolutely! Since you're starting your career, I'll focus on projects and learning potential. Tell me about a challenging coding project from your studies."

You: "During my final semester, I built a web application..."

Agent: "Excellent example! Walk me through the specific technical challenges and your problem-solving approach."
```

### Data Analyst Interview

```text
You: "I want to practice data analyst questions with both technical and behavioral aspects."

Agent: "Perfect! Here's a scenario: You're given a dataset with missing values and outliers. Walk me through your data cleaning approach."

You: "I'd start by exploring the dataset using Python pandas..."

Agent: "Great systematic approach! Can you discuss how you'd validate your decisions and communicate findings to stakeholders?"
```

### Sales Representative Practice

```text
You: "I need to practice sales interviews with objection handling scenarios."

Agent: "Let's do a role-play. I'm a client who says: 'Your product seems too expensive.' How do you handle this?"

You: "I understand price is a consideration. Can you help me understand what value you're looking for..."

Agent: [As client] "I need CRM integration..." [Then feedback] "Excellent! You asked discovery questions instead of being defensive."
```

## Available Commands

### Voice Interaction

- **"Start voice mode"** - Enable real-time conversation
- **"Switch to text mode"** - Change interaction method
- Natural conversation flow with interruption handling

### Interview Sessions

- `"Start a [type] interview for [role]"` - Begin session
- `"Ask me a [category] question"` - Get specific questions
- `"Provide feedback on my answer"` - Get detailed analysis
- `"End interview session"` - Complete and save session

### Calendar & Analytics

- `"Schedule interview for [date/time]"` - Book practice session
- `"Show my progress over time"` - View performance trends
- `"Generate interview report"` - Get detailed analysis
- `"What should I improve?"` - Get recommendations

## Configuration

### Custom Question Banks

```json
{
  "behavioral": {
    "leadership": [{
      "question": "Describe leading a challenging project",
      "follow_up": "What would you do differently?",
      "difficulty": "medium"
    }]
  }
}
```

### Interview Scoring

```json
{
  "behavioral": {
    "scoring_criteria": ["structure", "specificity", "outcome", "reflection"],
    "duration_minutes": 45
  }
}
```

## Advanced Features

- **Multi-modal feedback**: Voice + visual responses
- **Session persistence**: Complete conversation history
- **Performance analytics**: Trends and improvement areas
- **Calendar intelligence**: Smart scheduling with prep tips
- **Adaptive questioning**: Adjusts based on experience level

## Docker Deployment

```bash
docker build -t job-interview-agent .
docker run -it --env-file .env job-interview-agent
```

## Troubleshooting

**Voice Issues**: Check microphone permissions, use quiet environment
**Calendar Errors**: Delete `~/.credentials/calendar_token.json` and re-run setup
**API Quota**: Monitor usage in Google Cloud Console
**Connection Issues**: Ensure port 8000 is available, try `localhost:8000`

## Support

- [ADK Documentation](https://google.github.io/adk-docs/)
- [Report Issues](https://github.com/awesome-adk-agents/issues)

---

**Practice makes perfect! Start your voice interview now at `localhost:8000`**
