"""Defines constants."""

import os

import dotenv

dotenv.load_dotenv()

MODEL = os.getenv("MODEL", "gemini-2.0-flash")
DISABLE_WEB_DRIVER = int(os.getenv("DISABLE_WEB_DRIVER", "0"))
