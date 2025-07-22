# Black Bucks Chatbot Project

This project is a conversational chatbot built using Python and the HuggingFace Transformers library. It uses the `microsoft/DialoGPT-medium` model and is deployed with Flask for easy interaction via a web interface.

## 🚀 Features
- Responds to user messages with AI-generated replies
- Built using `transformers` and `Flask`
- Simple HTML frontend (`index.html`)
- Persistent conversation flow

## 📁 Project Structure
├── app.py # Flask server
├── bot.py # Chatbot logic using DialoGPT
├── chatbot.py # Conversation pipeline
├── templates/
│ └── index.html # Frontend interface
├── requirements.txt # Dependencies (Flask, transformers, etc.)
## ▶️ How to Run
1. Install dependencies:
pip install -r requirements.txt
2. Start the server:
python app.py
3. Open a browser and go to:
http://127.0.0.1:5000/
