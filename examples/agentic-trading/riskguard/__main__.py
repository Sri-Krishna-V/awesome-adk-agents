import logging

import click
import common.config as defaults
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill

from .agent import root_agent as riskguard_adk_agent
from .agent_executor import RiskGuardAgentExecutor  # Renamed from RiskGuardTaskManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--host",
    default=defaults.DEFAULT_RISKGUARD_URL.split(":")[1].replace("//", ""),
    help="Host to bind the server to.",
)
@click.option(
    "--port",
    default=int(defaults.DEFAULT_RISKGUARD_URL.split(":")[2]),
    help="Port to bind the server to.",
)
def main(host: str, port: int):
    """Runs the RiskGuard ADK agent as an A2A server."""
    logger.info(f"Configuring RiskGuard A2A server...")

    try:
        agent_card = AgentCard(
            name=riskguard_adk_agent.name,
            description=riskguard_adk_agent.description,
            url=f"http://{host}:{port}",  # SDK expects URL without trailing slash for server itself
            version="1.1.0",
            capabilities=AgentCapabilities(
                streaming=False,
                pushNotifications=False,
            ),
            skills=[
                AgentSkill(
                    id="check_trade_risk",
                    name="Check Trade Risk",
                    description="Validates if a proposed trade meets risk criteria.",
                    examples=["Check if buying 100 TECH_STOCK at $150 is allowed."],
                    tags=[],
                )
            ],
            defaultInputModes=["data"],
            defaultOutputModes=["data"],
        )
    except AttributeError as e:
        logger.error(
            f"Error accessing attributes from riskguard_adk_agent: {e}. Is riskguard/agent.py correct?"
        )
        raise

    try:
        agent_executor = RiskGuardAgentExecutor()
    except Exception as e:
        logger.error(f"Error initializing RiskGuardAgentExecutor: {e}")
        raise

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
        logger.error(f"Error initializing A2AStarletteApplication: {e}")
        raise

    # Start the Server
    import uvicorn

    logger.info(f"Starting RiskGuard A2A server on http://{host}:{port}/")
    uvicorn.run(app_builder.build(), host=host, port=port)


if __name__ == "__main__":
    main()
