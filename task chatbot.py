import random
import re

responses = {
    "hello": [
        "Hello! How can I help you today?",
        "Hi there! Nice to meet you.",
        "Hey! What can I do for you?"
    ],
    "hi": [
        "Hi! How are you?",
        "Hello! How can I assist you?"
    ],
    "how are you": [
        "I'm doing great! Thanks for asking.",
        "I'm fine and ready to chat!"
    ],
    "name": [
        "I'm a Python chatbot.",
        "You can call me PyBot!"
    ],
    "joke": [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the computer go to the doctor? Because it had a virus!"
    ],
    "bye": [
        "Goodbye! Have a great day!",
        "Bye! It was nice chatting with you.",
        "See you later!"
    ],
    "thanks": [
        "You're welcome!",
        "No problem!",
        "Happy to help!"
    ]
}


def get_response(user_input):
    user_input = user_input.lower().strip()

    # Check exact phrases first
    for key, reply_list in responses.items():
        if key in user_input:
            return random.choice(reply_list)

    # Basic pattern matching
    if re.search(r"\b(what|who)\b.*\b(you|your)\b", user_input):
        return "I'm PyBot, a simple Python chatbot."

    if re.search(r"\b(help|assist)\b", user_input):
        return "Sure! You can ask me about my name, tell me a joke, or simply chat with me."

    return "I'm sorry, I don't understand that yet. Try asking me something else."


def chatbot():
    print("=" * 50)
    print("🤖 Welcome to PyBot!")
    print("💬 Start chatting with the chatbot.")
    print("🚪 Type 'bye' to exit.")
    print("=" * 50)

    while True:
        user_input = input("\n👤 You: ")

        if not user_input.strip():
            print("🤖 Bot: Please type something.")
            continue

        response = get_response(user_input)

        print(f"🤖 Bot: {response}")

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    chatbot()
