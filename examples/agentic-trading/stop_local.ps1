# PowerShell script to stop local services on Windows
# stop_local.ps1

Write-Host "Stopping local services..." -ForegroundColor Yellow

# Check if PID file exists
if (Test-Path ".\local_pids.txt") {
    try {
        $pids = (Get-Content ".\local_pids.txt").Split(',')
        
        foreach ($pid in $pids) {
            if ($pid -and $pid.Trim() -ne "") {
                $processId = [int]$pid.Trim()
                try {
                    $process = Get-Process -Id $processId -ErrorAction SilentlyContinue
                    if ($process) {
                        Stop-Process -Id $processId -Force
                        Write-Host "Stopped process with PID: $processId" -ForegroundColor Green
                    }
                    else {
                        Write-Host "Process with PID $processId was not running" -ForegroundColor Gray
                    }
                }
                catch {
                    Write-Host "Could not stop process with PID: $processId" -ForegroundColor Red
                }
            }
        }
        
        # Remove the PID file
        Remove-Item ".\local_pids.txt" -ErrorAction SilentlyContinue
        Write-Host "Cleaned up PID file" -ForegroundColor Green
    }
    catch {
        Write-Host "Error reading PID file: $($_.Exception.Message)" -ForegroundColor Red
    }
}
else {
    Write-Host "PID file not found. Attempting to stop services by name..." -ForegroundColor Yellow
    
    # Try to stop processes by name/port
    $processNames = @("python", "uvicorn")
    foreach ($name in $processNames) {
        $processes = Get-Process -Name $name -ErrorAction SilentlyContinue
        foreach ($proc in $processes) {
            # Additional check to make sure we're stopping the right processes
            $commandLine = (Get-WmiObject Win32_Process -Filter "ProcessId = $($proc.Id)").CommandLine
            if ($commandLine -and ($commandLine -like "*riskguard*" -or $commandLine -like "*alphabot*" -or $commandLine -like "*simulator*")) {
                Stop-Process -Id $proc.Id -Force
                Write-Host "Stopped $name process (PID: $($proc.Id))" -ForegroundColor Green
            }
        }
    }
}

Write-Host "Local services cleanup completed." -ForegroundColor Green
