import spacy

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Define some responses
responses = {
    "greet": "Hello! How can I help you today?",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome! Is there anything else I can help with?",
    "name": "I'm a chatbot created to assist you with your queries.",
    "default": "I'm sorry, I didn't understand that."
}

def get_intent(text):
    doc = nlp(text)
    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey", "greetings"]:
            return "greet"
        elif token.lemma_ in ["bye", "goodbye", "see you"]:
            return "bye"
        elif token.lemma_ in ["thank", "thanks"]:
            return "thanks"
        elif token.lemma_ in ["name"]:
            return "name"
    return "default"

def chatbot_response(user_input):
    intent = get_intent(user_input)
    return responses.get(intent, responses["default"])

# Main loop
print("Chatbot: Hi! I'm your friendly chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:", responses["bye"])
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
