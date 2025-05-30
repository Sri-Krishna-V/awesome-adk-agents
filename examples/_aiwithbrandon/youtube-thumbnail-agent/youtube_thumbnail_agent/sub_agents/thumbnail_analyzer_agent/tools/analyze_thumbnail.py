import os
import os.path
from typing import Dict

import google.genai.types as types
from google.adk.tools.tool_context import ToolContext

from ....constants import REFERENCE_IMAGES_DIR


def analyze_thumbnail(
    tool_context: ToolContext,
    thumbnail_filename: str,
) -> Dict:
    """
    Load a thumbnail image as an artifact for the multimodal model to analyze.

    Args:
        tool_context: ADK tool context
        thumbnail_filename: The filename of the thumbnail to analyze

    Returns:
        Dictionary with the thumbnail image as an artifact
    """
    try:
        # Verify the thumbnail exists
        thumbnail_path = os.path.join(REFERENCE_IMAGES_DIR, thumbnail_filename)
        if not os.path.exists(thumbnail_path):
            return {
                "status": "error",
                "message": f"Thumbnail file not found: {thumbnail_filename}",
            }

        # Verify thumbnail_analysis exists in state
        if "thumbnail_analysis" not in tool_context.state:
            # If not, create it with an empty entry for this thumbnail
            tool_context.state["thumbnail_analysis"] = {thumbnail_filename: ""}
        elif thumbnail_filename not in tool_context.state["thumbnail_analysis"]:
            # If thumbnail isn't in the dictionary, add it
            tool_context.state["thumbnail_analysis"][thumbnail_filename] = ""

        # Read the image file
        with open(thumbnail_path, "rb") as f:
            image_bytes = f.read()

        # Create a Part object for the artifact
        image_artifact = types.Part(
            inline_data=types.Blob(data=image_bytes, mime_type="image/jpeg")
        )

        # Save as an artifact if tool_context is provided
        artifact_version = None
        try:
            # Save the artifact
            artifact_version = tool_context.save_artifact(
                filename=thumbnail_filename, artifact=image_artifact
            )

            # Load the artifact
            tool_context.load_artifact(filename=thumbnail_filename)

            # Store image path in state for reference
            tool_context.state["current_thumbnail"] = thumbnail_filename
            tool_context.state["current_thumbnail_version"] = artifact_version

        except ValueError as e:
            # Handle the case where artifact_service is not configured
            return {
                "status": "warning",
                "message": f"Thumbnail loaded but could not be saved as an artifact: {str(e)}. Is ArtifactService configured?",
                "thumbnail": thumbnail_filename,
            }
        except Exception as e:
            # Handle other potential artifact storage errors
            return {
                "status": "warning",
                "message": f"Thumbnail loaded but encountered an error saving as artifact: {str(e)}",
                "thumbnail": thumbnail_filename,
            }

        # Return success with the image artifact
        return {
            "status": "success",
            "message": f"Thumbnail loaded: {thumbnail_filename}"
            + (f" (version {artifact_version})" if artifact_version else ""),
            "thumbnail": thumbnail_filename,
            "artifact_filename": thumbnail_filename,
            "artifact_version": artifact_version,
        }

    except Exception as e:
        error_message = f"Error loading thumbnail: {str(e)}"
        print(error_message)
        return {"status": "error", "message": error_message}
