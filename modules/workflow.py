from modules.generator import generate_post
from modules.memory import init_db, topic_exists, save_post
from modules.topic_manager import get_next_topic


def run_workflow():
    init_db()

    topic = get_next_topic()

    if not topic:
        print("No new topics available.")
        return None

    if topic_exists(topic):
        print("Duplicate detected. Skipping.")
        return None

    post = generate_post(topic)

    save_post(topic, post)

    return post
