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
👉If you're opening this project from GitHub and want to run it on your local machine, follow these simple steps:

📦 1. Clone the Repository
git clone (paste the link)
cd (paste project name)
⚙️ 2. Install Required Libraries
Make sure you have Python installed. Then, install all required libraries using:

pip install -r requirements.txt
This will automatically install everything like transformers, flask, and more.

🧠 3. Run the Chatbot
To start the chatbot backend:
python app.py
Then open your browser and go to:
http://localhost:5000
📁 Project Files Overview
app.py	Flask server that connects frontend to chatbot
chatbot.py	Core chatbot logic using DialoGPT
index.html	Frontend user interface for the chatbot
requirements.txt	List of libraries to install

