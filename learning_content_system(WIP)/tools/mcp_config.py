"""
MCP Server Configuration for Learning Content System
"""

import json
import os
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters


# MCP Server Configurations
def get_huggingface_mcp_toolset():
    """
    Hugging Face MCP Server for model, dataset, and paper search
    """
    return MCPToolset(
        connection_params=StdioServerParameters(
            command="npx",
            args=["-y", "@shreyaskarnik/huggingface-mcp-server"],
        ),
        tool_filter=["search-models", "search-datasets",
                     "get-model-info", "search-papers"]
    )


def get_image_generation_mcp_toolset():
    """
    Image Generation MCP Server using SanaSprint
    """
    return MCPToolset(
        connection_params=StdioServerParameters(
            command="npx",
            args=["mcp-remote", "https://ysharma-sanasprint.hf.space/gradio_api/mcp/sse",
                  "--transport", "sse-only"],
        ),
        tool_filter=["generate_image"]
    )


def get_tts_mcp_toolset():
    """
    Text-to-Speech MCP Server using Dia-1.6B
    """
    return MCPToolset(
        connection_params=StdioServerParameters(
            command="npx",
            args=["mcp-remote", "https://ysharma-dia-1-6b.hf.space/gradio_api/mcp/sse",
                  "--transport", "sse-only"],
        ),
        tool_filter=["generate_speech"]
    )


def get_general_tools_mcp_toolset():
    """
    General MCP Tools for various utilities
    """
    return MCPToolset(
        connection_params=StdioServerParameters(
            command="npx",
            args=["mcp-remote", "https://abidlabs-mcp-tools.hf.space/gradio_api/mcp/sse",
                  "--transport", "sse-only"],
        )
    )


def get_sentiment_analysis_mcp_toolset():
    """
    Sentiment Analysis MCP Server for content quality assessment
    """
    return MCPToolset(
        connection_params=StdioServerParameters(
            command="npx",
            args=["mcp-remote", "https://sentiment-analysis-mcp.hf.space/gradio_api/mcp/sse",
                  "--transport", "sse-only"],
        ),
        tool_filter=["sentiment_analysis"]
    )


# All available MCP toolsets
AVAILABLE_MCP_TOOLSETS = {
    "huggingface": get_huggingface_mcp_toolset,
    "image_generation": get_image_generation_mcp_toolset,
    "tts": get_tts_mcp_toolset,
    "general_tools": get_general_tools_mcp_toolset,
    "sentiment_analysis": get_sentiment_analysis_mcp_toolset,
}
