from modules.generator import generate_post
from modules.memory import init_db, topic_exists, save_post


def run_workflow(topic: str):
    init_db()

    if topic_exists(topic):
        print("\n⚠ This topic already exists in the database. Skipping generation.\n")
        return None

    post = generate_post(topic)

    save_post(topic, post)

    return post
