# chatbot.py
from transformers import pipeline
from transformers.pipelines import Conversation

# Load chatbot model once
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Session-level conversation
conversation = None

def get_bot_response(user_input):
    global conversation
    if conversation is None:
        conversation = Conversation(user_input)
    else:
        conversation.add_user_input(user_input)

    chatbot([conversation])
    return conversation.generated_responses[-1]
