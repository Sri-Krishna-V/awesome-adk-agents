import json
import logging
from typing import Any, AsyncGenerator, Dict

from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event
from google.genai import types as genai_types
from pydantic import BaseModel, Field, ValidationError  # Import Pydantic

from .rules import (
    DEFAULT_RISKGUARD_MAX_CONCENTRATION,
    DEFAULT_RISKGUARD_MAX_POS_SIZE,
    RiskCheckResult,
    check_trade_risk_logic,
)

logger = logging.getLogger(__name__)


# --- Pydantic Input Models for RiskGuard ---
class TradeProposalInput(BaseModel):
    action: str
    ticker: str
    quantity: int
    price: float


class PortfolioStateInput(BaseModel):
    cash: float
    shares: int
    total_value: float


class RiskGuardInput(BaseModel):
    trade_proposal: TradeProposalInput
    portfolio_state: PortfolioStateInput
    max_pos_size: float = Field(default=DEFAULT_RISKGUARD_MAX_POS_SIZE)
    max_concentration: float = Field(default=DEFAULT_RISKGUARD_MAX_CONCENTRATION)


class RiskGuardAgent(BaseAgent):
    """
    ADK Agent implementing the RiskGuard logic.
    Designed to be hosted via an A2A server.
    """

    name: str = "RiskGuard"
    description: str = "Evaluates proposed trades against predefined risk rules."

    async def _run_async_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        """
        Processes a risk check request received via A2A (simulated via message content).
        """
        invocation_id_short = ctx.invocation_id[:8]
        logger.info(
            f"[{self.name} ({invocation_id_short})] Received risk check invocation"
        )

        default_error_reason = "Internal Error: Failed to process input."
        result_dict = {
            "approved": False,
            "reason": default_error_reason,
        }

        input_text = None
        if (
            ctx.user_content
            and ctx.user_content.parts
            and hasattr(ctx.user_content.parts[0], "text")
        ):
            input_text = ctx.user_content.parts[0].text

        if not input_text:
            logger.error(
                f"[{self.name} ({invocation_id_short})] Input message text not found."
            )
            result_dict["reason"] = "Internal Error: Missing input message text."
        else:
            try:
                input_payload = json.loads(input_text)
                validated_input = RiskGuardInput(**input_payload)
                logger.info(
                    f"[{self.name} ({invocation_id_short})] Successfully parsed and validated input: {validated_input.model_dump_json(indent=2)}"
                )

                # Pass Pydantic models or their dict representations to logic
                # The check_trade_risk_logic expects dicts for trade_proposal and portfolio_state
                result: RiskCheckResult = check_trade_risk_logic(
                    trade_proposal=validated_input.trade_proposal.model_dump(),
                    portfolio_state=validated_input.portfolio_state.model_dump(),
                    max_pos_size=validated_input.max_pos_size,
                    max_concentration=validated_input.max_concentration,
                )
                result_dict = {"approved": result.approved, "reason": result.reason}

            except json.JSONDecodeError as e:
                logger.error(
                    f"[{self.name} ({invocation_id_short})] Failed to decode input JSON from message: {input_text[:100]}... Error: {e}",
                    exc_info=True,
                )
                result_dict["reason"] = (
                    "Internal Error: Invalid input data format (JSON)."
                )
            except ValidationError as e:
                logger.error(
                    f"[{self.name} ({invocation_id_short})] Input validation failed: {e}. Input was: '{input_text[:200]}...'"
                )
                result_dict["reason"] = (
                    f"Internal Error: Invalid input data structure - {e.errors()}"
                )

            except Exception as e:
                logger.error(
                    f"[{self.name} ({invocation_id_short})] Unexpected error processing input: {e}",
                    exc_info=True,
                )
                result_dict["reason"] = f"Internal Error: {e}"

        logger.info(
            f"[{self.name} ({invocation_id_short})] Yielding result: {result_dict}"
        )
        yield Event(
            author=self.name,
            content=genai_types.Content(
                parts=[
                    genai_types.Part(
                        function_response=genai_types.FunctionResponse(
                            name="risk_check_result",  # This name is used by AgentExecutor to extract the result
                            response=result_dict,
                        )
                    )
                ]
            ),
            turn_complete=True,  # RiskGuard is a single-turn agent for each request
        )
        logger.info(
            f"[{self.name} ({invocation_id_short})] Risk check invocation processed and result yielded."
        )


root_agent = RiskGuardAgent()
logger.info(f"RiskGuardAgent root_agent instance created.")
