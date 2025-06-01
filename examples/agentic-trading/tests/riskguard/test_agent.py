import json
import pytest
import pytest_asyncio

# ADK Imports
try:
    from google.adk.agents.invocation_context import InvocationContext
    from google.adk.events import Event, EventActions
    from google.adk.sessions import InMemorySessionService, Session
    from google.genai import types as genai_types
except ImportError:
    from tests.adk_mocks import (
        Event,
        EventActions,
        InvocationContext,
        Session,
        genai_types,
        InMemorySessionService,
    )

from common.config import (
    DEFAULT_RISKGUARD_MAX_CONCENTRATION,
    DEFAULT_RISKGUARD_MAX_POS_SIZE,
)
from riskguard.agent import RiskGuardAgent


# --- Fixtures ---

@pytest.fixture
def agent() -> RiskGuardAgent:
    """Provides a RiskGuardAgent instance."""
    return RiskGuardAgent()

@pytest.fixture
def mock_session_service() -> InMemorySessionService:
    """Provides an InMemorySessionService instance."""
    return InMemorySessionService()

@pytest_asyncio.fixture
async def mock_session(mock_session_service: InMemorySessionService) -> Session:
    """Provides an awaited session instance."""
    return await mock_session_service.create_session(app_name="test_app", user_id="test_user")

@pytest_asyncio.fixture
async def mock_ctx(agent: RiskGuardAgent, mock_session_service: InMemorySessionService, mock_session: Session) -> InvocationContext:
    """Provides a base InvocationContext."""
    default_input_data = {"default": "data"}
    # Ensure genai_types.Part is correctly mocked if text is the only arg
    mock_content_part = genai_types.Part(text=json.dumps(default_input_data))
    mock_content = genai_types.Content(parts=[mock_content_part])
    return InvocationContext(
        user_content=mock_content,
        session_service=mock_session_service,
        invocation_id="test_invocation_base",
        agent=agent,
        session=mock_session
    )

def test_riskguard_agent_instantiation(agent: RiskGuardAgent):
    """Tests basic instantiation of the RiskGuardAgent."""
    assert agent is not None
    assert agent.name == "RiskGuard"
    assert agent.description == "Evaluates proposed trades against predefined risk rules."

@pytest.mark.asyncio
async def test_riskguard_run_async_impl_approve(agent, mock_ctx: InvocationContext):
    """Tests _run_async_impl approves a valid trade."""
    ctx = mock_ctx
    input_data = {
        "trade_proposal": {"action": "BUY", "ticker": "TEST", "quantity": 10, "price": 100.0},
        "portfolio_state": {"cash": 10000, "shares": 0, "total_value": 10000, "positions": {}},
        "max_pos_size": DEFAULT_RISKGUARD_MAX_POS_SIZE,
        "max_concentration": DEFAULT_RISKGUARD_MAX_CONCENTRATION
    }
    ctx.user_content = genai_types.Content(parts=[genai_types.Part(text=json.dumps(input_data))])
    ctx.invocation_id = "test_invocation_approve"

    events = []
    async for event in agent._run_async_impl(ctx):
        events.append(event)

    assert len(events) == 1
    final_event = events[0]
    assert final_event.author == agent.name
    assert final_event.turn_complete is True
    assert final_event.content.parts[0].function_response is not None

    result_data = final_event.content.parts[0].function_response.response
    assert result_data["approved"] is True
    assert result_data["reason"] == "Trade adheres to risk rules."

@pytest.mark.asyncio
async def test_riskguard_run_async_impl_reject_pos_size(agent, mock_ctx: InvocationContext):
    """Tests _run_async_impl rejects a trade exceeding max position size."""
    ctx = mock_ctx
    input_data = {
        "trade_proposal": {"action": "BUY", "ticker": "TEST", "quantity": 60, "price": 100.0},
        "portfolio_state": {"cash": 10000, "shares": 0, "total_value": 10000, "positions": {}},
        "max_pos_size": 5000,
        "max_concentration": 0.8
    }
    ctx.user_content = genai_types.Content(parts=[genai_types.Part(text=json.dumps(input_data))])
    ctx.invocation_id = "test_invocation_reject"

    events = []
    async for event in agent._run_async_impl(ctx):
        events.append(event)

    assert len(events) == 1
    final_event = events[0]
    assert final_event.author == agent.name
    assert final_event.turn_complete is True
    assert final_event.content.parts[0].function_response is not None

    result_data = final_event.content.parts[0].function_response.response
    assert result_data["approved"] is False
    assert "Exceeds max position size per trade" in result_data["reason"]
