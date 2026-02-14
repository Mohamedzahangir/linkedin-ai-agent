from openai import OpenAI
from config import OPENROUTER_API_KEY

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def generate_post(topic: str) -> str:
    prompt = f"""
You are an AI & Data Science student building a personal brand.

Write a professional LinkedIn post about: "{topic}"

Requirements:
- Strong opening hook
- Clear structured paragraphs
- Insightful but concise
- Professional tone
- Add spacing between paragraphs
- End with a thoughtful closing line
"""

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {"role": "system", "content": "You are a professional LinkedIn content strategist."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
