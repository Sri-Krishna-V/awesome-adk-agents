import os
import os.path
import re
from typing import Dict, List, Optional

import requests
from dotenv import load_dotenv
from google.adk.tools.tool_context import ToolContext

from ....constants import IMAGE_ROOT_DIR, REFERENCE_IMAGES_DIR

# Load environment variables
load_dotenv()


def ensure_reference_images_dir():
    """Ensure the reference_images directory exists."""
    # Create the root images directory if it doesn't exist
    os.makedirs(IMAGE_ROOT_DIR, exist_ok=True)
    # Create the reference_images directory
    os.makedirs(REFERENCE_IMAGES_DIR, exist_ok=True)
    return REFERENCE_IMAGES_DIR


def download_thumbnail(url: str, save_path: str, index: int) -> Optional[str]:
    """Download a thumbnail from URL."""
    response = requests.get(url)

    if response.status_code == 200:
        # Save the image
        with open(save_path, "wb") as f:
            f.write(response.content)
        return save_path
    else:
        print(
            f"Failed to download thumbnail {index} with status code {response.status_code}"
        )
        return None


def extract_channel_id(channel_name: str) -> Optional[str]:
    """Extract channel ID from different formats of channel names."""
    # If it's already a channel ID format
    if re.match(r"^[A-Za-z0-9_-]{24}$", channel_name):
        return channel_name

    # If it's a handle or user format
    if channel_name.startswith("@"):
        return channel_name  # Return as is, we'll handle it in the API call

    # If it's a full URL
    channel_url_match = re.search(
        r"youtube\.com/(?:channel|c|user)/([^/]+)", channel_name
    )
    if channel_url_match:
        return channel_url_match.group(1)

    # If it's a handle URL
    handle_url_match = re.search(r"youtube\.com/(@[^/]+)", channel_name)
    if handle_url_match:
        return handle_url_match.group(1)

    # Return as-is if nothing matches, assuming it might be a valid input
    return channel_name


def is_short_video(video_id: str, api_key: str) -> bool:
    """
    Determine if a video is a Short or not by checking its duration.
    YouTube Shorts are typically <= 60 seconds.

    Args:
        video_id: YouTube video ID
        api_key: YouTube API key

    Returns:
        Boolean indicating if the video is a Short
    """
    try:
        # Get video details including duration
        video_url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={video_id}&key={api_key}"
        response = requests.get(video_url)

        if response.status_code != 200:
            print(
                f"Failed to get video details for {video_id}. Status code: {response.status_code}"
            )
            return False  # Assume not a short if we can't determine

        data = response.json()

        if not data.get("items"):
            return False

        # Extract duration in ISO 8601 format (e.g., PT1M30S for 1 minute 30 seconds)
        duration_str = data["items"][0]["contentDetails"]["duration"]

        # Parse the duration
        # Simple check: if duration contains M and number before M is > 1, or if it contains H, it's not a short
        if "H" in duration_str:
            return False  # Has hours, definitely not a short

        if "M" in duration_str:
            minutes_match = re.search(r"PT(\d+)M", duration_str)
            if minutes_match and int(minutes_match.group(1)) > 1:
                return False  # More than 1 minute, not a short

        # Check seconds
        seconds_match = re.search(r"M(\d+)S|PT(\d+)S", duration_str)
        total_seconds = 0

        if "M" in duration_str:
            minutes_match = re.search(r"PT(\d+)M", duration_str)
            if minutes_match:
                total_seconds += int(minutes_match.group(1)) * 60

        if seconds_match:
            seconds_group = (
                seconds_match.group(1)
                if seconds_match.group(1)
                else seconds_match.group(2)
            )
            total_seconds += int(seconds_group)

        # YouTube Shorts are typically 300 seconds or less
        return total_seconds <= 300

    except Exception as e:
        print(f"Error determining if video is a short: {str(e)}")
        return False  # Assume not a short if we can't determine


