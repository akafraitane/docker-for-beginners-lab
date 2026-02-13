# Exercise 05: Todo App (Multi-Container Application)

Build a complete multi-container application with:
- PostgreSQL database
- Python Flask API backend
- Nginx static frontend

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Frontend  │────▶│   Backend   │────▶│  Database   │
│   (Nginx)   │     │   (Flask)   │     │  (Postgres) │
└─────────────┘     └─────────────┘     └─────────────┘
     :80                 :5000              :5432
```

## Quick Start

### Linux/macOS
```bash
chmod +x start.sh stop.sh
./start.sh
```

### Windows (PowerShell)
```powershell
.\start.ps1
```

Then open http://localhost:8080

## Manual Steps

1. Create network and volume:
```bash
docker network create todo-network
docker volume create todo-db-data
```

2. Start PostgreSQL:
```bash
docker run -d \
  --name todo-db \
  --network todo-network \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=todos \
  -v todo-db-data:/var/lib/postgresql/data \
  -v $(pwd)/database/init.sql:/docker-entrypoint-initdb.d/init.sql \
  postgres:15-alpine
```

3. Wait ~10 seconds, then build and start backend:
```bash
docker build -t todo-backend:v1 ./backend
docker run -d \
  --name todo-backend \
  --network todo-network \
  -e DB_HOST=todo-db \
  -e DB_NAME=todos \
  -e DB_USER=postgres \
  -e DB_PASSWORD=postgres \
  todo-backend:v1
```

4. Build and start frontend:
```bash
docker build -t todo-frontend:v1 ./frontend
docker run -d \
  --name todo-frontend \
  --network todo-network \
  -p 8080:80 \
  todo-frontend:v1
```

## Cleanup

### Linux/macOS
```bash
./stop.sh
```

### Windows (PowerShell)
```powershell
.\stop.ps1
```

Or manually:
```bash
docker stop todo-frontend todo-backend todo-db
docker rm todo-frontend todo-backend todo-db
docker network rm todo-network
docker volume rm todo-db-data  # Warning: This deletes data!
```

## Key Concepts Covered

- Multi-container applications
- Docker networking (container DNS)
- Data persistence with volumes
- Environment variables for configuration
- Nginx as reverse proxy
- Database initialization with SQL scripts

## Challenge

1. Add a Redis container for caching
2. Add health checks to all containers
3. Implement proper logging
