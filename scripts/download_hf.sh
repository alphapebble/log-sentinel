#!/bin/bash
# Download Hugging Face models or datasets for log-sentinel

# Example: Download a model (replace with your actual model if needed)
MODEL_NAME=${1:-"sentence-transformers/all-MiniLM-L6-v2"}
TARGET_DIR="./hf_models/${MODEL_NAME//\//_}"

mkdir -p "$TARGET_DIR"

if command -v huggingface-cli >/dev/null 2>&1; then
    echo "Downloading $MODEL_NAME to $TARGET_DIR using huggingface-cli..."
    huggingface-cli download $MODEL_NAME --local-dir "$TARGET_DIR"
else
    echo "huggingface-cli not found. Please install it with: pip install huggingface_hub"
    exit 1
fi

echo "Download complete."