def scrape_channel(
    tool_context: ToolContext,
    channel_name: str,
) -> Dict:
    """
    Scrape thumbnails from a YouTube channel, excluding Shorts.
    Will continue fetching videos until the requested number of longform thumbnails is found
    or there are no more videos to fetch.

    Args:
        tool_context: ADK tool context
        channel_name: YouTube channel name/ID/handle

    Returns:
        Dictionary with scraping results
    """
    num_thumbnails = 5
    # Number of videos to fetch per API request
    batch_size = 25
    max_attempts = (
        3  # Maximum number of pagination attempts to avoid excessive API usage
    )

    try:
        # Extract channel ID if needed
        channel_id = extract_channel_id(channel_name)
        if not channel_id:
            return {
                "status": "error",
                "message": f"Could not extract channel ID from: {channel_name}",
            }

        # Prepare reference images directory
        ref_dir = ensure_reference_images_dir()

        # Get YouTube API key from environment variables
        api_key = os.getenv("YOUTUBE_API_KEY")
        if not api_key:
            return {
                "status": "error",
                "message": "YouTube API key not found in environment variables. Please add YOUTUBE_API_KEY to your .env file.",
            }

        # Build API URL for channel lookup
        channel_url = None
        if channel_id.startswith("@"):
            # Handle format, need to get the channel ID first
            handle_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={channel_id}&type=channel&key={api_key}"
            handle_response = requests.get(handle_url)
            if handle_response.status_code != 200:
                return {
                    "status": "error",
                    "message": f"Failed to look up channel with handle {channel_id}. Status code: {handle_response.status_code}",
                }

            handle_data = handle_response.json()
            if not handle_data.get("items"):
                return {
                    "status": "error",
                    "message": f"No channel found for handle {channel_id}",
                }

            # Get the actual channel ID
            channel_id = handle_data["items"][0]["snippet"]["channelId"]

        # Initialize variables for pagination
        thumbnails: List[str] = []
        longform_videos_found = 0
        next_page_token = None
        attempts = 0

        # Initialize thumbnail_analysis in state if necessary
        if tool_context and "thumbnail_analysis" not in tool_context.state:
            tool_context.state["thumbnail_analysis"] = {}

        # Continue fetching until we have enough thumbnails or run out of videos
        while longform_videos_found < num_thumbnails and attempts < max_attempts:
            attempts += 1

            # Build URL for video lookup with pagination token if available
            page_param = f"&pageToken={next_page_token}" if next_page_token else ""
            channel_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&maxResults={batch_size}&order=date&type=video&key={api_key}{page_param}"

            # Fetch videos from the channel
            response = requests.get(channel_url)
            if response.status_code != 200:
                return {
                    "status": "error",
                    "message": f"Failed to fetch videos from the channel. Status code: {response.status_code}",
                }

            data = response.json()

            # Check if we have videos
            if not data.get("items"):
                break  # No more videos to process

            # Process videos in this batch
            for item in data["items"]:
                if longform_videos_found >= num_thumbnails:
                    break

                video_id = item["id"]["videoId"]

                # Skip if this is a short video
                if is_short_video(video_id, api_key):
                    continue

                # This is a longform video, process it
                longform_videos_found += 1
                thumbnail_url = item["snippet"]["thumbnails"]["high"]["url"]

                # Save the thumbnail
                thumbnail_filename = f"channel_thumbnail_{longform_videos_found}.jpg"
                save_path = os.path.join(ref_dir, thumbnail_filename)

                result = download_thumbnail(
                    thumbnail_url, save_path, longform_videos_found
                )
                if result:
                    thumbnails.append(thumbnail_filename)

                    # Add to thumbnail_analysis with empty string value for later analysis
                    if tool_context:
                        tool_context.state["thumbnail_analysis"][
                            thumbnail_filename
                        ] = ""

            # Check if we have a next page token for pagination
            next_page_token = data.get("nextPageToken")
            if not next_page_token:
                break  # No more pages to fetch

        if not thumbnails:
            return {
                "status": "warning",
                "message": f"Could not find or download any longform video thumbnails for {channel_name}",
            }

        # Return success, but note if we couldn't find enough thumbnails
        status = "success"
        message = f"Successfully scraped {len(thumbnails)} longform video thumbnails from {channel_name}"
        if len(thumbnails) < num_thumbnails:
            status = "partial_success"
            message += f" (requested {num_thumbnails}, but only found {len(thumbnails)} longform videos)"

        return {
            "status": status,
            "message": message,
            "channel_name": channel_name,
            "thumbnails": thumbnails,
        }

    except Exception as e:
        error_message = f"Error scraping channel: {str(e)}"
        print(error_message)
        return {"status": "error", "message": error_message}
