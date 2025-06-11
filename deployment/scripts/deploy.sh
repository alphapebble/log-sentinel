#!/bin/bash
# Deployment script for log-sentinel

set -e

# Change to the project root directory
cd "$(dirname "$0")/../.."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Build and start the containers
echo "Building and starting containers..."
docker-compose -f deployment/docker/docker-compose.yml up -d

echo "Deployment complete!"
echo "Backend is running at http://localhost:8000"
echo "ClickHouse at http://localhost:8123, Qdrant at http://localhost:6333, Ollama at http://localhost:11434"
