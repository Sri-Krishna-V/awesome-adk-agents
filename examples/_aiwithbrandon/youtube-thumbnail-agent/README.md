# YouTube Thumbnail Generator with Agent Development Kit (ADK)

A powerful AI-powered system that generates professional YouTube thumbnails automatically using OpenAI's Image Generation API and Google's Agent Development Kit (ADK).

## Features

- **Style Cloning**: Analyze and replicate thumbnail styles from popular YouTube channels
- **AI-Powered Generation**: Specialized AI agents handle the entire thumbnail creation process
- **Automated Workflow**: From prompt generation to final image editing
- **No Design Skills Required**: Save hours of editing time with AI-generated thumbnails

## Installation

1. Clone this repository
```bash
git clone https://github.com/yourusername/adk-yt-thumbnail-generator.git
cd adk-yt-thumbnail-generator
```

2. Set up a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables by creating a `.env` file with your API keys (see API Setup section below)

## API Setup

### OpenAI API Key
1. Visit [OpenAI's platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to the [API keys section](https://platform.openai.com/api-keys)
4. Click "Create new secret key"
5. Copy the key and add it to your `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

### Google Gemini API Key
1. Visit the [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API key" 
4. Copy the key and add it to your `.env` file:
   ```
   GOOGLE_API_KEY=your_gemini_api_key
   ```

### YouTube API Key
1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select an existing one)
3. Enable the YouTube Data API v3:
   - Navigate to "APIs & Services" > "Library"
   - Search for "YouTube Data API v3"
   - Click "Enable"
4. Create credentials:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "API Key"
5. Copy the key and add it to your `.env` file:
   ```
   YOUTUBE_API_KEY=your_youtube_api_key
   ```

## Usage

Run the thumbnail generator agent:
```bash
python -m youtube_thumbnail_agent.agent
```

## Architecture

The system uses a multi-agent approach:
- **Prompt Generator**: Creates tailored prompts for image generation
- **Image Generator**: Interfaces with OpenAI's API to create thumbnail images
- **Image Editor**: Refines and adjusts the generated images for optimal results

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

