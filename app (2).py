from flask import Flask, request, jsonify
from flask_cors import CORS
import random, math

app = Flask(__name__)
CORS(app)

NGOS = [
    {"name":"Dubai Food Bank","type":"Food Bank","lat":25.20,"lon":55.27},
    {"name":"Sharjah Elderly Care","type":"Elderly Home","lat":25.34,"lon":55.42},
    {"name":"UAE Relief Center","type":"Shelter","lat":25.27,"lon":55.29},
    {"name":"Abu Dhabi Kitchen","type":"Kitchen","lat":24.45,"lon":54.37},
    {"name":"Ajman Support Home","type":"Elderly Home","lat":25.41,"lon":55.51}
]

def dist():
    return random.uniform(2,10)

def reason(food, ngo):
    reasons = [
        f"{ngo} has urgent demand for {food}",
        f"{food} matches dietary needs of {ngo}",
        f"High priority distribution zone for {ngo}",
        f"Efficient delivery route for {ngo}"
    ]
    return random.choice(reasons)

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    meals = int(data["meals"])
    foodType = data["foodType"]
    seed = data.get("seed", 1)

    random.seed(seed)

    results = []

    for ngo in NGOS:
        score = random.randint(50,95)

        if meals > 120:
            score += 5

        km = round(dist(),1)

        results.append({
            "recipient": ngo["name"],
            "km": km,
            "score": score,
            "reason": reason(foodType, ngo["name"]),
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    highs = results[:2]
    meds = results[2:4]
    lows = results[4:6]

    final = []

    for r in highs:
        r["priority"] = "High"
        final.append(r)

    for r in meds:
        r["priority"] = "Medium"
        final.append(r)

    for r in lows:
        r["priority"] = "Low"
        final.append(r)

    return jsonify(final)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
