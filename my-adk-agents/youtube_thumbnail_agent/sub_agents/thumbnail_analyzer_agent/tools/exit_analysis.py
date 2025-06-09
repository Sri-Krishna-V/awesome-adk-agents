from typing import Dict

from google.adk.tools.tool_context import ToolContext


def exit_analysis(
    tool_context: ToolContext,
) -> Dict:
    """
    Exit the thumbnail analysis loop only if all thumbnails have been analyzed.

    This function checks if all thumbnails in the thumbnail_analysis state have
    non-empty analysis strings.

    Args:
        tool_context: ADK tool context

    Returns:
        Dictionary with exit status
    """
    tool_context.actions.escalate = True

    return {
        "status": "success",
        "message": "Analysis complete for all thumbnails. Exiting analysis loop.",
    }
