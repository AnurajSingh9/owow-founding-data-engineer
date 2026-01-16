import json
import sqlite3

import numpy as np
import networkx as nx
from sentence_transformers import SentenceTransformer


def load_conversations(path):
    with open(path, "r") as f:
        return json.load(f)


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def main():
    conversations = load_conversations("data/conversations.json")

    model = SentenceTransformer("all-MiniLM-L6-v2")

    conn = sqlite3.connect("analytics.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS engagement (user_id TEXT, campaign TEXT, count INTEGER)"
    )

    graph = nx.Graph()
    embeddings = []

    for item in conversations:
        user_id = item["user_id"]
        campaign = item["campaign"]
        message = item["message"]

        vector = model.encode(message)
        embeddings.append(
            {
                "user_id": user_id,
                "campaign": campaign,
                "vector": vector,
            }
        )

        graph.add_edge(user_id, campaign)

        cursor.execute(
            "INSERT INTO engagement VALUES (?, ?, ?)",
            (user_id, campaign, 1),
        )

    conn.commit()
    conn.close()

    print("data pipeline completed successfully")


if __name__ == "__main__":
    main()
