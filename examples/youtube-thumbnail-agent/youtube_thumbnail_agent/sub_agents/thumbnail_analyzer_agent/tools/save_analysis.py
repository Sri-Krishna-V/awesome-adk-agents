from typing import Dict

from google.adk.tools.tool_context import ToolContext


def save_analysis(
    thumbnail_filename: str,
    analysis: str,
    tool_context: ToolContext,
) -> Dict:
    """
    Save the analysis for a specific thumbnail to state.

    Args:
        thumbnail_filename: The filename of the analyzed thumbnail
        analysis: The detailed analysis text for the thumbnail
        tool_context: ADK tool context

    Returns:
        Dictionary with save status
    """
    try:
        print(f"Saving analysis for {thumbnail_filename}")
        if not thumbnail_filename:
            return {"status": "error", "message": "No thumbnail filename provided."}

        if not analysis:
            return {
                "status": "error",
                "message": "No analysis text provided. Analysis must be non-empty.",
            }

        # Ensure thumbnail_analysis exists in state
        if "thumbnail_analysis" not in tool_context.state:
            tool_context.state["thumbnail_analysis"] = {}

        # Check if the thumbnail is already in the dictionary
        if thumbnail_filename not in tool_context.state["thumbnail_analysis"]:
            # If not, add it - this shouldn't normally happen since thumbnails are pre-initialized
            # but this provides a safety mechanism
            tool_context.state["thumbnail_analysis"][thumbnail_filename] = ""

        # Save the analysis
        tool_context.state["thumbnail_analysis"][thumbnail_filename] = analysis

        # Return success
        return {
            "status": "success",
            "message": f"Analysis for {thumbnail_filename} saved successfully.",
            "thumbnail": thumbnail_filename,
            "analysis_length": len(analysis),
        }

    except Exception as e:
        error_message = f"Error saving analysis: {str(e)}"
        print(error_message)
        return {"status": "error", "message": error_message}
