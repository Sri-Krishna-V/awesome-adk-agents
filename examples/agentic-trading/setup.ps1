# PowerShell setup script for Agentic Trading Simulator
# setup.ps1

Write-Host "🤖 Agentic Trading Simulator - Setup Script" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan

# Check if Python is installed
try {
    $pythonVersion = python --version 2>$null
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "❌ Python not found. Please install Python 3.11+ from https://python.org" -ForegroundColor Red
    exit 1
}

# Check Python version
$pythonVersionOutput = python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
$majorMinor = $pythonVersionOutput.Split('.')
$major = [int]$majorMinor[0]
$minor = [int]$majorMinor[1]

if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 11)) {
    Write-Host "❌ Python 3.11+ is required. Current version: $pythonVersion" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Python version is compatible" -ForegroundColor Green

# Create virtual environment
Write-Host ""
Write-Host "📦 Setting up virtual environment..." -ForegroundColor Yellow

if (Test-Path "venv") {
    Write-Host "Virtual environment already exists. Removing old one..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force "venv"
}

python -m venv venv
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to create virtual environment" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Virtual environment created" -ForegroundColor Green

# Activate virtual environment
Write-Host "🔄 Activating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"

# Upgrade pip
Write-Host "📈 Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Install dependencies
Write-Host "📚 Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to install dependencies" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Dependencies installed successfully" -ForegroundColor Green

# Run a quick test to verify installation
Write-Host ""
Write-Host "🧪 Running installation verification..." -ForegroundColor Yellow

try {
    python -c "import google.adk; import pandas; import fastapi; import plotly; print('All imports successful')"
    Write-Host "✅ Installation verification passed" -ForegroundColor Green
}
catch {
    Write-Host "❌ Installation verification failed" -ForegroundColor Red
    Write-Host "Some dependencies may not have installed correctly." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "🎉 Setup completed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Run '.\deploy_local.ps1' to start all services" -ForegroundColor White
Write-Host "2. Open http://127.0.0.1:8000 in your browser" -ForegroundColor White
Write-Host "3. Use '.\stop_local.ps1' to stop services when done" -ForegroundColor White
Write-Host ""
Write-Host "For development:" -ForegroundColor Cyan
Write-Host "• Run 'pytest tests/' to run tests" -ForegroundColor White
Write-Host "• Use 'black .' and 'isort .' for code formatting" -ForegroundColor White
Write-Host ""
Write-Host "Need help? Check the README.md file for detailed documentation." -ForegroundColor Gray
