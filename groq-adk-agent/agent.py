from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq Research Agent with compound-beta model
groq_research_agent = Agent(
    name="groq_research_agent",
    model=LiteLlm(
        model="groq/llama-3.3-70b-versatile",  # Fallback model
        api_key=os.getenv("GROQ_API_KEY"),
        api_base="https://api.groq.com/openai/v1"
    ),
    description="Advanced research agent powered by Groq's compound AI system with web search and code execution",
    instruction="""You are an advanced research assistant powered by Groq's compound AI system. 
    You have access to real-time web search and code execution capabilities that are handled automatically.
    
    Your capabilities include:
    - Searching the web for current information
    - Performing calculations and data analysis
    - Running code to solve problems
    - Providing comprehensive research and analysis
    
    When users ask questions:
    1. For current information needs - search the web automatically
    2. For calculations or data analysis - execute code as needed
    3. For research tasks - combine web search with analysis
    4. Always provide accurate, well-sourced, and comprehensive responses
    
    Be proactive in using your tools when they would enhance your response."""
)

# Alternative agent using compound-beta directly
groq_compound_agent = Agent(
    name="groq_compound_agent",
    model=LiteLlm(
        model="groq/compound-beta",  # Using compound-beta directly
        api_key=os.getenv("GROQ_API_KEY"),
        api_base="https://api.groq.com/openai/v1"
    ),
    description="Groq compound AI agent with server-side tool orchestration",
    instruction="""You are a compound AI assistant with built-in web search and code execution.
    Your tools are automatically orchestrated server-side by Groq's compound system.
    
    For any query that requires:
    - Current information: Web search will be automatically triggered
    - Calculations: Code execution will be automatically used
    - Data analysis: Both tools may be used as needed
    
    Provide comprehensive, accurate responses leveraging your automated tool capabilities."""
)

# Lightweight agent using compound-beta-mini
groq_mini_agent = Agent(
    name="groq_mini_agent",
    model=LiteLlm(
        model="groq/compound-beta-mini",  # Using compound-beta-mini
        api_key=os.getenv("GROQ_API_KEY"),
        api_base="https://api.groq.com/openai/v1"
    ),
    description="Fast Groq compound AI agent optimized for single tool calls",
    instruction="""You are a fast compound AI assistant optimized for quick responses.
    You can use one tool per request (either web search OR code execution).
    
    Choose the most appropriate tool based on the user's request:
    - Web search for current information needs
    - Code execution for calculations and data processing
    
    Provide fast, accurate responses with the selected tool."""
)

# Session service for state management
session_service = InMemorySessionService()

# Runners for each agent
research_runner = Runner(
    agent=groq_research_agent,
    app_name="groq_research_app",
    session_service=session_service
)

compound_runner = Runner(
    agent=groq_compound_agent,
    app_name="groq_compound_app",
    session_service=session_service
)

mini_runner = Runner(
    agent=groq_mini_agent,
    app_name="groq_mini_app",
    session_service=session_service
)

# Default agent for ADK web interface
agent = groq_compound_agent  # This will be picked up by ADK web
