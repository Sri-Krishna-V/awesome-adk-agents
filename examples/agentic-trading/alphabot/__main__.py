import logging

import click
import common.config as defaults
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill

# Import the specific AgentExecutor for AlphaBot
from .agent_executor import AlphaBotAgentExecutor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--host",
    default=defaults.DEFAULT_ALPHABOT_URL.split(":")[1].replace("//", ""),
    help="Host to bind the server to.",
)
@click.option(
    "--port",
    default=int(defaults.DEFAULT_ALPHABOT_URL.split(":")[2]),
    help="Port to bind the server to.",
)
def main(host: str, port: int):
    """Runs the AlphaBot agent as an A2A server."""
    logger.info("Configuring AlphaBot A2A server...")

    # Define the Agent Card for AlphaBot
    try:
        agent_card = AgentCard(
            name="AlphaBot Agent",
            description="Trading agent that analyzes market data and portfolio state to propose trades.",
            url=f"http://{host}:{port}",  # SDK expects URL without trailing slash for server itself
            version="1.0.0",
            capabilities=AgentCapabilities(
                streaming=False,  # AlphaBotTaskManager doesn't support streaming
                pushNotifications=False,  # Not implemented
            ),
            skills=[
                AgentSkill(
                    id="provide_trade_signal",
                    name="Provide Trade Signal",
                    description="Analyzes market and portfolio data to decide whether to buy, sell, or hold.",
                    examples=[
                        "Given market data and portfolio, what trade should I make?"
                    ],
                    tags=[],
                )
            ],
            defaultInputModes=[
                "data"
            ],  # Expects market/portfolio state as structured data
            defaultOutputModes=["data"],  # Returns trade decision as structured data
        )
    except Exception as e:
        logger.exception("Error creating AgentCard")
        raise

    # Instantiate the AlphaBot AgentExecutor
    try:
        agent_executor = AlphaBotAgentExecutor()
    except Exception as e:
        logger.exception("Error initializing AlphaBotAgentExecutor")
        raise

    # Instantiate the A2AStarletteApplication
    task_store = InMemoryTaskStore()
    request_handler = DefaultRequestHandler(
        agent_executor=agent_executor, task_store=task_store
    )
    try:
        app_builder = A2AStarletteApplication(
            agent_card=agent_card,
            http_handler=request_handler,
        )
    except Exception as e:
        logger.exception("Error initializing A2AStarletteApplication")
        raise

    # Start the Server
    import uvicorn

    logger.info(f"Starting AlphaBot A2A server on http://{host}:{port}/")
    uvicorn.run(app_builder.build(), host=host, port=port)


if __name__ == "__main__":
    # Example: python -m alphabot --port 8081
    main()
