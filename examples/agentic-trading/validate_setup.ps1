# PowerShell script to validate the Agentic Trading setup
# validate_setup.ps1

Write-Host "🔍 Agentic Trading Simulator - Setup Validation" -ForegroundColor Cyan
Write-Host "=================================================" -ForegroundColor Cyan

$allGood = $true

# Check Python version
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>$null
    if ($pythonVersion -match "Python (\d+)\.(\d+)") {
        $major = [int]$matches[1]
        $minor = [int]$matches[2]
        if ($major -ge 3 -and $minor -ge 11) {
            Write-Host "✅ Python: $pythonVersion" -ForegroundColor Green
        }
        else {
            Write-Host "❌ Python version too old: $pythonVersion (3.11+ required)" -ForegroundColor Red
            $allGood = $false
        }
    }
    else {
        Write-Host "❌ Could not determine Python version" -ForegroundColor Red
        $allGood = $false
    }
}
catch {
    Write-Host "❌ Python not found or not accessible" -ForegroundColor Red
    $allGood = $false
}

# Check if virtual environment exists
Write-Host "Checking virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "✅ Virtual environment found" -ForegroundColor Green
}
else {
    Write-Host "⚠️  Virtual environment not found (run setup.ps1 first)" -ForegroundColor Yellow
    $allGood = $false
}

# Check if virtual environment is activated (if it exists)
if (Test-Path "venv") {
    Write-Host "Checking if virtual environment is activated..." -ForegroundColor Yellow
    $pythonPath = (Get-Command python).Source
    if ($pythonPath -like "*venv*") {
        Write-Host "✅ Virtual environment is activated" -ForegroundColor Green
    }
    else {
        Write-Host "⚠️  Virtual environment not activated" -ForegroundColor Yellow
        Write-Host "   Run: .\venv\Scripts\Activate.ps1" -ForegroundColor Gray
    }
}

# Check key dependencies
Write-Host "Checking key dependencies..." -ForegroundColor Yellow
$dependencies = @(
    @{name="google-adk"; import="google.adk"},
    @{name="fastapi"; import="fastapi"},
    @{name="pandas"; import="pandas"},
    @{name="plotly"; import="plotly"},
    @{name="a2a-sdk"; import="a2a"}
)

foreach ($dep in $dependencies) {
    try {
        $result = python -c "import $($dep.import); print('OK')" 2>$null
        if ($result -eq "OK") {
            Write-Host "✅ $($dep.name)" -ForegroundColor Green
        }
        else {
            Write-Host "❌ $($dep.name) - Import failed" -ForegroundColor Red
            $allGood = $false
        }
    }
    catch {
        Write-Host "❌ $($dep.name) - Not installed or import error" -ForegroundColor Red
        $allGood = $false
    }
}

# Check ports availability
Write-Host "Checking port availability..." -ForegroundColor Yellow
$ports = @(8000, 8080, 8081)
foreach ($port in $ports) {
    try {
        $listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Any, $port)
        $listener.Start()
        $listener.Stop()
        Write-Host "✅ Port $port is available" -ForegroundColor Green
    }
    catch {
        Write-Host "⚠️  Port $port is in use" -ForegroundColor Yellow
        Write-Host "   Run: .\stop_local.ps1 to stop existing services" -ForegroundColor Gray
    }
}

# Check file structure
Write-Host "Checking project structure..." -ForegroundColor Yellow
$requiredPaths = @(
    "alphabot/agent.py",
    "riskguard/agent.py", 
    "simulator/main.py",
    "common/config.py",
    "requirements.txt"
)

foreach ($path in $requiredPaths) {
    if (Test-Path $path) {
        Write-Host "✅ $path" -ForegroundColor Green
    }
    else {
        Write-Host "❌ Missing: $path" -ForegroundColor Red
        $allGood = $false
    }
}

# Final assessment
Write-Host ""
Write-Host "=================================================" -ForegroundColor Cyan
if ($allGood) {
    Write-Host "🎉 Setup validation passed!" -ForegroundColor Green
    Write-Host ""
    Write-Host "You're ready to run the simulator:" -ForegroundColor White
    Write-Host "1. Run: .\deploy_local.ps1" -ForegroundColor Cyan
    Write-Host "2. Open: http://127.0.0.1:8000" -ForegroundColor Cyan
    Write-Host "3. Stop: .\stop_local.ps1" -ForegroundColor Cyan
}
else {
    Write-Host "❌ Setup validation failed!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please fix the issues above and try again." -ForegroundColor White
    Write-Host "Need help? Check TROUBLESHOOTING.md" -ForegroundColor Gray
}
Write-Host "=================================================" -ForegroundColor Cyan
