from flask import Flask, request, jsonify, send_file
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    prompt = f"""
    You are a calm, empathetic mental health assistant.

    User says: {user_input}

    Respond with:
    - empathy
    - validation
    - simple actionable advice
    - short and supportive tone
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)