# 🎨 YouTube Thumbnail Generator with ADK

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4.svg)](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder)
[![OpenAI](https://img.shields.io/badge/OpenAI-DALL--E-412991.svg)](https://openai.com/dall-e-2/)
[![YouTube](https://img.shields.io/badge/YouTube-Thumbnails-red.svg)](https://youtube.com)

> **🎥 Learn More**: Check out the [ADK Crash Course](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s) by Brandon Hancock for comprehensive ADK learning!

A powerful AI-powered system that generates professional YouTube thumbnails automatically using OpenAI's Image Generation API and Google's Agent Development Kit (ADK). Transform your YouTube content creation with intelligent thumbnail generation that mimics popular styles and engages viewers.

## 🌟 What You'll Learn

- **AI Image Generation**: Leverage OpenAI's DALL-E for professional thumbnail creation
- **Style Analysis**: Analyze and replicate successful thumbnail styles
- **Agent Workflows**: Build complex multi-step AI workflows with ADK
- **Content Creation**: Automate the thumbnail design process completely

## ✨ Features

- 🎨 **Style Cloning** - Analyze and replicate thumbnail styles from popular YouTube channels
- 🤖 **AI-Powered Generation** - Specialized AI agents handle the entire thumbnail creation process
- ⚡ **Automated Workflow** - From prompt generation to final image editing
- 💡 **No Design Skills Required** - Save hours of editing time with AI-generated thumbnails
- 🎯 **Engagement Optimization** - Generate thumbnails designed to maximize click-through rates
- 📊 **Style Analytics** - Understand what makes thumbnails successful

## 🚀 Quick Start

### Prerequisites

- **Python 3.9+**
- **OpenAI API Key** with DALL-E access
- **Google API Key** for Gemini
- Basic understanding of YouTube content creation

## ⚡ Installation

### 1. Set up Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows
.venv\Scripts\activate

# Activate on macOS/Linux
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root with your API keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_gemini_api_key_here
```

## 🔑 API Setup

### OpenAI API Key

1. Visit [OpenAI's platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to the [API keys section](https://platform.openai.com/api-keys)
4. Click "Create new secret key"
5. Copy the key and add it to your `.env` file

### Google Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click "Get API key"
4. Copy the key and add it to your `.env` file### YouTube API Key (Optional)

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

```env
YOUTUBE_API_KEY=your_youtube_api_key
```

## 🎯 Usage

### Run the Thumbnail Generator

Start the thumbnail generator agent:

```bash
python -m youtube_thumbnail_agent.agent
```

### Example Interactions

Once running, you can request thumbnails using natural language:

- *"Generate a thumbnail for my coding tutorial video"*
- *"Create a thumbnail in the style of MrBeast for a challenge video"*
- *"Make a professional thumbnail for a business presentation"*
- *"Generate a gaming thumbnail with bright colors and action"*

### Workflow Options

The agent can handle various thumbnail creation workflows:

1. **Style-Based Generation** - Specify a particular style or channel to emulate
2. **Content-Based Generation** - Describe your video content for contextual thumbnails
3. **Custom Prompts** - Provide detailed descriptions for specific design elements
4. **Batch Generation** - Create multiple thumbnail variations

## 🏗️ Architecture

The system uses a sophisticated multi-agent approach:

### Core Agents

| Agent | Purpose | Capabilities |
|-------|---------|--------------|
| **Style Analyzer** | Analyzes successful thumbnail patterns | Channel research, trend analysis |
| **Prompt Generator** | Creates tailored prompts for image generation | Content analysis, style translation |
| **Image Generator** | Interfaces with OpenAI's DALL-E API | High-quality image creation |
| **Image Editor** | Refines and optimizes generated images | Post-processing, optimization |

### Workflow Process

1. **Content Analysis** - Understand the video topic and target audience
2. **Style Research** - Analyze successful thumbnails in similar niches
3. **Prompt Engineering** - Generate optimized prompts for image creation
4. **Image Generation** - Create thumbnails using AI image generation
5. **Post-Processing** - Enhance and optimize the final thumbnails

## 🛠️ Advanced Features

### Style Cloning

- Analyze popular YouTube channels for thumbnail patterns
- Extract common design elements and color schemes
- Replicate successful visual strategies

### Content Optimization

- Generate thumbnails optimized for click-through rates
- Adapt designs for different video categories
- Create A/B testing variations

### Batch Processing

- Generate multiple thumbnail options simultaneously
- Create variations with different styles and layouts
- Export in various sizes and formats

## 📁 Project Structure

```text
youtube-thumbnail-agent/
├── youtube_thumbnail_agent/
│   ├── __init__.py
│   ├── agent.py            # Main thumbnail generation agent
│   ├── agents/             # Individual agent implementations
│   │   ├── style_analyzer.py
│   │   ├── prompt_generator.py
│   │   ├── image_generator.py
│   │   └── image_editor.py
│   └── tools/              # Utility tools and helpers
├── .env                    # Environment variables (create this)
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 💡 Tips for Best Results

### Content Preparation

- Provide clear, descriptive video titles
- Include target audience information
- Specify the video category or niche

### Style Guidance

- Reference successful channels in your niche
- Describe preferred color schemes
- Mention any specific visual elements needed

### Iteration Strategy

- Generate multiple variations
- Test different styles and approaches
- Refine prompts based on results

## 🐛 Troubleshooting

### API Issues

- Verify all API keys are correctly set in `.env`
- Check API quota limits and usage
- Ensure billing is enabled for OpenAI account

### Image Quality

- Experiment with different prompt styles
- Try multiple generation attempts
- Adjust image resolution settings

### Style Inconsistency

- Provide more specific style references
- Use consistent color and design terminology
- Include example images or channel references

## 🔗 Navigation

- **[⬅️ Back to AI with Brandon Examples](../README.md)**
- **[🎬 Watch the ADK Tutorial](https://www.youtube.com/watch?v=P4VFL9nIaIA&t=9496s)**
- **[📚 Explore Other Examples](../)**

## 📖 Additional Resources

- **[OpenAI DALL-E Documentation](https://platform.openai.com/docs/guides/images)**
- **[YouTube Creator Academy](https://creatoracademy.youtube.com/)**
- **[Google ADK Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder)**
- **[Thumbnail Design Best Practices](https://support.google.com/youtube/answer/72431)**

## 🙏 Credits

Created by **[Brandon Hancock](https://github.com/bhancockio)** - Thank you for making AI-powered content creation accessible!

## 🚀 Next Steps

- Explore the [ADK Crash Course](../_adk-crash-course/) for more agent patterns
- Try the [Voice Agent](../adk-voice-agent/) for speech-enabled interactions
- Build your own creative AI agents with custom workflows

## 📄 License

Please refer to the original creator's licensing terms.

---

**Ready to revolutionize your thumbnail creation?** 🎨 Start by setting up your API keys above!

