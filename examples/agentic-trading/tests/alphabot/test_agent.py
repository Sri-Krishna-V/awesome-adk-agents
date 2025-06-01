import pytest
import json
from unittest.mock import AsyncMock

# ADK Imports
try:
    from google.adk.agents.invocation_context import InvocationContext
    from google.genai import types as genai_types
    from google.adk.events import Event, EventActions
    from google.adk.sessions import InMemorySessionService, Session
except ImportError:
    from tests.adk_mocks import (
        InvocationContext, genai_types, Event, EventActions, InMemorySessionService, Session # Import centralized EventActions
    )

from alphabot.agent import AlphaBotAgent, A2ARiskCheckTool
from common.config import DEFAULT_TICKER

def test_alphabot_agent_instantiation():
    """Tests basic instantiation of the AlphaBotAgent."""
    try:
        agent = AlphaBotAgent(stock_ticker="TEST_TICKER")
        assert agent is not None
        assert agent.name == "AlphaBot"
        assert agent.ticker == "TEST_TICKER"
        assert len(agent.tools) == 1
        assert isinstance(agent.tools[0], A2ARiskCheckTool)
        default_agent = AlphaBotAgent()
        assert default_agent.ticker == DEFAULT_TICKER
    except Exception as e:
        pytest.fail(f"AlphaBotAgent instantiation failed: {e}")


@pytest.mark.asyncio
async def test_alphabot_run_async_impl_no_signal():
    """Tests _run_async_impl when no crossover signal is generated."""
    agent = AlphaBotAgent(stock_ticker="TEST")
    agent._should_be_long = False

    mock_a2a_tool = AsyncMock(spec=A2ARiskCheckTool)
    mock_a2a_tool.name = "MockTool" # Tool name for mock Event
    async def mock_run_async(*args, **kwargs):
        # Simulate the tool yielding an event with a function response
        yield Event(
            author=mock_a2a_tool.name, # Event author matches tool name
            content=genai_types.Content(parts=[
                genai_types.Part(function_response=genai_types.FunctionResponse(
                    name=mock_a2a_tool.name, # FunctionResponse name matches tool name
                    response={"approved": True, "reason": "Mock tool approval"}
                ))
            ]),
            turn_complete=True # Typically tool events are turn_complete
        )
        # This 'if False' block is a common pattern for async generators
        # that might conditionally yield more items. It's fine as is.
        if False: # pragma: no cover
             yield

    mock_a2a_tool.run_async = mock_run_async
    agent.tools = [mock_a2a_tool]

    input_data = {
        "historical_prices": [100, 101, 102, 103, 104, 105],
        "current_price": 105.5,
        "portfolio_state": {"cash": 10000, "shares": 0, "total_value": 10000},
        "short_sma_period": 2,
        "long_sma_period": 4,
        "trade_quantity": 10,
        "riskguard_url": "mock_url",
        "max_pos_size": 5000,
        "max_concentration": 0.5,
        "day": 1
    }
    mock_content = genai_types.Content(parts=[genai_types.Part(text=json.dumps(input_data))])
    mock_session_service = InMemorySessionService()
    mock_session_instance: Session = await mock_session_service.create_session(app_name="test_app", user_id="test_user")
    mock_ctx = InvocationContext(
        user_content=mock_content,
        session_service=mock_session_service,
        invocation_id="test_invocation_1",
        agent=agent,
        session=mock_session_instance
    )

    events = []
    async for event in agent._run_async_impl(mock_ctx):
        events.append(event)

    assert len(events) == 1
    final_event = events[0]
    assert final_event.author == agent.name
    assert "No signal (Conditions not met)" in final_event.content.parts[0].text # Assuming text part for no signal

    # Check EventActions (or lack thereof)
    if final_event.actions: # final_event.actions could be None or an EventActions mock
        assert not final_event.actions.state_delta
        assert not final_event.actions.artifact_delta
        assert final_event.actions.transfer_to_agent is None
        assert final_event.actions.escalate is None
        assert not final_event.actions.requested_auth_configs
    else:
        # If no actions are expected, this is also a valid state
        assert final_event.actions is None or not final_event.actions # Handles None or an "empty" EventActions mock
