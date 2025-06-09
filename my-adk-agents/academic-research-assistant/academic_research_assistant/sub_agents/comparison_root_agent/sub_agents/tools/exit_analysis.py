from typing import Dict

from google.adk.tools.tool_context import ToolContext


def exit_analysis(
    tool_context: ToolContext,
) -> Dict:
    """
    Exit the analysis refinement loop when a satisfactory analysis has been approved.

    This function signals to the loop agent that the analysis has been satisfactorily
    reviewed and approved by the critic agent, and no further refinement is needed.

    Args:
        tool_context: ADK tool context

    Returns:
        Dictionary with exit status
    """
    tool_context.actions.escalate = True

    return {
        "status": "success",
        "message": "Analysis has been approved. Exiting refinement loop.",
    }
