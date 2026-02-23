import sqlite3
from datetime import datetime

DB_PATH = "database/posts.db"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT UNIQUE,
        content TEXT,
        created_at TEXT,
        likes INTEGER DEFAULT 0,
        comments INTEGER DEFAULT 0,
        impressions INTEGER DEFAULT 0
    )
""")

    conn.commit()
    conn.close()


def topic_exists(topic: str) -> bool:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM posts WHERE topic = ?", (topic,))
    result = cursor.fetchone()

    conn.close()

    return result is not None


def save_post(topic: str, content: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO posts (topic, content, created_at)
        VALUES (?, ?, ?)
    """, (topic, content, datetime.utcnow().isoformat()))

    conn.commit()
    conn.close()

def update_engagement(topic: str, likes: int, comments: int, impressions: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE posts
        SET likes = ?, comments = ?, impressions = ?
        WHERE topic = ?
    """, (likes, comments, impressions, topic))

    conn.commit()
    conn.close()