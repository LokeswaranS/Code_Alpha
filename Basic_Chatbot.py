import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you today?"]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm great, how about you?"]
    ],
    [
        r"(.*) your name?",
        ["My name is ChatBot.", "You can call me ChatBot."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "It was nice chatting with you. Goodbye!"]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a chatbot and I exist in the virtual world.", "I don't have a physical location."]
    ],
    [
        r"help",
        ["I can assist you with basic conversation. Feel free to ask me anything!"]
    ],
    [
        r"quit",
        ["Goodbye!", "It was nice talking to you. See you later!"]
    ]
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

def chat_with_bot():
    print("Welcome! Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            break
        
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    # Initialize NLTK tokenizer
    nltk.download('punkt')
    chat_with_bot()
