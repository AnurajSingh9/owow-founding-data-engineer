import sqlite3
from fastapi import FastAPI

app = FastAPI()

# connect to analytics database
conn = sqlite3.connect("analytics.db", check_same_thread=False)
cursor = conn.cursor()


@app.get("/recommendations/{user_id}")
def get_recommendations(user_id: str):
    """
    Returns top campaigns based on engagement frequency.
    """

    cursor.execute(
        """
        SELECT campaign, SUM(count) AS score
        FROM engagement
        GROUP BY campaign
        ORDER BY score DESC
        LIMIT 5
        """
    )

    rows = cursor.fetchall()

    response = []
    for row in rows:
        response.append(
            {
                "campaign": row[0],
                "score": row[1],
            }
        )

    return {
        "user_id": user_id,
        "recommendations": response,
    }
