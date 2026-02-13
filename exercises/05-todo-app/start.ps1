# PowerShell script to start the Todo Application

Write-Host "🐳 Starting Todo Application..." -ForegroundColor Cyan

# Create network if not exists
docker network create todo-network 2>$null

# Create volume if not exists
docker volume create todo-db-data 2>$null

# Start database
Write-Host "📦 Starting database..." -ForegroundColor Yellow
docker run -d `
  --name todo-db `
  --network todo-network `
  -e POSTGRES_USER=postgres `
  -e POSTGRES_PASSWORD=postgres `
  -e POSTGRES_DB=todos `
  -v todo-db-data:/var/lib/postgresql/data `
  -v ${PWD}/database/init.sql:/docker-entrypoint-initdb.d/init.sql `
  postgres:15-alpine

Write-Host "⏳ Waiting for database to be ready..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

# Build and start backend
Write-Host "🔧 Building and starting backend..." -ForegroundColor Yellow
docker build -t todo-backend:v1 ./backend
docker run -d `
  --name todo-backend `
  --network todo-network `
  -e DB_HOST=todo-db `
  -e DB_NAME=todos `
  -e DB_USER=postgres `
  -e DB_PASSWORD=postgres `
  todo-backend:v1

# Build and start frontend
Write-Host "🌐 Building and starting frontend..." -ForegroundColor Yellow
docker build -t todo-frontend:v1 ./frontend
docker run -d `
  --name todo-frontend `
  --network todo-network `
  -p 8080:80 `
  todo-frontend:v1

Write-Host "✅ Application started! Open http://localhost:8080" -ForegroundColor Green
