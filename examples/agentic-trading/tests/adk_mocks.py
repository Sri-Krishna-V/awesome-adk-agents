"""Mocks for ADK (Agent Development Kit) classes, used when the actual ADK is not installed.
These mocks aim to provide minimal viable functionality for tests to run.
"""

from unittest.mock import MagicMock


class BaseSessionService(MagicMock):
    """Mock for google.adk.sessions.BaseSessionService."""

    pass


class Session(MagicMock):
    """Mock for google.adk.sessions.Session."""

    pass


class InMemorySessionService(BaseSessionService):
    """Mock for google.adk.sessions.InMemorySessionService."""

    async def create_session(self, app_name: str, user_id: str) -> Session:
        """Mocks the creation of a session."""
        session_mock = Session()
        session_mock.id = f"{app_name}-{user_id}-session"  # Example ID
        return session_mock


class InvocationContext:
    """Mock for google.adk.agents.invocation_context.InvocationContext."""

    def __init__(
        self,
        user_content=None,  # Should be a mock of genai_types.Content
        session_service: InMemorySessionService = None,
        invocation_id: str = None,
        agent=None,  # Agent instance
        session: Session = None,  # Session instance
    ):
        self.user_content = user_content
        self.session_service = session_service
        self.invocation_id = invocation_id
        self.agent = agent
        self.session = session


class genai_types:
    """Mock for the google.genai.types module."""

    class Content(MagicMock):
        """Mock for genai_types.Content."""

        def __init__(self, parts=None, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.parts = parts if parts is not None else []

    class Part(MagicMock):
        """Mock for genai_types.Part."""

        def __init__(
            self, text=None, function_call=None, function_response=None, *args, **kwargs
        ):
            super().__init__(*args, **kwargs)
            if text is not None:
                self.text = text
            if function_call is not None:
                self.function_call = function_call
            if function_response is not None:
                self.function_response = function_response

    class FunctionResponse(MagicMock):
        """Mock for genai_types.FunctionResponse."""

        def __init__(self, name=None, response=None, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.name = name
            self.response = response


class EventActions(MagicMock):
    """Mock for google.adk.events.EventActions."""

    def __init__(
        self,
        skip_summarization=None,
        state_delta=None,
        artifact_delta=None,
        transfer_to_agent=None,
        escalate=None,
        requested_auth_configs=None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.skip_summarization = skip_summarization
        self.state_delta = state_delta if state_delta is not None else {}
        self.artifact_delta = artifact_delta if artifact_delta is not None else {}
        self.transfer_to_agent = transfer_to_agent
        self.escalate = escalate
        self.requested_auth_configs = (
            requested_auth_configs if requested_auth_configs is not None else {}
        )

    def __bool__(self):
        """Define boolean-ness based on whether it has meaningful content."""
        return bool(
            self.state_delta
            or self.artifact_delta
            or self.transfer_to_agent
            or self.escalate
            or self.requested_auth_configs
        )


class Event:
    """Mock for google.adk.events.Event."""

    def __init__(
        self,
        author: str,
        content,
        actions: EventActions = None,
        turn_complete: bool = False,
    ):  # content is genai_types.Content mock
        self.author = author
        self.content = content  # Should be an instance of genai_types.Content (mock)
        self.actions = actions
        self.turn_complete = turn_complete

    def get_function_responses(self):
        """
        Mock for Event.get_function_responses.
        Returns a list of function_response objects from the event's content parts.
        Each object in the list is expected to have a `.name` and `.response` attribute.
        """
        responses = []
        if self.content and hasattr(self.content, "parts"):
            for (
                part_mock
            ) in (
                self.content.parts
            ):  # part_mock is an instance of genai_types.Part (mock)
                if (
                    hasattr(part_mock, "function_response")
                    and part_mock.function_response is not None
                ):
                    # part_mock.function_response is the genai_types.FunctionResponse mock
                    responses.append(part_mock.function_response)
        return responses
