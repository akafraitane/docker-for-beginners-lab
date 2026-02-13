#!/bin/bash

echo "🛑 Stopping Todo Application..."

docker stop todo-frontend todo-backend todo-db 2>/dev/null
docker rm todo-frontend todo-backend todo-db 2>/dev/null

echo "✅ Application stopped!"
