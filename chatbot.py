import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm doing great, thanks for asking!"]
    ],
    [
        r"(.*) your name?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"what can you do for me ?",
        ["I can provide information, answer questions, or just have a chat with you.",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye, have a great day!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that. Can you please repeat or ask something else?",]
    ]
]

# Create a chatbot using the Chat class
def simple_chatbot():
    print("Hi! I'm ChatBot. How can I assist you today?")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

# Invoke the chatbot function
if __name__ == "__main__":
    simple_chatbot()
