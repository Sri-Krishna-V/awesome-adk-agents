"""Constants used throughout the Academic Research Assistant.

This module defines global constants used across the Academic Research Assistant
agent system. It loads environment variables using dotenv for configuration.

Constants:
    MODEL (str): The LLM model to use for all agents, defaults to 'gemini-2.0-flash'
        if not specified in environment variables.
    DISABLE_WEB_DRIVER (int): Flag to enable/disable web driver functionality,
        useful for testing or environments where browser automation is not available.
        Defaults to 0 (enabled).

Usage:
    from academic_research_assistant.shared_libraries import constants
    
    model = constants.MODEL
    web_driver_disabled = constants.DISABLE_WEB_DRIVER
"""

import os

import dotenv

dotenv.load_dotenv()

MODEL = os.getenv("MODEL", "gemini-2.0-flash")
DISABLE_WEB_DRIVER = int(os.getenv("DISABLE_WEB_DRIVER", "0"))
