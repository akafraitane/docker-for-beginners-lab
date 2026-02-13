# PowerShell script to stop the Todo Application

Write-Host "🛑 Stopping Todo Application..." -ForegroundColor Yellow

docker stop todo-frontend todo-backend todo-db 2>$null
docker rm todo-frontend todo-backend todo-db 2>$null

Write-Host "✅ Application stopped!" -ForegroundColor Green
