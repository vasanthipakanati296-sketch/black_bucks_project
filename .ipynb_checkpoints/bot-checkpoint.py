from transformers import pipeline, Conversation

# Load the pre-trained DialoGPT model
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Start a conversation loop
print("🤖 Chatbot is ready! Type 'exit' to quit.")

conversation = None

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Create or continue the conversation
    if conversation is None:
        conversation = Conversation(user_input)
    else:
        conversation.add_user_input(user_input)

    # Get response
    response = chatbot([conversation])
    print("Bot:", conversation.generated_responses[-1])
