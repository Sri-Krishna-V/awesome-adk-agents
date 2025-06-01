import json
import logging
from typing import Any

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.server.tasks import TaskUpdater
from a2a.types import DataPart, Part
from common.config import (
    DEFAULT_ALPHABOT_LONG_SMA,
    DEFAULT_ALPHABOT_SHORT_SMA,
    DEFAULT_ALPHABOT_TRADE_QTY,
    DEFAULT_ALPHABOT_TRADE_DECISION_ARTIFACT_NAME,
    DEFAULT_RISKGUARD_MAX_CONCENTRATION,
    DEFAULT_RISKGUARD_MAX_POS_SIZE,
    DEFAULT_RISKGUARD_URL,
)
from google.adk import Runner
from google.adk.artifacts import InMemoryArtifactService
from google.adk.memory import InMemoryMemoryService
from google.adk.sessions import InMemorySessionService, Session
from google.genai import types as genai_types

from alphabot.agent import root_agent as alphabot_adk_agent

logger = logging.getLogger(__name__)


class AlphaBotAgentExecutor(AgentExecutor):
    """Executes the AlphaBot ADK agent logic in response to A2A requests."""

    def __init__(self):
        self._adk_agent = alphabot_adk_agent
        self._adk_runner = Runner(
            app_name="alphabot_adk_runner",
            agent=self._adk_agent,
            session_service=InMemorySessionService(),
            memory_service=InMemoryMemoryService(),
            artifact_service=InMemoryArtifactService(),
        )
        logger.info("AlphaBotAgentExecutor initialized with ADK Runner.")

    async def execute(self, context: RequestContext, event_queue: EventQueue):
        task_updater = TaskUpdater(event_queue, context.task_id, context.context_id)

        if (
            not context.current_task
        ):  # Should be created by DefaultRequestHandler if not existing
            task_updater.submit(message=context.message)  # Send initial message
        task_updater.start_work(
            message=task_updater.new_agent_message(
                parts=[
                    Part(root=DataPart(data={"status": "Processing trade signal..."}))
                ]
            )
        )

        # Extract data from context.message
        market_data: dict[str, Any] | None = None
        portfolio_state: dict[str, Any] | None = None

        if context.message and context.message.parts:
            for part_union in context.message.parts:
                part = part_union.root  # Access the actual Part model
                if isinstance(part, DataPart):
                    # Check for indicative keys to identify market_data
                    if (
                        "current_price" in part.data
                        and "historical_prices" in part.data
                    ):
                        market_data = part.data
                    # Check for indicative keys to identify portfolio_state
                    elif "cash" in part.data and "shares" in part.data:
                        portfolio_state = part.data

        if market_data is None or portfolio_state is None:
            logger.error(
                f"Task {context.task_id}: Missing market_data or portfolio_state. Extracted market_data: {market_data}, Extracted portfolio_state: {portfolio_state}. Input message parts: {context.message.parts if context.message else 'No message'}"
            )
            task_updater.failed(
                message=task_updater.new_agent_message(
                    parts=[
                        Part(
                            root=DataPart(
                                data={
                                    "error": "Invalid input: Missing market_data or portfolio_state"
                                }
                            )
                        )
                    ]
                )
            )
            return

        # Ensure agent_params is initialized even if context.message.metadata is None
        agent_params = (context.message.metadata or {}) if context.message else {}
        short_sma = agent_params.get("short_sma", DEFAULT_ALPHABOT_SHORT_SMA)
        long_sma = agent_params.get("long_sma", DEFAULT_ALPHABOT_LONG_SMA)
        trade_qty = agent_params.get("trade_qty", DEFAULT_ALPHABOT_TRADE_QTY)
        riskguard_url = agent_params.get("riskguard_url", DEFAULT_RISKGUARD_URL)
        max_pos_size = agent_params.get("max_pos_size", DEFAULT_RISKGUARD_MAX_POS_SIZE)
        max_concentration = agent_params.get(
            "max_concentration", DEFAULT_RISKGUARD_MAX_CONCENTRATION
        )

        # Prepare input for ADK Agent
        agent_input_dict = {
            "historical_prices": market_data.get("historical_prices", []),
            "current_price": market_data.get("current_price"),
            "day": market_data.get("day"),
            "portfolio_state": portfolio_state,
            "short_sma_period": short_sma,
            "long_sma_period": long_sma,
            "trade_quantity": trade_qty,
            "riskguard_url": riskguard_url,
            "max_pos_size": max_pos_size,
            "max_concentration": max_concentration,
        }
        agent_input_dict = {k: v for k, v in agent_input_dict.items() if v is not None}
        agent_input_json = json.dumps(agent_input_dict)
        adk_content = genai_types.Content(
            parts=[genai_types.Part(text=agent_input_json)]
        )

        # Ensure ADK Session Exists
        session_id_for_adk = context.context_id
        logger.info(
            f"Task {context.task_id}: Attempting to get/create ADK session for session_id: '{session_id_for_adk}' (type: {type(session_id_for_adk)})"
        )

        session: Session | None = None
        if (
            session_id_for_adk
        ):  # Only proceed if session_id_for_adk is not None or empty
            try:
                session = (
                    await self._adk_runner.session_service.get_session(  # Added await
                        app_name=self._adk_runner.app_name,
                        user_id="a2a_user",
                        session_id=session_id_for_adk,
                    )
                )
            except Exception as e_get:
                logger.exception(
                    f"Task {context.task_id}: Exception during ADK session get_session for session_id '{session_id_for_adk}': {e_get}"
                )
                session = None  # Ensure session is None if get_session failed

            if not session:
                logger.info(
                    f"Task {context.task_id}: ADK Session not found or failed to get for '{session_id_for_adk}'. Creating new session."
                )
                try:
                    session = await self._adk_runner.session_service.create_session(  # Added await
                        app_name=self._adk_runner.app_name,
                        user_id="a2a_user",
                        session_id=session_id_for_adk,
                        state={},
                    )
                    if session:  # session should be the Session object here
                        # Assuming the ADK Session object uses 'id' for its identifier
                        logger.info(
                            f"Task {context.task_id}: Successfully created ADK session '{session.id if hasattr(session, 'id') else 'ID_NOT_FOUND'}'."
                        )
                    else:
                        # This case might happen if create_session, despite being awaited, could return None (though unlikely for InMemory)
                        logger.error(
                            f"Task {context.task_id}: ADK InMemorySessionService.create_session returned None for session_id '{session_id_for_adk}'."
                        )
                except Exception as e_create:
                    logger.exception(
                        f"Task {context.task_id}: Exception during ADK session create_session for session_id '{session_id_for_adk}': {e_create}"
                    )
                    session = None  # Ensure session is None if creation failed
            else:  # session was successfully retrieved by get_session
                # Assuming the ADK Session object uses 'id' for its identifier
                logger.info(
                    f"Task {context.task_id}: Found existing ADK session '{session.id if hasattr(session, 'id') else 'ID_NOT_FOUND'}'."
                )
        else:
            logger.error(
                f"Task {context.task_id}: ADK session_id (context.context_id) is None or empty. Cannot initialize ADK session."
            )

        if (
            not session
        ):  # If session is still None after trying to get/create, or if session_id_for_adk was initially invalid
            error_message = f"Failed to establish ADK session. session_id was '{session_id_for_adk}'."
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

        final_result_dict: dict[str, Any] = {}
        final_reason_text = "Reason not provided."
        captured_state_delta = None

        try:
            # Assuming the ADK Session object uses 'id' for its identifier for logging confirmation
            logger.info(
                f"Task {context.task_id}: Calling ADK run_async with session_id_for_adk: '{session_id_for_adk}'. ADK session object is {'present and has id' if session and hasattr(session, 'id') and session.id else 'None, or missing id attribute, or id is None/empty'}."
            )
            async for event in self._adk_runner.run_async(
                user_id="a2a_user",
                session_id=session_id_for_adk,
                new_message=adk_content,  # Use session_id_for_adk which was validated
            ):
                if event.actions and event.actions.state_delta:
                    captured_state_delta = event.actions.state_delta
                if event.is_final_response():
                    if event.content and event.content.parts:
                        text_part = next(
                            (
                                p
                                for p in event.content.parts
                                if hasattr(p, "text") and p.text
                            ),
                            None,
                        )
                        if text_part:
                            final_reason_text = text_part.text

            if captured_state_delta:
                if "approved_trade" in captured_state_delta:
                    final_result_dict = {
                        "approved": True,
                        "trade_proposal": captured_state_delta["approved_trade"],
                        "reason": final_reason_text,
                    }
                elif "rejected_trade_proposal" in captured_state_delta:
                    final_result_dict = {
                        "approved": False,
                        "trade_proposal": captured_state_delta[
                            "rejected_trade_proposal"
                        ],
                        "reason": final_reason_text,
                    }
                else:  # No trade decision in state_delta, use reason text as generic message
                    final_result_dict = {"status": "Info", "message": final_reason_text}
            elif (
                final_reason_text != "Reason not provided."
            ):  # Use reason text if no state_delta but reason exists
                final_result_dict = {"status": "Info", "message": final_reason_text}
            else:  # Fallback if nothing conclusive
                final_result_dict = {
                    "status": "Unknown",
                    "message": "Agent finished, unknown result format.",
                }

            task_updater.add_artifact(
                parts=[Part(root=DataPart(data=final_result_dict))],
                name=DEFAULT_ALPHABOT_TRADE_DECISION_ARTIFACT_NAME,
            )
            task_updater.complete()

        except Exception as e:
            logger.exception(
                f"Task {context.task_id}: Error running AlphaBot ADK agent: {e}"
            )
            task_updater.failed(
                message=task_updater.new_agent_message(
                    parts=[Part(root=DataPart(data={"error": f"ADK Agent error: {e}"}))]
                )
            )

    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        logger.warning(
            f"Cancellation not implemented for AlphaBot ADK agent task: {context.task_id}"
        )
        task_updater = TaskUpdater(event_queue, context.task_id, context.context_id)
