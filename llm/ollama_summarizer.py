# ollama_summarizer.py
"""
Summarize log sessions using a local Ollama LLM model.
"""
import requests
from typing import List

OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "mistral"  # Change to your local model name if needed

def summarize_session_ollama(session_lines: List[str], model: str = OLLAMA_MODEL) -> str:
    prompt = "Summarize the following security log session in plain English, highlighting any suspicious or unusual activity.\n" + "\n".join(session_lines)
    payload = {"model": model, "prompt": prompt, "stream": False}
    response = requests.post(OLLAMA_API_URL, json=payload, timeout=60)
    response.raise_for_status()
    return response.json().get("response", "")
