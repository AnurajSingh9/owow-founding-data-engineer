# Architecture

The goal of this system is to show how different types of data can work together to support AI-driven personalization.

Conversation data comes in as raw text along with user and campaign details.
This data is processed by a Python-based pipeline that handles ingestion, embedding generation, and storage.

Text embeddings are generated using a sentence transformer model and stored in a vector store (FAISS). This allows similarity search between users or messages.

User-to-campaign relationships are maintained in a graph layer. In this prototype, the graph is mocked, but in a real system this would be handled using Neo4j to support traversal and relationship queries.

Aggregated interaction metrics are stored in an analytics database (SQLite here).
This simulates how data would be synced to BigQuery for reporting and ranking.

A FastAPI service ties everything together by querying the vector store, graph relationships, and analytics data to return ranked campaign recommendations.

Some infrastructure components are intentionally simplified to keep the assignment easy to run locally while still demonstrating real-world design thinking.
