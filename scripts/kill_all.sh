#!/bin/bash
# Kill all log-sentinel-related containers and processes (reusable for other projects)

# Load environment variables from .env if present
if [ -f .env ]; then
    set -o allexport
    source .env
    set +o allexport
fi

COMPOSE_FILE=${COMPOSE_FILE:-deployment/docker/docker-compose.yml}

echo "Stopping all Docker Compose services defined in $COMPOSE_FILE..."
docker compose -f "$COMPOSE_FILE" down

echo "If you have any local Python processes to kill, use:"
echo "  pkill -f 'uvicorn app.main:app'"
echo "  pkill -f 'streamlit run'"
echo "All log-sentinel services stopped."
