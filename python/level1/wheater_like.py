"""
Create a program that asks the user about the current weather and, using a dictionary for decision-making, suggests an activity.
Start the script with this dictionary on top of your script:

weather_activities = {
    "1": "It's a beautiful day! How about a walk in the park? 🌳",
    "2": "Perfect weather for a cozy indoor day with a good book! 📚",
    "3": "Maybe it's a great time for a reflective cup of tea! ☕",
    "4": "Build a snowman or have a snowball fight! ⛄"
}

(1) The program prompts the user to choose 1, 2, 3, or 4 depending on the current weather.

(2) Then, the program displays some text that belongs to the choice in the dictionary given further above.
"""

weather_activities = {
    "1": "It's a beautiful day! How about a walk in the park? 🌳",
    "2": "Perfect weather for a cozy indoor day with a good book! 📚",
    "3": "Maybe it's a great time for a reflective cup of tea! ☕",
    "4": "Build a snowman or have a snowball fight! ⛄"
}

while True:
    print("Choose the current weather condition:")
    print("1. Sunny")
    print("2. Rainy")
    print("3. Cloudy")
    print("4. Snowy")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice in weather_activities:
        print(weather_activities[choice])
        break
    else:
        print("Invalid choice, please select a number between 1 and 4.")