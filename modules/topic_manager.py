import random
import sqlite3

DB_PATH = "database/posts.db"


TOPIC_POOL = [
    "AI vs Automation in modern systems",
    "Why consistency beats motivation",
    "The rise of AI agents in 2025",
    "Building in public as a developer",
    "Why most automation projects fail",
    "Prompt engineering vs system design"
]


def get_unused_topics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT topic FROM posts")
    used_topics = {row[0] for row in cursor.fetchall()}

    conn.close()

    return [topic for topic in TOPIC_POOL if topic not in used_topics]


def get_next_topic():
    unused = get_unused_topics()

    if not unused:
        print("⚠ All topics used.")
        return None

    return random.choice(unused)
