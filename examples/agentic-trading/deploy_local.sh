#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Starting local services..."

# Ensure we are in the project root directory (where the script is located)
cd "$(dirname "$0")"

# Start RiskGuard (Default Port: 8080 - see common/config.py)
echo "Starting RiskGuard service in the background..."
python -m riskguard &
RISKGUARD_PID=$!
echo "RiskGuard started with PID: $RISKGUARD_PID"

# Start AlphaBot (Default Port: 8081 - see common/config.py)
echo "Starting AlphaBot service in the background..."
python -m alphabot &
ALPHABOT_PID=$!
echo "AlphaBot started with PID: $ALPHABOT_PID"

# Start Simulator UI (Default Port: 8000)
echo "Starting Simulator UI service in the background..."
# Note: Using --host 0.0.0.0 to make it accessible from other devices on the network if needed.
uvicorn simulator.main:app --host 0.0.0.0 --port 8000 &
SIMULATOR_PID=$!
echo "Simulator UI started with PID: $SIMULATOR_PID"

echo "--------------------------------------------------"
echo "Local services started:"
echo "  RiskGuard:   http://127.0.0.1:8080 (PID: $RISKGUARD_PID)" # Assuming default port
echo "  AlphaBot:    http://127.0.0.1:8081 (PID: $ALPHABOT_PID)" # Assuming default port
echo "  Simulator:   http://127.0.0.1:8000 (PID: $SIMULATOR_PID)"
echo "--------------------------------------------------"
echo "Use 'kill $RISKGUARD_PID $ALPHABOT_PID $SIMULATOR_PID' or Ctrl+C in the terminals (if not backgrounded) to stop."

# Optional: Wait for all background processes to finish (uncomment if needed)
# wait
