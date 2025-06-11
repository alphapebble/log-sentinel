# embedding_and_vector.py
"""
Generate embeddings for session summaries and push to Pinecone or Qdrant.
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

# Pinecone example
import pinecone

def push_to_pinecone(session_id: str, embedding: List[float], metadata: Dict, index_name: str, api_key: str, env: str):
    pinecone.init(api_key=api_key, environment=env)
    index = pinecone.Index(index_name)
    index.upsert([(session_id, embedding, metadata)])

# Qdrant example
from qdrant_client import QdrantClient

def push_to_qdrant(session_id: str, embedding: List[float], metadata: Dict, collection_name: str, url: str):
    client = QdrantClient(url=url)
    client.upsert(collection_name=collection_name, points=[{
        "id": session_id,
        "vector": embedding,
        "payload": metadata
    }])
