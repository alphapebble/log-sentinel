#!/bin/bash
# Initialize ClickHouse and Qdrant databases for log-sentinel (reusable for other projects)

# Load environment variables from .env if present
if [ -f .env ]; then
    set -o allexport
    source .env
    set +o allexport
fi

COMPOSE_FILE=${COMPOSE_FILE:-deployment/docker/docker-compose.yml}
CLICKHOUSE_SERVICE=${CLICKHOUSE_SERVICE:-clickhouse}

DOCKER_COMPOSE_BIN="docker compose"

# Function to initialize the ClickHouse database
init_clickhouse() {
    echo "Initializing ClickHouse database..."
    $DOCKER_COMPOSE_BIN -f "$COMPOSE_FILE" exec "$CLICKHOUSE_SERVICE" clickhouse-client --query "CREATE DATABASE IF NOT EXISTS logs;"
}

# Function to initialize the Qdrant database
init_qdrant() {
    echo "Qdrant does not require explicit DB init; collections are created on first use."
}

# Main function
main() {
    # Initialize the ClickHouse database
    init_clickhouse
    
    # Initialize the Qdrant database
    init_qdrant
    
    echo "Database initialization complete."
}

# Run the main function if the script is executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
