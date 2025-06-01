# PowerShell script to deploy local services on Windows
# deploy_local.ps1

Write-Host "Starting local services..." -ForegroundColor Green

# Ensure we are in the project root directory
Set-Location $PSScriptRoot

# Function to check if a port is available
function Test-Port {
    param([int]$Port)
    try {
        $listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Any, $Port)
        $listener.Start()
        $listener.Stop()
        return $true
    }
    catch {
        return $false
    }
}

# Check if required ports are available
$ports = @(8080, 8081, 8000)
foreach ($port in $ports) {
    if (-not (Test-Port $port)) {
        Write-Host "Error: Port $port is already in use. Please stop the service using that port." -ForegroundColor Red
        exit 1
    }
}

Write-Host "All required ports (8000, 8080, 8081) are available." -ForegroundColor Green

# Start RiskGuard service (Port 8080)
Write-Host "Starting RiskGuard service..." -ForegroundColor Yellow
$riskguard = Start-Process python -ArgumentList "-m", "riskguard" -PassThru -WindowStyle Hidden
Write-Host "RiskGuard started with PID: $($riskguard.Id)" -ForegroundColor Green

# Wait a moment for the service to start
Start-Sleep -Seconds 2

# Start AlphaBot service (Port 8081)
Write-Host "Starting AlphaBot service..." -ForegroundColor Yellow
$alphabot = Start-Process python -ArgumentList "-m", "alphabot" -PassThru -WindowStyle Hidden
Write-Host "AlphaBot started with PID: $($alphabot.Id)" -ForegroundColor Green

# Wait a moment for the service to start
Start-Sleep -Seconds 2

# Start Simulator UI service (Port 8000)
Write-Host "Starting Simulator UI service..." -ForegroundColor Yellow
$simulator = Start-Process uvicorn -ArgumentList "simulator.main:app", "--host", "0.0.0.0", "--port", "8000" -PassThru -WindowStyle Hidden
Write-Host "Simulator UI started with PID: $($simulator.Id)" -ForegroundColor Green

# Wait for services to fully start
Write-Host "Waiting for services to start..." -ForegroundColor Yellow
Start-Sleep -Seconds 5

Write-Host "================================================================" -ForegroundColor Cyan
Write-Host "Local services started successfully:" -ForegroundColor Green
Write-Host "  🛡️  RiskGuard:   http://127.0.0.1:8080 (PID: $($riskguard.Id))" -ForegroundColor White
Write-Host "  🤖 AlphaBot:    http://127.0.0.1:8081 (PID: $($alphabot.Id))" -ForegroundColor White
Write-Host "  📊 Simulator:   http://127.0.0.1:8000 (PID: $($simulator.Id))" -ForegroundColor White
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "🌐 Open your browser and navigate to: http://127.0.0.1:8000" -ForegroundColor Green
Write-Host ""
Write-Host "To stop all services, run: .\stop_local.ps1" -ForegroundColor Yellow
Write-Host "Or manually kill processes with PIDs: $($riskguard.Id), $($alphabot.Id), $($simulator.Id)" -ForegroundColor Yellow

# Save PIDs to a file for easy cleanup
"$($riskguard.Id),$($alphabot.Id),$($simulator.Id)" | Out-File -FilePath ".\local_pids.txt" -Encoding UTF8

Write-Host ""
Write-Host "Press Ctrl+C to stop monitoring or close this window." -ForegroundColor Gray
Write-Host "Services will continue running in the background." -ForegroundColor Gray

# Keep the script running to monitor services
try {
    while ($true) {
        Start-Sleep -Seconds 30
        # Check if services are still running
        $runningServices = 0
        if (Get-Process -Id $riskguard.Id -ErrorAction SilentlyContinue) { $runningServices++ }
        if (Get-Process -Id $alphabot.Id -ErrorAction SilentlyContinue) { $runningServices++ }
        if (Get-Process -Id $simulator.Id -ErrorAction SilentlyContinue) { $runningServices++ }
        
        if ($runningServices -eq 0) {
            Write-Host "All services have stopped." -ForegroundColor Red
            break
        }
    }
}
catch {
    Write-Host "Monitoring stopped." -ForegroundColor Yellow
}
