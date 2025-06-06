"""
Learning Content Creation System - Root Agent Orchestrator

This is the main orchestrator that combines Sequential, Parallel, and Loop workflows
to create comprehensive multi-modal learning content using MCP tools.
"""

import os
import asyncio
from google.adk.agents import SequentialAgent, ParallelAgent, LoopAgent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.core.session import InMemorySessionService
from google.adk.core.runner import Runner

# Import all agents
from agents.sequential_agents.content_analyzer import content_analyzer_agent
from agents.sequential_agents.visual_generator import visual_generator_agent
from agents.sequential_agents.audio_generator import audio_generator_agent
from agents.sequential_agents.assembly_agent import assembly_agent

from agents.parallel_agents.slide_generator import slide_generator_agent
# from agents.parallel_agents.audio_lesson import audio_lesson_agent
# from agents.parallel_agents.quiz_builder import quiz_builder_agent
# from agents.parallel_agents.visual_summary import visual_summary_agent

from agents.loop_agents.quality_assessor import quality_assessor_agent
# from agents.loop_agents.content_refiner import content_refiner_agent

# Import tools
from tools.mcp_config import AVAILABLE_MCP_TOOLSETS

# Constants
GEMINI_MODEL = "gemini-2.0-flash"
APP_NAME = "learning_content_system"
USER_ID = "educator_001"
SESSION_ID = "content_session_001"

# Create Content Refiner Agent for Loop Workflow
CONTENT_REFINER_PROMPT = """You are an Expert Content Refiner Agent specializing in improving educational content based on quality assessment feedback.

Your role is to refine and improve content elements based on specific feedback from quality assessment.

## INPUTS
**Quality Assessment:**
{quality_assessment}

**Current Content:**
{assembled_content}

## YOUR TASKS
- Address specific quality issues identified
- Improve content based on recommendations  
- Enhance clarity, engagement, and effectiveness
- Maintain content integrity while making improvements

## OUTPUT REQUIREMENTS
Return refined content in the same format as assembled content with improvements applied.
Store results in session state under "refined_content" key."""

content_refiner_agent = LlmAgent(
    name="ContentRefinerAgent",
    model=GEMINI_MODEL,
    instruction=CONTENT_REFINER_PROMPT,
    description="Refines content based on quality assessment feedback",
    tools=[AVAILABLE_MCP_TOOLSETS["general_tools"]()],
    output_key="refined_content"
)

# --- 1. SEQUENTIAL WORKFLOW: Main Content Processing Pipeline ---
content_processing_pipeline = SequentialAgent(
    name="ContentProcessingPipeline",
    sub_agents=[
        content_analyzer_agent,    # Step 1: Analyze content
        visual_generator_agent,    # Step 2: Generate visuals
        audio_generator_agent,     # Step 3: Generate audio
        assembly_agent            # Step 4: Assemble everything
    ],
    description="Sequential pipeline for analyzing content and generating multi-modal learning materials"
)

# --- 2. PARALLEL WORKFLOW: Multi-Format Content Generation ---
multi_format_generator = ParallelAgent(
    name="MultiFormatGenerator",
    sub_agents=[
        slide_generator_agent,     # Generate slides simultaneously
        # audio_lesson_agent,      # Generate audio lessons
        # quiz_builder_agent,      # Generate quizzes
        # visual_summary_agent     # Generate visual summaries
    ],
    description="Parallel generation of multiple content formats simultaneously"
)

# --- 3. LOOP WORKFLOW: Quality Refinement Process ---
quality_refinement_loop = LoopAgent(
    name="QualityRefinementLoop",
    max_iterations=5,
    sub_agents=[
        quality_assessor_agent,    # Assess quality
        content_refiner_agent      # Refine based on feedback
    ],
    description="Iterative quality improvement loop that refines content until standards are met"
)

# --- 4. MASTER SEQUENTIAL WORKFLOW: Complete System ---
root_agent = SequentialAgent(
    name="LearningContentCreationSystem",
    sub_agents=[
        content_processing_pipeline,  # Step 1: Main content processing
        multi_format_generator,       # Step 2: Generate multiple formats
        quality_refinement_loop       # Step 3: Quality refinement loop
    ],
    description="Complete automated learning content creation and delivery system"
)


