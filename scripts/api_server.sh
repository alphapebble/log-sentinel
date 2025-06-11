#!/bin/bash
# API server management script for log-sentinel (reusable for other projects)

# Load environment variables from .env if present
if [ -f .env ]; then
    set -o allexport
    source .env
    set +o allexport
fi

API_PORT=${API_PORT:-8000}
COMPOSE_FILE=${COMPOSE_FILE:-deployment/docker/docker-compose.yml}
SERVICE_NAME=${SERVICE_NAME:-backend}

DOCKER_COMPOSE_BIN="docker compose"

start_api() {
    echo "Starting API server ($SERVICE_NAME) on port $API_PORT..."
    $DOCKER_COMPOSE_BIN -f "$COMPOSE_FILE" up -d "$SERVICE_NAME"
    echo "API server should be running at http://localhost:$API_PORT"
}

stop_api() {
    echo "Stopping API server ($SERVICE_NAME)..."
    $DOCKER_COMPOSE_BIN -f "$COMPOSE_FILE" stop "$SERVICE_NAME"
}

restart_api() {
    stop_api
    sleep 2
    start_api
}

status_api() {
    $DOCKER_COMPOSE_BIN -f "$COMPOSE_FILE" ps "$SERVICE_NAME"
}

case $1 in
    start)
        start_api
        ;;
    stop)
        stop_api
        ;;
    restart)
        restart_api
        ;;
    status)
        status_api
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        echo "Set API_PORT, COMPOSE_FILE, and SERVICE_NAME in .env to reuse for other projects."
        exit 1
        ;;
esac
