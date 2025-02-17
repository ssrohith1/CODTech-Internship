import random
import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Predefined responses
responses = {
    "greeting": [
        "Hello! How can I assist you today?", 
        "Hi there! What can I do for you?", 
        "Hey! Need any help?",
        "Good to see you! How can I help?",
        "Hi! What’s on your mind today?"
    ],
    "goodbye": [
        "Goodbye! Have a great day!", 
        "See you later!", 
        "Bye! Take care!",
        "Farewell! Hope to chat again soon!",
        "Take care! Looking forward to our next chat!"
    ],
    "thanks": [
        "You're welcome!", 
        "No problem!", 
        "Glad I could help!",
        "Anytime! Let me know if you need more help!",
        "You're very welcome!"
    ],
    "help": [
        "I’m here to help! What do you need?", 
        "How can I assist you today?", 
        "Tell me what you need help with, and I'll do my best!",
        "I'm happy to help! Just let me know what you need!",
        "Ask away! I’ll do my best to assist you."
    ],
    "default": [
        "I'm not sure I understand. Can you rephrase?", 
        "Sorry, I didn't get that.", 
        "Could you clarify?",
        "I'm not quite sure. Can you give me more details?",
        "Hmm, I don't understand that yet. Could you explain differently?"
    ]
}

def get_intent(text):
    doc = nlp(text.lower())
    for token in doc:
        if token.lemma_ in ["hello", "hi", "hey"]:
            return "greeting"
        elif token.lemma_ in ["bye", "goodbye", "see you"]:
            return "goodbye"
        elif token.lemma_ in ["thank", "thanks"]:
            return "thanks"
        elif token.lemma_ in ["help", "assist", "support"]:
            return "help"
    return "default"

def chatbot():
    print("AI Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("AI Chatbot:", random.choice(responses["goodbye"]))
            break
        intent = get_intent(user_input)
        print("AI Chatbot:", random.choice(responses[intent]))

if __name__ == "__main__":
    chatbot()
