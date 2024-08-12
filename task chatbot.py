#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install nltk')


# In[ ]:


##pip install nltk
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you. You can call me ChatBot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good, thank you! How can I help you today?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Glad to hear that!", "Alright, great!",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I am a virtual being, I don't have a physical location.",]
    ],
    [
        r"(.*) created (you|yourself)?",
        ["I was created by a Python enthusiast.", "Someone who loves programming created me."]
    ],
    [
        r"(.*) (raining|rain) ?",
        ["I don't have real-time weather data, but you can check online!"]
    ],
    [
        r"quit",
        ["Bye, take care!", "Goodbye!"]
    ],
]

reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"
}


def chatbot():
    print("Hi, I'm the chatbot you created. How can I help you today? (type 'quit' to exit)")

    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()



# In[ ]:




