"""
Main agent module for the Job Interview Roleplay Agent.

This agent provides comprehensive interview simulation capabilities including:
- Behavioral interview questions
- Technical interview scenarios
- Interview scheduling with calendar integration
- Real-time feedback and scoring
- Multi-role interview simulations (HR, Technical Lead, etc.)
"""

from google.adk.agents import Agent
from .tools import (
    schedule_interview,
    list_scheduled_interviews,
    cancel_interview,
    update_interview,
    start_interview_session,
    ask_behavioral_question,
    ask_technical_question,
    provide_feedback,
    evaluate_answer,
    generate_interview_report,
    get_question_bank,
    save_interview_progress,
    load_interview_progress,
)
from .prompts import GLOBAL_INSTRUCTION, MAIN_INSTRUCTION
from .utils import get_current_time


root_agent = Agent(
    name="job_interview_agent",
    model="gemini-2.0-flash-live-001",
    description="Comprehensive job interview roleplay agent with calendar integration and multi-scenario support.",
    global_instruction=GLOBAL_INSTRUCTION,
    instruction=MAIN_INSTRUCTION.format(current_time=get_current_time()),
    tools=[
        # Calendar and scheduling tools
        schedule_interview,
        list_scheduled_interviews,
        cancel_interview,
        update_interview,

        # Interview session tools
        start_interview_session,
        ask_behavioral_question,
        ask_technical_question,
        provide_feedback,
        evaluate_answer,

        # Data and reporting tools
        generate_interview_report,
        get_question_bank,
        save_interview_progress,
        load_interview_progress,
    ],
)
