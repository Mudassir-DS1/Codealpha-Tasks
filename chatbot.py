import spacy

class ChatBot:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.responses = {
            "hello": "Hi there! How can I help you today?",
            "bye": "Goodbye! Have a great day!",
            "how are you": "I'm just a bot, but I'm here to help you!",
            "default": "I'm sorry, I don't understand that."
        }

    def get_response(self, user_input):
        doc = self.nlp(user_input.lower())
        for token in doc:
            if token.lemma_ in self.responses:
                return self.responses[token.lemma_]
        return self.responses["default"]

# Example usage
bot = ChatBot()
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break
    response = bot.get_response(user_input)
    print(f"Bot: {response}")
