
import datetime

print("Hello! I'm here to chat. Type 'bye' to exit")

# Define some responses for keywords
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What’s on your mind?",
    "weather": "I'm not sure about the weather, but it’s always a good day to code!",
    "time": f"The current time is {datetime.datetime.now().strftime('%H:%M')}.",
    "day": f"Today is {datetime.datetime.now().strftime('%A')}.",
    "python": "Python is a versatile programming language, great for web development, data science, and more.",
    "bye": "Bye! Have a great day!",
}

def returnResponse(text):
    for t in text:
        if t in responses:
            return responses[t]

while True:
    userInput = input("You: ")
    
    chatWords = userInput.split(" ")
    
    resp = returnResponse(chatWords)
    
    print(resp or "I don't understand, please try again.")
    
    if "bye" in chatWords:
        break