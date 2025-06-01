import json
import logging
from typing import Any

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.server.tasks import TaskUpdater
from a2a.types import DataPart, Part, TaskState
from common.config import (
    DEFAULT_RISKGUARD_MAX_CONCENTRATION,
    DEFAULT_RISKGUARD_MAX_POS_SIZE,
)
from google.adk import Runner
from google.adk.sessions import InMemorySessionService, Session
from google.genai import types as genai_types

from .agent import root_agent as riskguard_adk_agent

logger = logging.getLogger(__name__)


class RiskGuardAgentExecutor(AgentExecutor):
    """Executes the RiskGuard ADK agent logic in response to A2A requests."""

    def __init__(self):
        self._adk_agent = riskguard_adk_agent
        self._adk_runner = Runner(
            app_name="riskguard_adk_runner",
            agent=self._adk_agent,
            session_service=InMemorySessionService(),
            # Other services like memory and artifact can be added if needed by the ADK agent
        )
        logger.info("RiskGuardAgentExecutor initialized with ADK Runner.")

    async def execute(self, context: RequestContext, event_queue: EventQueue):
        task_updater = TaskUpdater(event_queue, context.task_id, context.context_id)

        if not context.current_task:
            task_updater.submit(message=context.message)
        task_updater.start_work(
            message=task_updater.new_agent_message(
                parts=[Part(root=DataPart(data={"status": "Checking risk..."}))]
            )
        )

        trade_proposal: dict[str, Any] | None = None
        portfolio_state: dict[str, Any] | None = None

        if context.message and context.message.parts:
            for part_union in context.message.parts:
                part = part_union.root  # Access the actual Part model
                if isinstance(part, DataPart):
                    if "trade_proposal" in part.data:
                        trade_proposal = part.data["trade_proposal"]
                    if "portfolio_state" in part.data:
                        portfolio_state = part.data["portfolio_state"]

        if not trade_proposal or not portfolio_state:
            logger.error(
                f"Task {context.task_id}: Missing 'trade_proposal' or 'portfolio_state'"
            )
            task_updater.failed(
                message=task_updater.new_agent_message(
                    parts=[Part(root=DataPart(data={"error": "Invalid input data"}))]
                )
            )
            return

        risk_metadata = context.message.metadata or {}
        max_pos_size = risk_metadata.get("max_pos_size", DEFAULT_RISKGUARD_MAX_POS_SIZE)
        max_concentration = risk_metadata.get(
            "max_concentration", DEFAULT_RISKGUARD_MAX_CONCENTRATION
        )

        agent_input_data = {
            "trade_proposal": trade_proposal,
            "portfolio_state": portfolio_state,
            "max_pos_size": max_pos_size,
            "max_concentration": max_concentration,
        }
        agent_input_json = json.dumps(agent_input_data)
        adk_content = genai_types.Content(
            parts=[genai_types.Part(text=agent_input_json)]
        )

        session: Session | None = await self._adk_runner.session_service.get_session(
            app_name=self._adk_runner.app_name,
            user_id="a2a_user",
            session_id=context.context_id,
        )
        if session is None:
            logger.info(
                f"Task {context.task_id}: ADK Session not found for '{context.context_id}'. Creating new session."
            )
            session = await self._adk_runner.session_service.create_session(
                app_name=self._adk_runner.app_name,
                user_id="a2a_user",
                session_id=context.context_id,
                state={},
            )
            if session:
                logger.info(
                    f"Task {context.task_id}: Successfully created ADK session '{session.id if hasattr(session, 'id') else 'ID_NOT_FOUND'}'."
                )
            else:
                logger.error(
                    f"Task {context.task_id}: ADK InMemorySessionService.create_session returned None for session_id '{context.context_id}'."
                )
        else:
            logger.info(
                f"Task {context.task_id}: Found existing ADK session '{session.id if hasattr(session, 'id') else 'ID_NOT_FOUND'}'."
            )

        if not session:
            error_message = f"Failed to establish ADK session. session_id was '{context.context_id}'."
            logger.error(
                f"Task {context.task_id}: {error_message} Cannot proceed with ADK run."
            )
            task_updater.failed(
                message=task_updater.new_agent_message(
                    parts=[
                        Part(
                            root=DataPart(
                                data={"error": f"Internal error: {error_message}"}
                            )
                        )
                    ]
                )
            )
            return

        risk_result_dict: dict[str, Any] = {
            "approved": False,
            "reason": "Internal Error",
        }
        try:
            async for event in self._adk_runner.run_async(
                user_id="a2a_user",
                session_id=context.context_id,
                new_message=adk_content,
            ):
                if event.content and event.content.parts:
                    first_part = event.content.parts[0]
                    if (
                        hasattr(first_part, "function_response")
                        and first_part.function_response
                        and first_part.function_response.name == "risk_check_result"
                    ):
                        response_data = first_part.function_response.response
                        if isinstance(response_data, dict):
                            risk_result_dict = response_data
                            break  # Assuming the first function_response is the one we need.

            task_updater.add_artifact(
                parts=[Part(root=DataPart(data=risk_result_dict))],
                name="risk_assessment",
            )
            task_updater.complete()

        except Exception as e:
            logger.error(
                f"Error running RiskGuard ADK agent for task {context.task_id}: {e}",
                exc_info=True,
            )
            task_updater.failed(
                message=task_updater.new_agent_message(
                    parts=[Part(root=DataPart(data={"error": f"ADK Agent error: {e}"}))]
                )
            )

    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        logger.warning(
            f"Cancellation not implemented for RiskGuard ADK agent task: {context.task_id}"
        )
        task_updater = TaskUpdater(event_queue, context.task_id, context.context_id)
