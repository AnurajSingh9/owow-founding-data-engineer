# Architecture Diagram

User conversations are first ingested by a simple data pipeline.
Text messages are converted into embeddings using a sentence transformer model.

Embeddings are stored in a vector store (FAISS) for similarity search.
User and campaign relationships are maintained in a graph layer (Neo4j mock).
Aggregated interaction data is stored in an analytics database (SQLite).

A FastAPI service uses vector similarity, graph relationships, and analytics data to return campaign recommendations.

Additional considerations:
- In-memory caching to reduce latency (Redis-like behavior)
- Basic logging and validation for observability
