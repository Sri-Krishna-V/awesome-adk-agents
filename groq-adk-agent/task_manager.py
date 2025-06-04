from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
import os
from dotenv import load_dotenv
import asyncio
from typing import Dict, Any
import json

load_dotenv()


class GroqTaskManager:
    """Task manager for coordinating multiple Groq compound agents"""

    def __init__(self):
        self.session_service = InMemorySessionService()
        self.agents = self._initialize_agents()
        self.runners = self._initialize_runners()

    def _initialize_agents(self) -> Dict[str, Agent]:
        """Initialize different Groq agents for various tasks"""

        base_config = {
            "api_key": os.getenv("GROQ_API_KEY"),
            "api_base": "https://api.groq.com/openai/v1"
        }

        return {
            "research": Agent(
                name="research_specialist",
                model=LiteLlm(model="groq/compound-beta", **base_config),
                description="Deep research specialist with web search and analysis",
                instruction="""You specialize in comprehensive research tasks.
                Use web search to gather current information and code execution for analysis.
                Provide detailed, well-sourced research reports."""
            ),

            "calculator": Agent(
                name="calculation_specialist",
                model=LiteLlm(model="groq/compound-beta-mini", **base_config),
                description="Fast calculation and data processing specialist",
                instruction="""You specialize in calculations, data analysis, and code execution.
                Solve mathematical problems, process data, and perform computations efficiently."""
            ),

            "web_searcher": Agent(
                name="web_search_specialist",
                model=LiteLlm(model="groq/compound-beta-mini", **base_config),
                description="Current information and web search specialist",
                instruction="""You specialize in finding current information on the web.
                Search for the most recent and relevant information on any topic."""
            ),

            "coordinator": Agent(
                name="task_coordinator",
                model=LiteLlm(model="groq/compound-beta", **base_config),
                description="Coordinates complex multi-step tasks across specialists",
                instruction="""You coordinate complex tasks that may require multiple specialists.
                Break down complex requests and orchestrate the appropriate specialists.
                Synthesize results into comprehensive responses."""
            )
        }

    def _initialize_runners(self) -> Dict[str, Runner]:
        """Initialize runners for each agent"""
        return {
            name: Runner(
                agent=agent,
                app_name=f"groq_{name}_app",
                session_service=self.session_service
            )
            for name, agent in self.agents.items()
        }

    async def handle_research_task(self, query: str, user_id: str = "default") -> str:
        """Handle research-focused tasks"""
        session_id = f"research_{user_id}"

        response = await self.runners["research"].run_async(
            user_id=user_id,
            session_id=session_id,
            message=f"Research this topic comprehensively: {query}"
        )
        return response.content

    async def handle_calculation_task(self, query: str, user_id: str = "default") -> str:
        """Handle calculation and analysis tasks"""
        session_id = f"calc_{user_id}"

        response = await self.runners["calculator"].run_async(
            user_id=user_id,
            session_id=session_id,
            message=f"Solve this calculation or analysis task: {query}"
        )
        return response.content

    async def handle_web_search_task(self, query: str, user_id: str = "default") -> str:
        """Handle web search tasks"""
        session_id = f"search_{user_id}"

        response = await self.runners["web_searcher"].run_async(
            user_id=user_id,
            session_id=session_id,
            message=f"Find current information about: {query}"
        )
        return response.content

    async def handle_complex_task(self, query: str, user_id: str = "default") -> str:
        """Handle complex multi-step tasks"""
        session_id = f"complex_{user_id}"

        response = await self.runners["coordinator"].run_async(
            user_id=user_id,
            session_id=session_id,
            message=f"Handle this complex task: {query}"
        )
        return response.content

    def route_task(self, query: str) -> str:
        """Route tasks to appropriate handlers based on query content"""
        query_lower = query.lower()

        if any(keyword in query_lower for keyword in ["calculate", "math", "compute", "analyze data"]):
            return "calculation"
        elif any(keyword in query_lower for keyword in ["current", "latest", "news", "recent", "today"]):
            return "web_search"
        elif any(keyword in query_lower for keyword in ["research", "study", "investigate", "analyze"]):
            return "research"
        else:
            return "complex"


# Task manager instance
task_manager = GroqTaskManager()
