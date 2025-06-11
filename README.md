# CyberSec Log Analyzer

A modern cybersecurity log analyzer for ingesting, parsing, analyzing, and visualizing security logs using Python, ClickHouse, DuckDB, XGBoost, and LLMs. 

## Features
- Multi-format log parsing (Sysmon, CICIDS, Zscaler, VPN)
- OLAP storage with ClickHouse & DuckDB
- Anomaly detection with XGBoost
- LLM-based summarization (GPT-4, Mistral, Ollama)
- Vector search (Pinecone/Qdrant)
- Streamlit/FastAPI dashboard

## Quick Start
1. Clone the repo and install dependencies (see below)
2. Configure `.env` and `docker-compose.yml` as needed
3. Run the dashboard: `streamlit run app/` or `uvicorn app.main:app --reload`

## Folder Structure
- `data/` - Raw and processed logs
- `parsers/` - Log parsers
- `storage/` - OLAP loaders and schema
- `analytics/` - SQL/Python analytics
- `ml/` - Feature extraction & ML
- `llm/` - Summarization & embeddings
- `vector_search/` - Vector DB utils
- `app/` - Dashboard UI
- `notebooks/` - EDA and dev analysis
- `tests/` - Unit/integration tests

## Requirements
- Python 3.10+
- Docker (for ClickHouse, Pinecone, etc.)
- See `requirements.txt` for Python deps

## License
MIT
