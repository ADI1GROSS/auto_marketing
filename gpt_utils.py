import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_ad_text(prompt: str) -> str:
    system_prompt = (
        "You are a Facebook ad copywriter. Your job is to write a short, catchy ad "
        "that encourages people to click or buy. Keep it informal, friendly, and persuasive."
    )
    user_message = f"I want to advertise the following: {prompt}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7
    )

    return response.choices[0].message["content"].strip()
