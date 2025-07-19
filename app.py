# app.py
from flask import Flask, render_template, request, jsonify
from chatbot import get_bot_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    bot_reply = get_bot_response(user_input)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