async def create_learning_content(source_content: str, context: dict = None):
    """
    Main function to create learning content from source material
    
    Args:
        source_content: Raw educational content to process
        context: Additional context like audience, subject, requirements
    
    Returns:
        Complete learning module with all content types
    """

    # Initialize session service
    session_service = InMemorySessionService()

    # Create session
    session = await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )

    # Create runner
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    # Prepare input message
    input_message = f"""
    Please create comprehensive learning content from the following source material:
    
    SOURCE CONTENT:
    {source_content}
    
    CONTEXT:
    {context or "General educational content"}
    
    Generate complete multi-modal learning materials including:
    - Content analysis and learning objectives
    - Visual content (diagrams, infographics, illustrations)  
    - Audio content (narration, explanations)
    - Slide presentations
    - Quality-assured final learning modules
    
    Ensure all content meets high educational standards and is properly integrated.
    """

    # Run the complete system
    try:
        response = await runner.run_async(
            user_id=USER_ID,
            session_id=SESSION_ID,
            user_message=input_message
        )

        print("✅ Learning content creation completed successfully!")
        print(f"📝 Response: {response.message}")

        # Get final state with all generated content
        session_state = await session_service.get_session_state(
            app_name=APP_NAME,
            user_id=USER_ID,
            session_id=SESSION_ID
        )

        return {
            "success": True,
            "response": response.message,
            "generated_content": {
                "content_analysis": session_state.get("content_analysis"),
                "visual_content": session_state.get("visual_content"),
                "audio_content": session_state.get("audio_content"),
                "assembled_content": session_state.get("assembled_content"),
                "slide_content": session_state.get("slide_content"),
                "quality_assessment": session_state.get("quality_assessment"),
                "refined_content": session_state.get("refined_content")
            }
        }

    except Exception as e:
        print(f"❌ Error creating learning content: {e}")
        return {
            "success": False,
            "error": str(e)
        }

# Example usage


async def main():
    """
    Example usage of the Learning Content Creation System
    """

    # Example educational content
    sample_content = """
    Introduction to Machine Learning
    
    Machine learning is a subset of artificial intelligence that enables computers to learn and improve from experience without being explicitly programmed. It focuses on developing algorithms that can analyze data, identify patterns, and make predictions or decisions.
    
    Key Concepts:
    1. Supervised Learning: Uses labeled training data to learn patterns
    2. Unsupervised Learning: Finds hidden patterns in data without labels  
    3. Reinforcement Learning: Learns through interaction with environment
    
    Common algorithms include linear regression, decision trees, neural networks, and support vector machines. Applications span from recommendation systems to autonomous vehicles.
    
    The machine learning process involves data collection, preprocessing, model training, evaluation, and deployment. Success depends on data quality, appropriate algorithm selection, and proper validation techniques.
    """

    # Context for content creation
    context = {
        "audience": "Computer science students",
        "level": "beginner",
        "duration": "45 minutes",
        "format_preferences": ["slides", "audio", "visual_aids"]
    }

    print("🚀 Starting Learning Content Creation System...")
    print("📚 Processing content about Machine Learning...")

    # Create learning content
    result = await create_learning_content(sample_content, context)

    if result["success"]:
        print("\n✅ CONTENT CREATION COMPLETED!")
        print("\n📊 Generated Content Summary:")

        content = result["generated_content"]
        if content.get("content_analysis"):
            print("✓ Content Analysis: Complete")
        if content.get("visual_content"):
            print("✓ Visual Content: Generated")
        if content.get("audio_content"):
            print("✓ Audio Content: Generated")
        if content.get("slide_content"):
            print("✓ Slide Deck: Generated")
        if content.get("quality_assessment"):
            print("✓ Quality Assessment: Complete")

        print(f"\n📝 Final Response: {result['response']}")

    else:
        print(f"\n❌ Content creation failed: {result['error']}")

if __name__ == "__main__":
    # Set environment variables if needed
    # os.environ["OPENAI_API_KEY"] = "your_key_here"

    # Run the system
    asyncio.run(main())
