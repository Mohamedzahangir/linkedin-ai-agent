from modules.generator import generate_post

if __name__ == "__main__":
    topic = "Automation vs AI Agents in modern systems"
    post = generate_post(topic)

    print("\n" + "=" * 50)
    print("Generated LinkedIn Post:\n")
    print(post)
    print("=" * 50 + "\n")
