# Project Structure Guide

This document explains the organization and purpose of files in the Agentic Trading Simulator.

## 📁 Directory Structure

```
agentic-trading/
├── 📄 README.md                    # Main documentation
├── 📄 TROUBLESHOOTING.md           # Common issues and solutions
├── 📄 requirements.txt             # All dependencies
├── 📄 requirements-dev.txt         # Development/testing dependencies
├── 📄 pyproject.toml              # Python project configuration
├── 📄 setup.ps1                   # Windows setup script
├── 📄 deploy_local.ps1            # Windows deployment script
├── 📄 stop_local.ps1              # Windows service stop script
├── 📄 deploy_local.sh             # Linux/Mac deployment script
├── 📄 Dockerfile                  # Docker container configuration
├── 📄 docker-compose.yml          # Multi-container orchestration
│
├── 📁 alphabot/                   # Trading strategy agent
│   ├── 📄 __init__.py
│   ├── 📄 __main__.py             # Entry point for AlphaBot service
│   ├── 📄 agent.py                # Main AlphaBot agent implementation
│   ├── 📄 agent_executor.py       # ADK agent executor
│   ├── 📄 a2a_risk_tool.py        # Tool for communicating with RiskGuard
│   └── 📄 requirements.txt        # AlphaBot-specific dependencies
│
├── 📁 riskguard/                  # Risk management agent  
│   ├── 📄 __init__.py
│   ├── 📄 __main__.py             # Entry point for RiskGuard service
│   ├── 📄 agent.py                # Main RiskGuard agent implementation
│   ├── 📄 agent_executor.py       # ADK agent executor
│   ├── 📄 rules.py                # Risk assessment rules
│   └── 📄 requirements.txt        # RiskGuard-specific dependencies
│
├── 📁 simulator/                  # Web-based simulation interface
│   ├── 📄 __init__.py
│   ├── 📄 main.py                 # FastAPI web application
│   ├── 📄 market.py               # Market simulation logic
│   ├── 📄 portfolio.py            # Portfolio tracking
│   ├── 📄 requirements.txt        # Simulator-specific dependencies
│   ├── 📁 static/                 # Web assets (CSS, JS, images)
│   └── 📁 templates/              # HTML templates
│
├── 📁 common/                     # Shared configuration and utilities
│   ├── 📄 __init__.py
│   ├── 📄 config.py               # Central configuration settings
│   └── 📁 utils/                  # Shared utility functions
│       └── 📄 indicators.py       # Technical analysis indicators
│
└── 📁 tests/                      # Test suite
    ├── 📄 __init__.py
    ├── 📄 adk_mocks.py            # Mock objects for testing
    ├── 📁 alphabot/               # AlphaBot tests
    └── 📁 riskguard/              # RiskGuard tests
```

## 🔧 Key Components

### AlphaBot Agent (`alphabot/`)
**Purpose**: Implements trading strategy logic
- **`agent.py`**: Core trading strategy (SMA crossover)
- **`a2a_risk_tool.py`**: Communication tool for risk checks
- **Port**: 8081

### RiskGuard Agent (`riskguard/`)  
**Purpose**: Evaluates trade proposals against risk rules
- **`agent.py`**: Risk assessment logic
- **`rules.py`**: Configurable risk management rules
- **Port**: 8080

### Simulator UI (`simulator/`)
**Purpose**: Web interface for running simulations
- **`main.py`**: FastAPI web server
- **`market.py`**: Market data generation and simulation
- **`portfolio.py`**: Portfolio state management
- **Port**: 8000

### Common (`common/`)
**Purpose**: Shared configuration and utilities
- **`config.py`**: Default settings for all services
- **`utils/indicators.py`**: Technical analysis functions

## 🚀 Service Communication Flow

1. **User** interacts with **Simulator UI** (port 8000)
2. **Simulator** sends market data to **AlphaBot** (port 8081) via A2A protocol
3. **AlphaBot** analyzes data and may send trade proposal to **RiskGuard** (port 8080) via A2A
4. **RiskGuard** evaluates trade against risk rules and responds to **AlphaBot**
5. **AlphaBot** sends final trade decision back to **Simulator**
6. **Simulator** updates portfolio and displays results to user

## 📋 File Purposes

### Configuration Files
- **`requirements.txt`**: Aggregates all dependencies from individual services
- **`requirements-dev.txt`**: Development tools (testing, linting, formatting)
- **`pyproject.toml`**: Python project metadata and tool configuration
- **`common/config.py`**: Centralized default settings for ports, URLs, and parameters

### Scripts
- **`setup.ps1`**: Automated setup for Windows (creates venv, installs dependencies)
- **`deploy_local.ps1`**: Starts all services on Windows
- **`stop_local.ps1`**: Stops all services on Windows  
- **`deploy_local.sh`**: Starts all services on Linux/Mac

### Entry Points
- **`alphabot/__main__.py`**: Starts AlphaBot agent service
- **`riskguard/__main__.py`**: Starts RiskGuard agent service
- **`simulator/main.py`**: Starts FastAPI web application

## 🧪 Testing

- **`tests/`**: Contains unit tests for each component
- **`tests/adk_mocks.py`**: Mock objects for testing ADK components
- Run tests: `pytest tests/`

## 🐳 Deployment

- **`Dockerfile`**: Container configuration for cloud deployment
- **`docker-compose.yml`**: Local multi-container setup
- Cloud deployment scripts available for Google Cloud Run

## 💡 Adding New Features

### To add a new trading strategy:
1. Modify `alphabot/agent.py`
2. Update configuration in `common/config.py`
3. Add tests in `tests/alphabot/`

### To add new risk rules:
1. Update `riskguard/rules.py`
2. Modify `riskguard/agent.py` if needed
3. Add tests in `tests/riskguard/`

### To enhance the UI:
1. Modify `simulator/main.py` for backend changes
2. Update templates in `simulator/templates/`
3. Add static assets in `simulator/static/`

This modular structure makes it easy to understand, test, and extend the trading simulation system.
