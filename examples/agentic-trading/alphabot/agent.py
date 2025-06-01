import json
import logging
import uuid
from typing import Any, AsyncGenerator, Dict, List

# Import defaults from the central config
from common.config import (
    DEFAULT_ALPHABOT_LONG_SMA,
    DEFAULT_ALPHABOT_SHORT_SMA,
    DEFAULT_ALPHABOT_TRADE_QTY,
    DEFAULT_RISKGUARD_MAX_CONCENTRATION,
    DEFAULT_RISKGUARD_MAX_POS_SIZE,
    DEFAULT_RISKGUARD_URL,
    DEFAULT_TICKER,
)
from common.utils.indicators import calculate_sma

# ADK Imports
from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.events import Event, EventActions
from google.adk.tools import BaseTool, ToolContext
from google.genai import types as genai_types
from pydantic import BaseModel, Field, ValidationError  # Import Pydantic

from .a2a_risk_tool import A2ARiskCheckTool

logger = logging.getLogger(__name__)


# --- Pydantic Input Model for AlphaBot ---
class PortfolioStateInput(BaseModel):
    cash: float
    shares: int
    total_value: float


class AlphaBotInput(BaseModel):
    historical_prices: List[float]
    current_price: float
    portfolio_state: PortfolioStateInput  # Use the nested model
    short_sma_period: int = Field(default=DEFAULT_ALPHABOT_SHORT_SMA)
    long_sma_period: int = Field(default=DEFAULT_ALPHABOT_LONG_SMA)
    trade_quantity: int = Field(default=DEFAULT_ALPHABOT_TRADE_QTY)
    riskguard_url: str = Field(default=DEFAULT_RISKGUARD_URL)
    max_pos_size: float = Field(default=DEFAULT_RISKGUARD_MAX_POS_SIZE)
    max_concentration: float = Field(default=DEFAULT_RISKGUARD_MAX_CONCENTRATION)
    day: int


