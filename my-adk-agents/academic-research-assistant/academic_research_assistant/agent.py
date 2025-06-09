# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Defines the Academic Research Assistant Agent.

This module implements the root agent for the Academic Research Assistant system,
which helps users accelerate academic literature reviews by orchestrating specialized
sub-agents in a sequential workflow.

The agent architecture follows a hierarchical structure with:
1. A root agent that coordinates the overall workflow
2. Three specialized sub-agents that handle different aspects of the research process:
   - Profiler agent: Analyzes researcher profiles to extract relevant keywords
   - Searcher agent: Finds relevant academic papers based on topic and keywords
   - Comparison agent: Analyzes and compares papers to generate insights

Typical usage:
    from academic_research_assistant.agent import root_agent
    root_agent.start()
"""

from google.adk.agents.llm_agent import Agent

from .shared_libraries import constants
from . import prompts

from .sub_agents.profiler_agent.agent import profiler_agent
from .sub_agents.searcher_agent.agent import searcher_agent
from .sub_agents.comparison_root_agent.agent import comparison_root_agent

academic_research_assistant = Agent(
    model=constants.MODEL,
    name="academic_research_assistant",
    description="An AI assistant to accelerate academic literature reviews.",
    instruction=prompts.ROOT_PROMPT,
    sub_agents=[
        comparison_root_agent,
        profiler_agent,
        searcher_agent,  
    ],
)

root_agent = academic_research_assistant
