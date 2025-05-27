"""
LinkedIn Final Post Generator Agent

This agent generates the final LinkedIn post after refinement and review.
"""

from google.adk.agents.llm_agent import LlmAgent

GEMINI_MODEL = "gemini-2.0-flash"

final_post_generator = LlmAgent(
    name = "FinalPostGenerator",
    model = GEMINI_MODEL,
    instruction = """You are a LinkedIn Final Post Generator.
    Your task is to provide the final LinkedIn post output after refinement and review.
    
    #OUTPUT INSTRUCTIONS
    - Return ONLY the final post content
    - Do not add formatting markers or explanations

    #FORMAT
    The final post:
    {current_post}
    
    """
    ,
    description = "Generates the final LinkedIn post after all refinements and reviews",
    output_key = "final_post",
)