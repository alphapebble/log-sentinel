#!/bin/bash
# Ollama management script for log-sentinel (reusable for other projects)

# Load environment variables from .env if present
if [ -f .env ]; then
    set -o allexport
    source .env
    set +o allexport
fi

OLLAMA_PORT=${OLLAMA_PORT:-11434}
COMPOSE_FILE=${COMPOSE_FILE:-deployment/docker/docker-compose.yml}
OLLAMA_SERVICE=${OLLAMA_SERVICE:-ollama}

DOCKER_COMPOSE_BIN="docker compose"

start_ollama() {
    echo "Starting Ollama service ($OLLAMA_SERVICE) on port $OLLAMA_PORT..."
    $DOCKER_COMPOSE_BIN -f "$COMPOSE_FILE" up -d "$OLLAMA_SERVICE"
    echo "Ollama should be running at http://localhost:$OLLAMA_PORT"
}

stop_ollama() {
    echo "Stopping Ollama service ($OLLAMA_SERVICE)..."
    $DOCKER_COMPOSE_BIN -f "$COMPOSE_FILE" stop "$OLLAMA_SERVICE"
}

status_ollama() {
    $DOCKER_COMPOSE_BIN -f "$COMPOSE_FILE" ps "$OLLAMA_SERVICE"
}

check_model() {
    local model_name="$1"
    if command -v curl >/dev/null 2>&1; then
        curl -s http://localhost:$OLLAMA_PORT/api/tags | grep -q "\"name\":\"$model_name\""
        if [ $? -eq 0 ]; then
            echo "Model $model_name is available in Ollama."
        else
            echo "Model $model_name is NOT available in Ollama."
        fi
    else
        echo "curl not found. Cannot check model availability."
    fi
}

case "$1" in
    start)
        start_ollama
        ;;
    stop)
        stop_ollama
        ;;
    status)
        status_ollama
        ;;
    check-model)
        check_model "$2"
        ;;
    *)
        echo "Usage: $0 {start|stop|status|check-model <model_name>}"
        echo "Set OLLAMA_PORT, COMPOSE_FILE, and OLLAMA_SERVICE in .env to reuse for other projects."
        exit 1
        ;;
esac
