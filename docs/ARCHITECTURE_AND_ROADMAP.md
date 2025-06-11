# CyberSec Log Analyzer Documentation

## Architecture Overview

```
[ Raw Logs (VPN, Zscaler, Sysmon, CICIDS) ]
                    ↓
              [ Log Parsers ]
                    ↓
            [ Structured DataFrames ]
       ↙               ↓                ↘
 [ ClickHouse ]   [ DuckDB ]   [ Feature Extractor ]
       ↓                             ↓
[ OLAP Queries ]        [ XGBoost Anomaly Classifier ]
                                     ↓
        [ Sliding Window Summarizer with LLM ]
                                     ↓
                  [ Vector Search with Qdrant ]
                                     ↓
                   [ Dashboard UI / Alerts ]
```

- **Log Parsers:** Python scripts for CICIDS, Sysmon, etc. (see `parsers/`)
- **OLAP Storage:** ClickHouse (cloud/large) and DuckDB (local/EDA)
- **Analytics:** SQL and Python for sessionization, feature extraction, and anomaly queries
- **ML:** XGBoost for anomaly detection
- **LLM:** Ollama for local summarization, embedding
- **Vector Search:** Qdrant for similar incident retrieval
- **Dashboard:** Streamlit/FastAPI frontend (see `app/`)

---

## Roadmap

### Phase 1: MVP
- [x] CICIDS + Sysmon log parsers
- [x] Store parsed logs in DuckDB and ClickHouse
- [x] Simple OLAP queries for IP spikes, login anomalies
- [x] Basic Streamlit/FastAPI dashboard

### Phase 2: Classical ML
- [x] Feature extraction (time/user-based)
- [x] XGBoost anomaly classifier
- [x] Output binary flag with confidence score

### Phase 3: LLM Summarization + Embedding
- [x] Session window summarization (Ollama)
- [x] Embedding generation
- [x] Qdrant vector DB integration

### Phase 4: Final Dashboard
- [ ] Alert viewer with time slider + filters
- [ ] Comparison: LLM summary vs ML flag
- [ ] Similar incidents section (vector DB)

---

## Folder Structure

- `data/` — Raw and processed logs
- `parsers/` — Log parsers (CICIDS, Sysmon, etc.)
- `storage/` — ClickHouse, DuckDB loaders
- `analytics/` — OLAP queries, sessionization
- `ml/` — Feature extraction, XGBoost model
- `llm/` — Summarization, embedding logic
- `vector_search/` — Qdrant utilities
- `app/` — Dashboard UI (Streamlit/FastAPI)
- `notebooks/` — EDA, dev analysis
- `tests/` — Unit/integration tests
- `deployment/` — Docker, scripts

---

## Getting Started

1. Clone the repo and install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Configure `.env` and `deployment/docker/docker-compose.yml` as needed
3. Start services:
   ```sh
   docker compose -f deployment/docker/docker-compose.yml up -d
   ```
4. Run the dashboard:
   ```sh
   streamlit run app/   # or
   uvicorn app.main:app --reload
   ```

---

## Contributing
- See `tests/` for test examples
- Use modular, testable Python code
- Document new modules in this `docs/` folder

---

## References
- [CICIDS 2017 Dataset](https://www.unb.ca/cic/datasets/malmem-2017.html)
- [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
- [DuckDB](https://duckdb.org/), [ClickHouse](https://clickhouse.com/)
- [Ollama](https://ollama.com/), [Qdrant](https://qdrant.tech/)

---

## Maintainers
- [Your Name](mailto:your.email@example.com)

---

*Last updated: 2025-06-11*