class AlphaBotAgent(BaseAgent):
    ticker: str
    tools: List[BaseTool]

    def __init__(
        self,
        stock_ticker: str = DEFAULT_TICKER,
        agent_name: str = "AlphaBot",
        **kwargs,
    ):
        a2a_tool = A2ARiskCheckTool()
        agent_description = (
            "AlphaBot agent using SMA crossover strategy with A2A risk checks."
        )
        super().__init__(
            name=agent_name,
            description=agent_description,
            tools=[a2a_tool],
            ticker=stock_ticker,
            **kwargs,
        )
        logger.debug(f"[{self.name}] Initialized with ticker: {self.ticker}")

    def _parse_and_validate_input_pydantic(
        self, ctx: InvocationContext
    ) -> AlphaBotInput | None:
        """Parses input JSON into AlphaBotInput Pydantic model."""
        invocation_id_short = ctx.invocation_id[:8]
        logger.debug(
            f"[{self.name} ({invocation_id_short})] Attempting to parse input with Pydantic..."
        )
        if (
            not ctx.user_content
            or not ctx.user_content.parts
            or not hasattr(ctx.user_content.parts[0], "text")
        ):
            logger.error(
                f"[{self.name} ({invocation_id_short})] ERROR - Input event text not found."
            )
            return None

        input_text = ctx.user_content.parts[0].text
        try:
            input_payload = json.loads(input_text)
            validated_input = AlphaBotInput(**input_payload)
            logger.info(
                f"[{self.name} ({invocation_id_short})] Successfully parsed and validated input: {validated_input.model_dump(exclude={'historical_prices'})}"
            )
            logger.debug(
                f"[{self.name} ({invocation_id_short})] Full validated input historical_prices count: {len(validated_input.historical_prices)}"
            )
            return validated_input
        except json.JSONDecodeError as e:
            logger.error(
                f"[{self.name} ({invocation_id_short})] ERROR - Failed to decode input JSON: '{input_text[:200]}...'. Error: {e}"
            )
            return None
        except ValidationError as e:
            logger.error(
                f"[{self.name} ({invocation_id_short})] ERROR - Input validation failed: {e}. Input was: '{input_text[:200]}...'"
            )
            return None

    def _calculate_indicators(
        self,
        historical_prices: List[float],
        short_period: int,
        long_period: int,
        invocation_id: str,
    ) -> tuple[float | None, float | None, float | None, float | None]:
        """Calculates current and previous short/long SMAs."""
        logger.debug(
            f"[{self.name} ({invocation_id[:8]})] Calculating indicators with "
            f"short_period={short_period}, long_period={long_period}. "
            f"Historical prices count: {len(historical_prices)}."
        )

        sma_short = calculate_sma(historical_prices, short_period)
        sma_long = calculate_sma(historical_prices, long_period)

        prev_sma_short = None
        prev_sma_long = None

        if len(historical_prices) > 1:
            previous_prices = historical_prices[:-1]
            if len(previous_prices) >= short_period:
                prev_sma_short = calculate_sma(previous_prices, short_period)
            if len(previous_prices) >= long_period:
                prev_sma_long = calculate_sma(previous_prices, long_period)

        logger.info(
            f"[{self.name} ({invocation_id[:8]})] SMAs: CurrShort={sma_short if sma_short is not None else 'N/A'}, "
            f"CurrLong={sma_long if sma_long is not None else 'N/A'}, "
            f"PrevShort={prev_sma_short if prev_sma_short is not None else 'N/A'}, "
            f"PrevLong={prev_sma_long if prev_sma_long is not None else 'N/A'}"
        )
        return sma_short, sma_long, prev_sma_short, prev_sma_long

    def _generate_signal(
        self,
        sma_short: float | None,
        sma_long: float | None,
        prev_sma_short: float | None,
        prev_sma_long: float | None,
        invocation_id: str,
    ) -> str | None:
        """Generates BUY/SELL signal based on SMA crossover."""
        logger.debug(f"[{self.name} ({invocation_id[:8]})] Generating signal...")
        if (
            sma_short is None
            or sma_long is None
            or prev_sma_short is None
            or prev_sma_long is None
        ):
            logger.info(
                f"[{self.name} ({invocation_id[:8]})] Not enough history for signal generation (one or more SMAs are None)."
            )
            return None

        buy_cond1 = prev_sma_short <= prev_sma_long
        buy_cond2 = sma_short > sma_long
        logger.info(
            f"[{self.name} ({invocation_id[:8]})] BUY Check: (Prev Short {prev_sma_short:.2f} <= Prev Long {prev_sma_long:.2f}) = {buy_cond1}, "
            f"(Curr Short {sma_short:.2f} > Curr Long {sma_long:.2f}) = {buy_cond2}"
        )
        if buy_cond1 and buy_cond2:
            logger.info(
                f"[{self.name} ({invocation_id[:8]})] +++ BUY SIGNAL DETECTED +++"
            )
            return "BUY"

        sell_cond1 = prev_sma_short >= prev_sma_long
        sell_cond2 = sma_short < sma_long
        logger.info(
            f"[{self.name} ({invocation_id[:8]})] SELL Check: (Prev Short {prev_sma_short:.2f} >= Prev Long {prev_sma_long:.2f}) = {sell_cond1}, "
            f"(Curr Short {sma_short:.2f} < Curr Long {sma_long:.2f}) = {sell_cond2}"
        )
        if sell_cond1 and sell_cond2:
            logger.info(
                f"[{self.name} ({invocation_id[:8]})] --- SELL SIGNAL DETECTED ---"
            )
            return "SELL"

        logger.info(
            f"[{self.name} ({invocation_id[:8]})] No crossover signal conditions met."
        )
        return None

    def _determine_trade_proposal(
        self,
        signal: str | None,
        current_price: float,
        portfolio_state: PortfolioStateInput,  # Use Pydantic model
        trade_quantity: int,
        current_should_be_long: bool,
        invocation_id: str,
    ) -> dict | None:
        """Determines the trade proposal based on signal and current state."""
        logger.info(
            f"[{self.name} ({invocation_id[:8]})] Determining trade proposal: Signal='{signal}', "
            f"current_price=${current_price:.2f}, current_should_be_long={current_should_be_long}"
        )
        trade_proposal = None
        if signal == "BUY":
            if not current_should_be_long:
                trade_proposal = {
                    "action": "BUY",
                    "ticker": self.ticker,
                    "quantity": trade_quantity,
                    "price": current_price,
                }
                logger.info(
                    f"[{self.name} ({invocation_id[:8]})] Proposing BUY {trade_proposal['quantity']} {trade_proposal['ticker']} @ ${trade_proposal['price']:.2f}"
                )
            else:
                logger.info(
                    f"[{self.name} ({invocation_id[:8]})] BUY Signal, but already long. No trade proposal."
                )
        elif signal == "SELL":
            if current_should_be_long:
                # portfolio_state is now PortfolioStateInput object
                if portfolio_state.shares > 0:
                    trade_proposal = {
                        "action": "SELL",
                        "ticker": self.ticker,
                        "quantity": portfolio_state.shares,  # Sell all
                        "price": current_price,
                    }
                    logger.info(
                        f"[{self.name} ({invocation_id[:8]})] Proposing SELL {trade_proposal['quantity']} {trade_proposal['ticker']} @ ${trade_proposal['price']:.2f}"
                    )
                else:
                    logger.info(
                        f"[{self.name} ({invocation_id[:8]})] SELL Signal, state is long, but no shares held. No trade proposal."
                    )
            else:
                logger.info(
                    f"[{self.name} ({invocation_id[:8]})] SELL Signal, but already flat/short. No trade proposal."
                )

        if not trade_proposal:
            logger.info(
                f"[{self.name} ({invocation_id[:8]})] No trade proposal generated for signal '{signal}' and current_should_be_long={current_should_be_long}."
            )
        return trade_proposal

    async def _perform_risk_check(
        self,
        trade_proposal: dict,
        portfolio_state: PortfolioStateInput,  # Use Pydantic model
        risk_params: dict,  # This contains riskguard_url, max_pos_size, max_concentration
        ctx: InvocationContext,
    ) -> dict | None:
        """Calls the A2A Risk Check tool and returns the result."""
        invocation_id_short = ctx.invocation_id[:8]
        logger.info(
            f"[{self.name} ({invocation_id_short})] Performing A2A Risk Check for trade: {trade_proposal}"
        )

        tool_args = {
            "trade_proposal": trade_proposal,
            "portfolio_state": portfolio_state.model_dump(),  # Convert Pydantic to dict for tool
            "risk_params": risk_params,  # Pass through extracted risk_params
        }
        logger.debug(
            f"[{self.name} ({invocation_id_short})] A2A Tool Args: {tool_args}"
        )

        a2a_risk_tool_instance = next(
            (t for t in self.tools if isinstance(t, A2ARiskCheckTool)), None
        )

        if not a2a_risk_tool_instance:
            logger.error(
                f"[{self.name} ({invocation_id_short})] ERROR - A2A Risk check tool not found."
            )
            return {
                "approved": False,
                "reason": "Internal Error: Risk check tool misconfiguration.",
            }

        adk_tool_context = ToolContext(
            invocation_context=ctx,
            function_call_id=f"risk_check_{invocation_id_short}_{uuid.uuid4().hex[:4]}",
        )
        logger.debug(
            f"[{self.name} ({invocation_id_short})] Created ToolContext for A2A tool call: {adk_tool_context.function_call_id}"
        )

        tool_event_generator = a2a_risk_tool_instance.run_async(
            args=tool_args, tool_context=adk_tool_context
        )

        risk_result = None
        async for tool_event in tool_event_generator:
            logger.debug(
                f"[{self.name} ({invocation_id_short})] Received event from A2A tool: {tool_event.author}"
            )
            if tool_event.author == a2a_risk_tool_instance.name:
                if hasattr(tool_event, "get_function_responses") and callable(
                    getattr(tool_event, "get_function_responses")
                ):
                    response_parts = tool_event.get_function_responses()
                    if response_parts:
                        risk_result = response_parts[0].response
                        logger.info(
                            f"[{self.name} ({invocation_id_short})] Extracted risk result: {risk_result}"
                        )
                        break
                    else:
                        logger.warning(
                            f"[{self.name} ({invocation_id_short})] Warning - Event from {tool_event.author} did not contain FunctionResponse parts."
                        )
                else:
                    logger.warning(
                        f"[{self.name} ({invocation_id_short})] Warning - Event from {tool_event.author} does not have 'get_function_responses' or it's not callable."
                    )
            else:
                logger.debug(
                    f"[{self.name} ({invocation_id_short})] Received intermediate/other event from author: {tool_event.author}"
                )

        if risk_result is None:
            logger.error(
                f"[{self.name} ({invocation_id_short})] Did not receive a valid result from A2A RiskGuard tool after iterating."
            )
            return {
                "approved": False,
                "reason": "A2A Error: No response from RiskGuard tool.",
            }
        return risk_result

    def _process_risk_result(
        self, risk_result: dict, trade_proposal: dict, signal: str, invocation_id: str
    ) -> Event:
        """
        Processes the risk check result and creates the final event with state_delta.
        """
        invocation_id_short = invocation_id[:8]
        logger.info(
            f"[{self.name} ({invocation_id_short})] Processing risk result={risk_result}, "
            f"trade_proposal={trade_proposal}, Original signal='{signal}'"
        )
        approved = risk_result.get("approved", False)
        reason = risk_result.get("reason", "No reason provided.")

        state_delta_content = {}
        new_should_be_long_value = None

        if approved:
            logger.info(
                f"[{self.name} ({invocation_id_short})] Trade APPROVED by RiskGuard. Reason: {reason}"
            )
            if signal == "BUY":
                new_should_be_long_value = True
            elif signal == "SELL":
                new_should_be_long_value = False

            if new_should_be_long_value is not None:
                state_delta_content["should_be_long"] = new_should_be_long_value
                logger.debug(
                    f"[{self.name} ({invocation_id_short})] Setting 'should_be_long' in state_delta to: {new_should_be_long_value}"
                )
            state_delta_content["approved_trade"] = trade_proposal
            final_event_text = f"Trade Approved (A2A): {reason}"
        else:
            logger.info(
                f"[{self.name} ({invocation_id_short})] Trade REJECTED by RiskGuard. Reason: {reason}"
            )
            state_delta_content["rejected_trade_proposal"] = trade_proposal
            final_event_text = f"Trade Rejected (A2A): {reason}"

        logger.info(
            f"[{self.name} ({invocation_id_short})] Final state_delta to be emitted: {state_delta_content}"
        )
        return Event(
            author=self.name,
            content=genai_types.Content(
                parts=[genai_types.Part(text=final_event_text)]
            ),
            actions=EventActions(state_delta=state_delta_content),
        )

    async def _run_async_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        invocation_id_short = ctx.invocation_id[:8]
        logger.info(
            f"[{self.name} ({invocation_id_short})] >>> Invocation START. Session ID: {ctx.session.id} <<<"
        )

        current_should_be_long = ctx.session.state.get("should_be_long", False)
        logger.info(
            f"[{self.name} ({invocation_id_short})] Initial 'should_be_long' from session state: {current_should_be_long}"
        )

        validated_input = self._parse_and_validate_input_pydantic(ctx)
        if validated_input is None:
            logger.warning(
                f"[{self.name} ({invocation_id_short})] Invalid input data (Pydantic). Yielding error event."
            )
            yield Event(
                author=self.name,
                content=genai_types.Content(
                    parts=[
                        genai_types.Part(
                            text="Error: Invalid input data structure or values."
                        )
                    ]
                ),
            )
            logger.info(
                f"[{self.name} ({invocation_id_short})] >>> Invocation END (Invalid Input) <<<"
            )
            return

        # Use validated_input fields directly
        historical_prices = validated_input.historical_prices
        current_price = validated_input.current_price
        portfolio_state = (
            validated_input.portfolio_state
        )  # This is now PortfolioStateInput model
        short_sma_period = validated_input.short_sma_period
        long_sma_period = validated_input.long_sma_period
        trade_quantity = validated_input.trade_quantity
        # Risk params are now part of validated_input, passed to _perform_risk_check
        risk_params_for_tool = {
            "riskguard_url": validated_input.riskguard_url,
            "max_pos_size": validated_input.max_pos_size,
            "max_concentration": validated_input.max_concentration,
        }

        if not historical_prices or current_price is None:
            logger.warning(
                f"[{self.name} ({invocation_id_short})] Insufficient market data. Yielding event."
            )
            yield Event(
                author=self.name,
                content=genai_types.Content(
                    parts=[
                        genai_types.Part(
                            text="No signal due to insufficient market data."
                        )
                    ]
                ),
            )
            logger.info(
                f"[{self.name} ({invocation_id_short})] >>> Invocation END (Insufficient Market Data) <<<"
            )
            return

        sma_short, sma_long, prev_sma_short, prev_sma_long = self._calculate_indicators(
            historical_prices, short_sma_period, long_sma_period, ctx.invocation_id
        )
        if sma_short is None or sma_long is None:
            logger.info(
                f"[{self.name} ({invocation_id_short})] Not enough history for current SMAs. Yielding event."
            )
            yield Event(
                author=self.name,
                content=genai_types.Content(
                    parts=[genai_types.Part(text="No signal yet (calculating SMAs).")]
                ),
            )
            logger.info(
                f"[{self.name} ({invocation_id_short})] >>> Invocation END (Not enough history for SMAs) <<<"
            )
            return

        signal = self._generate_signal(
            sma_short, sma_long, prev_sma_short, prev_sma_long, ctx.invocation_id
        )

        if signal == "SELL" and current_should_be_long and portfolio_state.shares == 0:
            logger.warning(
                f"[{self.name} ({invocation_id_short})] State Correction: SELL Signal, 'should_be_long' is True (from session), but no shares held. Correcting state."
            )
            yield Event(
                author=self.name,
                content=genai_types.Content(
                    parts=[
                        genai_types.Part(
                            text="State correction: Position was long as per session state, but no shares held on SELL signal. Corrected to flat/not long."
                        )
                    ]
                ),
                actions=EventActions(state_delta={"should_be_long": False}),
            )
            logger.info(
                f"[{self.name} ({invocation_id_short})] >>> Invocation END (State Corrected) <<<"
            )
            return

        if signal is None:
            reason_no_signal = (
                "Not enough history for previous SMAs"
                if (prev_sma_short is None or prev_sma_long is None)
                and (sma_short is not None and sma_long is not None)
                else "Conditions not met"
            )
            logger.info(
                f"[{self.name} ({invocation_id_short})] No signal generated. Reason: {reason_no_signal}. Yielding event."
            )
            yield Event(
                author=self.name,
                content=genai_types.Content(
                    parts=[genai_types.Part(text=f"No signal ({reason_no_signal}).")]
                ),
            )
            logger.info(
                f"[{self.name} ({invocation_id_short})] >>> Invocation END (No Signal) <<<"
            )
            return

        trade_proposal = self._determine_trade_proposal(
            signal,
            current_price,
            portfolio_state,
            trade_quantity,
            current_should_be_long,
            ctx.invocation_id,
        )
        if trade_proposal is None:
            logger.info(
                f"[{self.name} ({invocation_id_short})] Signal ('{signal}') generated, but no trade action needed based on current_should_be_long={current_should_be_long}. Yielding event."
            )
            yield Event(
                author=self.name,
                content=genai_types.Content(
                    parts=[
                        genai_types.Part(
                            text="Signal generated, no action needed based on current strategy state."
                        )
                    ]
                ),
            )
            logger.info(
                f"[{self.name} ({invocation_id_short})] >>> Invocation END (No Trade Proposal Needed) <<<"
            )
            return

        logger.info(
            f"[{self.name} ({invocation_id_short})] Trade proposal generated: {trade_proposal}. Yielding informational event before risk check."
        )
        yield Event(
            author=self.name,
            content=genai_types.Content(
                parts=[
                    genai_types.Part(
                        text=f"Proposing {trade_proposal['action']} {trade_proposal['quantity']} {trade_proposal['ticker']} @ ${trade_proposal['price']:.2f} (pending A2A Risk Check)"
                    )
                ]
            ),
        )

        risk_result = None
        try:
            risk_result = await self._perform_risk_check(
                trade_proposal,
                portfolio_state,
                risk_params_for_tool,
                ctx,  # Pass Pydantic portfolio_state and extracted risk_params
            )
        except Exception as e:
            logger.error(
                f"[{self.name} ({invocation_id_short})] Error during risk check tool call: {e}",
                exc_info=True,
            )
            yield Event(
                author=self.name,
                content=genai_types.Content(
                    parts=[genai_types.Part(text="Error during risk check.")]
                ),
            )
            logger.info(
                f"[{self.name} ({invocation_id_short})] >>> Invocation END (Risk Check Error) <<<"
            )
            return

        if risk_result is None:
            logger.error(
                f"[{self.name} ({invocation_id_short})] Risk check returned None unexpectedly. Yielding error event."
            )
            yield Event(
                author=self.name,
                content=genai_types.Content(
                    parts=[
                        genai_types.Part(
                            text="Trade proposal failed (no A2A risk response)."
                        )
                    ]
                ),
            )
            logger.info(
                f"[{self.name} ({invocation_id_short})] >>> Invocation END (Null Risk Result) <<<"
            )
            return

        final_event = self._process_risk_result(
            risk_result, trade_proposal, signal, ctx.invocation_id
        )
        logger.info(
            f"[{self.name} ({invocation_id_short})] Yielding final event: {final_event.content.parts[0].text if final_event.content and final_event.content.parts else 'No Content'}, StateDelta: {final_event.actions.state_delta if final_event.actions else 'No Actions'}"
        )
        yield final_event
        logger.info(
            f"[{self.name} ({invocation_id_short})] >>> Invocation END (Processed) <<<"
        )


root_agent = AlphaBotAgent()
logger.info(
    "AlphaBot root_agent instance created. State 'should_be_long' will be managed via ADK session."
)
