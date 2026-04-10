import os
import json
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_restock_suggestions(items):
    items_text = ""
    for item in items:
        items_text += f"- {item.name}: {item.quantity} units left (category: {item.category})\n"

    prompt = "You are a warehouse inventory analyst.\n\n"
    prompt += "These items are running low on stock:\n"
    prompt += items_text
    prompt += "\nRespond in JSON only, no extra text:\n"
    prompt += '{"suggestions": [{"name": "item name", "priority": "CRITICAL", "reorder_quantity": 50, "reason": "your reason here"}], "summary": "one sentence overall summary"}'

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )

    raw = response.choices[0].message.content.strip()
    print("RAW RESPONSE:", raw)

    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip()

    return json.loads(raw)