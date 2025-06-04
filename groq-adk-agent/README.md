# Groq ADK Agent

A powerful AI agent built with Groq API and Agent Development Kit (ADK) capabilities.

## Features

- **Fast AI Processing**: Leverages Groq's lightning-fast inference
- **Task Management**: Built-in task scheduling and management system
- **Multiple Models**: Support for various Groq models
- **Interactive Mode**: Command-line interface for real-time interaction
- **Configurable**: Environment-based configuration
- **Extensible**: Modular design for easy customization

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API key

### Installation

1. Clone or navigate to the project directory:
   ```bash
   cd groq-adk-agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your Groq API key
   ```

### Usage

#### Interactive Mode
```bash
python -m groq-adk-agent --interactive
```

#### Single Request
```bash
python -m groq-adk-agent --request "What is artificial intelligence?"
```

#### Show Capabilities
```bash
python -m groq-adk-agent --capabilities
```

#### Run as Module
```python
from agent import GroqADKAgent

agent = GroqADKAgent()
response = agent.process_request("Hello, world!")
print(response)
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GROQ_API_KEY` | Your Groq API key | Required |
| `GROQ_MODEL` | Model to use | `llama-3.1-70b-versatile` |
| `DEBUG` | Enable debug mode | `false` |
| `LOG_LEVEL` | Logging level | `INFO` |

### Supported Models

- `llama-3.1-70b-versatile` (default)
- `llama-3.1-8b-instant`
- `mixtral-8x7b-32768`
- `gemma2-9b-it`

## Project Structure

```
groq-adk-agent/
├── agent.py              # Main agent implementation
├── task_manager.py       # Task management system
├── __main__.py          # CLI entry point
├── .well-known/
│   └── agent.json       # Agent metadata
├── requirements.txt     # Python dependencies
├── .env                # Environment configuration
└── README.md           # This file
```

## API Reference

### GroqADKAgent

Main agent class that handles request processing.

#### Methods

- `process_request(request: str) -> Dict[str, Any]`: Process a text request
- `get_capabilities() -> List[str]`: Get agent capabilities

### TaskManager

Manages task scheduling and execution.

#### Methods

- `create_task(description: str, priority: int) -> str`: Create a new task
- `get_task(task_id: str) -> Optional[Task]`: Get task by ID
- `get_pending_tasks() -> List[Task]`: Get all pending tasks
- `get_task_stats() -> Dict[str, int]`: Get task statistics

## Development

### Adding New Features

1. Extend the `GroqADKAgent` class in `agent.py`
2. Add new task types in `task_manager.py` if needed
3. Update the capabilities list
4. Add corresponding CLI commands in `__main__.py`

### Testing

```bash
# Run the agent with a test request
python -m groq-adk-agent --request "Test message"

# Check capabilities
python -m groq-adk-agent --capabilities
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions:
- Check the documentation
- Review existing issues
- Create a new issue with detailed information

---

Built with ❤️ using Groq and ADK
