from flask import Flask, request, jsonify
from flask_cors import CORS
from huggingface_hub import InferenceClient
import os
import math
import random

app = Flask(__name__)
CORS(app)

# -----------------------------
#  LLaMA MODEL
# -----------------------------
client = InferenceClient(
    model="meta-llama/llama-3.1-8b-instant",
    token=os.getenv("HF_TOKEN")
)

# -----------------------------
#  NGO DATASET
# -----------------------------
NGOS = [
    {"name":"Dubai Food Bank","type":"Food Bank","lat":25.20,"lon":55.27,"capacity":500},
    {"name":"Sharjah Elderly Care Home","type":"Elderly Home","lat":25.34,"lon":55.42,"capacity":120},
    {"name":"UAE Refugee Support Center","type":"Refugee Camp","lat":25.27,"lon":55.29,"capacity":800},
    {"name":"Abu Dhabi Community Kitchen","type":"Food Bank","lat":24.45,"lon":54.37,"capacity":300}
]

# -----------------------------
# 🧠 SCORING ENGINE
# -----------------------------
def score(meals, ngo):

    dist = math.sqrt((ngo["lat"]-25.2)**2 + (ngo["lon"]-55.27)**2)*100
    dist_score = max(0, 100 - dist*10)

    cap_score = min(100, ngo["capacity"]/max(meals,1)*100)

    urgency = 100 if ngo["type"] in ["Refugee Camp","Elderly Home"] else 70

    return round(dist_score*0.4 + cap_score*0.4 + urgency*0.2, 2)

# -----------------------------
#  DYNAMIC LLM REASONING
# -----------------------------
def explain(ngo, meals, foodType, expiry):

    styles = [
        "focus on urgency and humanitarian impact",
        "focus on logistics efficiency",
        "focus on waste reduction",
        "focus on capacity optimization"
    ]

    prompt = f"""
You are a humanitarian AI.

NGO: {ngo['name']}
Type: {ngo['type']}
Meals: {meals}
Food: {foodType}
Expiry: {expiry}

Instruction: {random.choice(styles)}

Give a short unique explanation. Do NOT repeat wording.
"""

    try:
        return client.text_generation(
            prompt,
            max_new_tokens=120,
            temperature=0.9
        )
    except:
        return f"{ngo['name']} is suitable based on demand and capacity."

# -----------------------------
#  API
# -----------------------------
@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    meals = int(data["meals"])
    foodType = data["foodType"]
    expiry = data["expiry"]

    results = []

    for ngo in NGOS:

        s = score(meals, ngo)

        priority = "High" if s > 80 else "Medium" if s > 60 else "Low"

        results.append({
            "recipient": ngo["name"],
            "type": ngo["type"],
            "score": s,
            "km": round(s/10,1),
            "priority": priority,
            "reason": explain(ngo, meals, foodType, expiry)
        })

    return jsonify(sorted(results, key=lambda x: x["score"], reverse=True))

# -----------------------------
@app.route("/")
def home():
    return "NourishNet AI Running 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
