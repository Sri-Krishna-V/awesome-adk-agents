"""
Shared utilities for image handling across agents.
"""

import os
from typing import Dict

from google.adk.tools.tool_context import ToolContext


def ensure_image_directory_exists():
    """
    Ensure that the images directory exists, creating it if necessary.

    Returns:
        str: Path to the images directory
    """
    # Get the absolute path to the repository root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(current_dir, "../.."))

    # Create the images directory path
    images_dir = os.path.join(repo_root, "images")

    # Create the directory if it doesn't exist
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
        print(f"Created images directory at {images_dir}")

    return images_dir


def list_images(tool_context: ToolContext) -> Dict:
    """
    List all images saved in the local images directory.

    Args:
        tool_context (ToolContext): The tool context

    Returns:
        dict: Status and list of image filenames
    """
    try:
        # Ensure images directory exists
        images_dir = ensure_image_directory_exists()

        print(f"[Image Utils] Images directory: {images_dir}")

        # Get a list of all image files in the directory
        image_files = []
        if os.path.exists(images_dir):
            # Get all files in the directory
            all_files = os.listdir(images_dir)

            # Filter for image files only
            image_files = [
                file
                for file in all_files
                if any(
                    file.lower().endswith(ext)
                    for ext in [".png", ".jpg", ".jpeg", ".gif", ".webp"]
                )
            ]

        if not image_files:
            return {
                "status": "success",
                "message": "No images found in the directory.",
                "images": [],
                "count": 0,
            }

        # Sort the image files alphabetically
        image_files.sort()

        # Format the filenames list
        formatted_filenames = []
        for i, filename in enumerate(image_files, 1):
            formatted_filenames.append(f"{i}. {filename}")

        # Update current images in state if needed
        if not tool_context.state.get("current_image_filenames") and image_files:
            tool_context.state["current_image_filenames"] = [image_files[0]]

        return {
            "status": "success",
            "message": f"Found {len(image_files)} image(s):",
            "images": image_files,
            "filenames": "\n".join(formatted_filenames),
            "count": len(image_files),
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Error listing images: {str(e)}",
            "images": [],
            "count": 0,
        }


def delete_image(filename: str, tool_context: ToolContext) -> Dict:
    """
    Delete an image from the local images directory.

    Args:
        filename (str): The name of the image file to delete
        tool_context (ToolContext): The tool context

    Returns:
        dict: Status and result message
    """
    try:
        # Ensure images directory exists
        images_dir = ensure_image_directory_exists()

        # Full path to the image
        image_path = os.path.join(images_dir, filename)

        # Check if the file exists
        if not os.path.exists(image_path):
            return {"status": "error", "message": f"Image '{filename}' not found."}

        # Delete the file
        os.remove(image_path)

        # Update current_image_filenames in state if needed
        current_images = tool_context.state.get("current_image_filenames", [])
        if filename in current_images:
            current_images.remove(filename)
            tool_context.state["current_image_filenames"] = current_images

        return {
            "status": "success",
            "message": f"Image '{filename}' has been deleted successfully.",
        }
    except Exception as e:
        return {"status": "error", "message": f"Error deleting image: {str(e)}"}
