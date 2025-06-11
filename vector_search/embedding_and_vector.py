# embedding_and_vector.py
"""
Generate embeddings for session summaries and push to Qdrant (community version).
"""
from typing import List, Dict
import requests
import numpy as np

# Example: Use Ollama for local embedding generation
OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings"
OLLAMA_MODEL = "mistral"  # Change as needed

def get_embedding_ollama(text: str, model: str = OLLAMA_MODEL) -> List[float]:
    payload = {"model": model, "prompt": text}
    response = requests.post(OLLAMA_EMBED_URL, json=payload, timeout=60)
    response.raise_for_status()
    return response.json().get("embedding", [])

# Qdrant example (community version)
from qdrant_client import QdrantClient

def push_to_qdrant(session_id: str, embedding: List[float], metadata: Dict, collection_name: str, url: str):
    client = QdrantClient(url=url)
    client.upsert(collection_name=collection_name, points=[{
        "id": session_id,
        "vector": embedding,
        "payload": metadata
    }])
