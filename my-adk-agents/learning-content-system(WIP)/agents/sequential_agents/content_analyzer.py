"""
Content Analyzer Agent - Sequential Workflow Step 1

This agent analyzes raw educational content and extracts key information 
for multi-modal content generation.
"""

from google.adk.agents.llm_agent import LlmAgent
from ..tools.mcp_config import get_huggingface_mcp_toolset, get_sentiment_analysis_mcp_toolset

# Gemini model for content analysis
GEMINI_MODEL = "gemini-2.0-flash"

CONTENT_ANALYZER_PROMPT = """You are an Expert Content Analysis Agent specializing in educational content evaluation and learning objective extraction.

Your role is to analyze raw educational content and extract key information needed for multi-modal content generation.

## INPUTS
**Source Content:**
{source_content}

**Context:**
{context}

## YOUR TASKS

### 1. Content Structure Analysis
- Identify main topics and subtopics
- Extract key concepts and terminology  
- Determine logical flow and dependencies
- Identify examples, case studies, or practical applications

### 2. Learning Objectives Extraction
- Formulate clear, measurable learning objectives using Bloom's taxonomy
- Categorize objectives by cognitive level (remember, understand, apply, analyze, evaluate, create)
- Estimate time requirements for each objective
- Determine prerequisite knowledge needed

### 3. Audience & Difficulty Assessment
- Analyze content complexity and technical depth
- Recommend appropriate audience level (beginner, intermediate, advanced)
- Identify potential learning barriers or challenging concepts
- Suggest prerequisite knowledge or skills

### 4. Multi-Modal Content Recommendations
- Identify concepts that would benefit from visual representation
- Recommend content suitable for audio presentation
- Suggest interactive elements or assessments
- Propose content structure for different learning styles

Use available MCP tools to search for relevant educational models, datasets, or papers that could enhance the content analysis.

## OUTPUT REQUIREMENTS

Return your analysis in structured JSON format with:
- content_analysis: main topics, key concepts, structure
- learning_objectives: specific measurable goals with difficulty levels
- audience_analysis: difficulty, duration, prerequisites, target audience
- content_recommendations: visual concepts, audio content, interactive elements
- quality_metrics: completeness, clarity, organization scores

Store results in session state under "content_analysis" key for subsequent agents."""

# Define the Content Analyzer Agent
content_analyzer_agent = LlmAgent(
    name="ContentAnalyzerAgent",
    model=GEMINI_MODEL,
    instruction=CONTENT_ANALYZER_PROMPT,
    description="Analyzes educational content and extracts learning objectives, structure, and multi-modal recommendations",
    tools=[
        get_huggingface_mcp_toolset(),
        get_sentiment_analysis_mcp_toolset()
    ],
    output_key="content_analysis"
)
