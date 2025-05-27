from typing import Dict

from google.adk.tools.tool_context import ToolContext


def select_thumbnail(
    tool_context: ToolContext,
    thumbnail_filename: str,
) -> Dict:
    """
    Select a thumbnail for analysis by setting it in state.

    Args:
        tool_context: ADK tool context
        thumbnail_filename: The filename of the thumbnail to analyze

    Returns:
        Dictionary with selection status
    """
    try:
        if not thumbnail_filename:
            return {"status": "error", "message": "No thumbnail filename provided."}

        # Verify thumbnail_analysis exists in state
        if "thumbnail_analysis" not in tool_context.state:
            return {
                "status": "error",
                "message": "thumbnail_analysis not found in state. Cannot select thumbnail.",
            }

        # Check if the thumbnail exists in the analysis dictionary
        if thumbnail_filename not in tool_context.state["thumbnail_analysis"]:
            return {
                "status": "error",
                "message": f"Thumbnail {thumbnail_filename} not found in thumbnail_analysis state.",
            }

        # Check if this thumbnail has already been analyzed
        if tool_context.state["thumbnail_analysis"][thumbnail_filename]:
            return {
                "status": "warning",
                "message": f"Thumbnail {thumbnail_filename} has already been analyzed. You should select a different one.",
            }

        # Set the thumbnail to analyze in state
        tool_context.state["thumbnail_to_analyze"] = thumbnail_filename

        # Return success
        return {
            "status": "success",
            "message": f"Selected {thumbnail_filename} for analysis.",
            "thumbnail": thumbnail_filename,
        }

    except Exception as e:
        error_message = f"Error selecting thumbnail: {str(e)}"
        print(error_message)
        return {"status": "error", "message": error_message}
