from modules.generator import generate_post
from modules.memory import init_db, topic_exists, save_post


def run_workflow():
    topic = "human vs ai- the future of work"

    init_db()

    if topic_exists(topic):
        print("\n⚠ This topic already exists in the database. Skipping generation.\n")
        return

    post = generate_post(topic)

    save_post(topic, post)

    print("\n" + "=" * 50)
    print("Generated and Saved LinkedIn Post:\n")
    print(post)
    print("=" * 50 + "\n")


if __name__ == "__main__":
    run_workflow()
