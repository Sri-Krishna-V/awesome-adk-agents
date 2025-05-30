GEMINI_MODEL = "gemini-2.5-flash-preview-04-17"

# OpenAI image generation constants
THUMBNAIL_IMAGE_SIZE = "1536x1024"  # Landscape format for YouTube thumbnails

# Image directory structure constants
IMAGE_ROOT_DIR = "images"  # Root directory for all images
REFERENCE_IMAGES_DIR = (
    f"{IMAGE_ROOT_DIR}/reference_images"  # For scraped/reference thumbnails
)
THUMBNAIL_ASSETS_DIR = f"{IMAGE_ROOT_DIR}/assets"  # For user-uploaded assets
GENERATED_THUMBNAILS_DIR = f"{IMAGE_ROOT_DIR}/generated"  # For generated thumbnails
