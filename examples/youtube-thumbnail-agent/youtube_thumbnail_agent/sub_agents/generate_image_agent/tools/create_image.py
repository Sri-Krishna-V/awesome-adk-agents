"""
Tool for creating images using OpenAI's image generation API with asset incorporation.
"""

import base64
import glob
import os
from typing import Dict, Optional

import google.genai.types as types
from google.adk.tools.tool_context import ToolContext
from openai import OpenAI

from ....constants import (
    GENERATED_THUMBNAILS_DIR,
    IMAGE_ROOT_DIR,
    THUMBNAIL_ASSETS_DIR,
    THUMBNAIL_IMAGE_SIZE,
)


def create_image(
    prompt: str,
    tool_context: Optional[ToolContext] = None,
) -> Dict:
    """
    Create an image using OpenAI's image generation API with gpt-image-1 model,
    automatically incorporating any assets from the assets directory.

    Behavior:
    - First time: Uses only assets from assets directory (if any)
    - Subsequent edits: Uses both the previously generated thumbnail AND assets

    Args:
        prompt (str): The prompt to generate an image from
        tool_context (ToolContext, optional): The tool context

    Returns:
        dict: Result containing status and message
    """
    try:
        # Get API key from environment
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            return {
                "status": "error",
                "message": "OPENAI_API_KEY not found in environment variables",
            }

        client = OpenAI(api_key=api_key)

        # Clean up prompt if needed
        clean_prompt = prompt.strip()

        # Add YouTube thumbnail context if not mentioned
        if "youtube thumbnail" not in clean_prompt.lower():
            clean_prompt = f"YouTube thumbnail: {clean_prompt}"

        # Initialize response variable
        response = None
        asset_paths = []

        # Ensure root images directory exists
        os.makedirs(IMAGE_ROOT_DIR, exist_ok=True)

        # First, check assets directory - we'll need this regardless
        assets_dir = THUMBNAIL_ASSETS_DIR

        # Create the directory if it doesn't exist
        if not os.path.exists(assets_dir):
            os.makedirs(assets_dir, exist_ok=True)

        # List all files in the assets directory
        asset_files_paths = glob.glob(os.path.join(assets_dir, "*"))

        # Track all asset paths for reporting
        for asset_path in asset_files_paths:
            asset_paths.append(asset_path)

        # Check if we already have a generated thumbnail to use as reference
        if tool_context and tool_context.state.get("thumbnail_generated") is True:
            previous_thumbnail_path = tool_context.state.get("thumbnail_path")

            if previous_thumbnail_path and os.path.exists(previous_thumbnail_path):
                # Add the previous thumbnail path to our assets list for reporting
                if previous_thumbnail_path not in asset_paths:
                    asset_paths.append(previous_thumbnail_path)

                try:
                    # OpenAI images.edit requires at least one image
                    # If we have a previous thumbnail AND other assets, we want to use both

                    if asset_files_paths:
                        # We have both - use previous thumbnail as main and incorporate other assets
                        try:
                            # Generate using previous thumbnail and all assets
                            # Direct array literal works better with type checking
                            asset_file_objects = [
                                open(path, "rb") for path in asset_files_paths
                            ]
                            all_files = [
                                open(previous_thumbnail_path, "rb")
                            ] + asset_file_objects

                            try:
                                response = client.images.edit(
                                    model="gpt-image-1",
                                    # Use direct array literal which has the correct typing
                                    image=[
                                        open(previous_thumbnail_path, "rb"),
                                        *[
                                            open(path, "rb")
                                            for path in asset_files_paths
                                        ],
                                    ],
                                    prompt=clean_prompt,
                                    n=1,
                                    size=THUMBNAIL_IMAGE_SIZE,
                                )
                            finally:
                                # Close all files
                                for file in all_files:
                                    file.close()
                        except Exception as e:
                            return {
                                "status": "error",
                                "message": f"Error generating image with previous thumbnail and assets: {str(e)}",
                            }
                    else:
                        # We only have the previous thumbnail
                        with open(previous_thumbnail_path, "rb") as previous_thumbnail:
                            response = client.images.edit(
                                model="gpt-image-1",
                                image=previous_thumbnail,
                                prompt=clean_prompt,
                                n=1,
                                size=THUMBNAIL_IMAGE_SIZE,
                            )

                except Exception as e:
                    return {
                        "status": "error",
                        "message": f"Error generating image with previous thumbnail: {str(e)}",
                    }
            else:
                # Previous thumbnail path is invalid - fall back to normal flow
                # (This will be handled in the next section)
                pass
        else:
            # No previous thumbnail exists yet - use normal asset flow
            # This will be handled in the next section if we don't have a response yet
            pass

        # If we don't have a response yet (no previous thumbnail or error), try with assets
        if response is None:
            if asset_files_paths:
                # We have assets but no previous thumbnail (or couldn't use it)
                try:
                    # Open all asset files and pass them to the API
                    asset_file_objects = [
                        open(path, "rb") for path in asset_files_paths
                    ]

                    try:
                        # Generate the image using edit endpoint with all assets
                        # Use direct array literal to avoid typing issues
                        response = client.images.edit(
                            model="gpt-image-1",
                            image=[open(path, "rb") for path in asset_files_paths],
                            prompt=clean_prompt,
                            n=1,
                            size=THUMBNAIL_IMAGE_SIZE,
                        )
                    finally:
                        # Ensure all file handles are closed properly
                        for file in asset_file_objects:
                            file.close()

                except Exception as e:
                    return {
                        "status": "error",
                        "message": f"Error generating image with assets: {str(e)}",
                    }
            else:
                # No assets and no previous thumbnail - use the generate endpoint
                response = client.images.generate(
                    model="gpt-image-1",
                    prompt=clean_prompt,
                    n=1,
                    size=THUMBNAIL_IMAGE_SIZE,
                )

        # Get the base64 image data
        if response and response.data and len(response.data) > 0:
            image_base64 = response.data[0].b64_json
            if image_base64:
                image_bytes = base64.b64decode(image_base64)
            else:
                return {
                    "status": "error",
                    "message": "No image data returned from the API",
                }
        else:
            return {
                "status": "error",
                "message": "No data returned from the API",
            }

        # Use simple filename as requested
        filename = "youtube_thumbnail.png"

        # Save as an artifact if tool_context is provided
        artifact_version = None
        if tool_context:
            # Create a Part object for the artifact
            image_artifact = types.Part(
                inline_data=types.Blob(data=image_bytes, mime_type="image/png")
            )

            try:
                # Save the artifact
                artifact_version = tool_context.save_artifact(
                    filename=filename, artifact=image_artifact
                )

                # Update state to indicate a thumbnail has been generated
                tool_context.state["thumbnail_generated"] = True
                tool_context.state["image_filename"] = filename
                tool_context.state["image_version"] = artifact_version

            except ValueError as e:
                # Handle the case where artifact_service is not configured
                return {
                    "status": "warning",
                    "message": f"Image generated but could not be saved as an artifact: {str(e)}. Is ArtifactService configured?",
                }
            except Exception as e:
                # Handle other potential artifact storage errors
                return {
                    "status": "warning",
                    "message": f"Image generated but encountered an error saving as artifact: {str(e)}",
                }

        # Create directory for local file saving
        os.makedirs(GENERATED_THUMBNAILS_DIR, exist_ok=True)

        # Save the image locally as well
        filepath = os.path.join(GENERATED_THUMBNAILS_DIR, filename)
        with open(filepath, "wb") as f:
            f.write(image_bytes)

        # Update state with thumbnail path
        if tool_context:
            tool_context.state["thumbnail_path"] = filepath
            tool_context.state["thumbnail_generated"] = True

        # Return success with artifact details if available
        if artifact_version is not None:
            return {
                "status": "success",
                "message": f"Image created successfully and saved as artifact '{filename}' (version {artifact_version}) and local file '{filepath}'",
                "filepath": filepath,
                "artifact_filename": filename,
                "artifact_version": artifact_version,
                "assets_used": (
                    [os.path.basename(path) for path in asset_paths]
                    if asset_paths
                    else []
                ),
                "thumbnail_generated": True,
                "is_first_generation": not (
                    tool_context
                    and tool_context.state.get("thumbnail_generated", False)
                ),
            }
        else:
            return {
                "status": "success",
                "message": f"Image created successfully and saved as local file '{filepath}'",
                "filepath": filepath,
                "assets_used": (
                    [os.path.basename(path) for path in asset_paths]
                    if asset_paths
                    else []
                ),
                "thumbnail_generated": True,
                "is_first_generation": not (
                    tool_context
                    and tool_context.state.get("thumbnail_generated", False)
                ),
            }

    except Exception as e:
        return {"status": "error", "message": f"Error creating image: {str(e)}"}
