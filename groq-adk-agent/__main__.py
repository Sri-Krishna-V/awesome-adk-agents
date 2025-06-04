#!/usr/bin/env python3
"""
Groq ADK Agent - Main entry point
Integrates Groq's compound AI system with Google ADK
"""

import asyncio
import os
import sys
from dotenv import load_dotenv
from google.adk.runners import Runner
from agent import groq_compound_agent, session_service
from task_manager import task_manager

# Load environment variables
load_dotenv()


async def main():
    """Main function to run the Groq ADK agent"""
    print("🚀 Starting Groq ADK Agent...")
    print("📡 Connecting to Groq's compound AI system...")

    # Check for API key
    if not os.getenv("GROQ_API_KEY"):
        print("❌ Error: GROQ_API_KEY not found in environment variables")
        print("Please set your Groq API key in the .env file")
        sys.exit(1)

    # Initialize runner
    runner = Runner(
        agent=groq_compound_agent,
        app_name="groq_adk_agent",
        session_service=session_service
    )

    print("✅ Agent initialized successfully!")
    print("🔧 Compound AI capabilities: Web Search + Code Execution")
    print("💡 Try asking about current events, calculations, or research topics")
    print("\nType 'quit' to exit\n")

    user_id = "cli_user"
    session_id = "cli_session"

    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()

            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("👋 Goodbye!")
                break

            if not user_input:
                continue

            print("🤖 Agent: ", end="", flush=True)

            # Run the agent
            response = await runner.run_async(
                user_id=user_id,
                session_id=session_id,
                message=user_input
            )

            print(response.content)
            print()

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try again.\n")


def run_interactive_demo():
    """Run an interactive demo of different agent capabilities"""
    print("🎯 Groq ADK Agent Demo")
    print("=" * 50)

    demo_queries = [
        ("Current Information", "What are the latest AI breakthroughs in 2025?"),
        ("Calculation", "Calculate the compound interest on $10,000 at 5% annually for 10 years"),
        ("Code Execution", "Write and run Python code to find prime numbers up to 100"),
        ("Research", "Research the environmental impact of electric vehicles vs gasoline cars")
    ]

    async def run_demo():
        for category, query in demo_queries:
            print(f"\n📋 {category} Example:")
            print(f"Query: {query}")
            print("Response: Processing...", end="", flush=True)

            try:
                if category == "Current Information":
                    result = await task_manager.handle_web_search_task(query)
                elif category == "Calculation":
                    result = await task_manager.handle_calculation_task(query)
                elif category == "Research":
                    result = await task_manager.handle_research_task(query)
                else:
                    result = await task_manager.handle_complex_task(query)

                print(f"\r🤖 Response: {result[:200]}...")

            except Exception as e:
                print(f"\r❌ Error: {e}")

    asyncio.run(run_demo())


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Groq ADK Agent")
    parser.add_argument("--demo", action="store_true",
                        help="Run interactive demo")
    parser.add_argument("--chat", action="store_true",
                        help="Start chat interface (default)")

    args = parser.parse_args()

    if args.demo:
        run_interactive_demo()
    else:
        asyncio.run(main())
