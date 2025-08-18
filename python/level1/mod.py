"""
Create a program that prompts the user to enter their mood (Happy, Stressed, or Tired)
and display a message depending on the moood submitted by the user.

(1) The program prompts the user to enter their name (e.g., Ardit)

(2) The program greets the user with “Hi. [name]! How are you feeling today? and displays the mood options.

(3) The user chooses a number (1, 2, or 3).

(4) If the user is happpy, the program displays “That’s great, [name]! Keep streading your joy“

(5) If the user is stressed, the program displays “Take a deep breath, [name]. You're doing amazing!“

(6) If the user is tired, the program displays “Rest up, [name]. Tomorrow is a fresh start!“
"""

while True:
    name = input("Hi! What is your name? ")
    print(f"Hi, {name}! How are you feeling today?")
    print("1. Happy")
    print("2. Stressed")
    print("3. Tired")

    mood = input("Please enter the number corresponding to your mood (1, 2, or 3): ")

    if mood == '1':
        print(f"That's great, {name}! Keep spreading your joy!")
    elif mood == '2':
        print(f"Take a deep breath, {name}. You're doing amazing!")
    elif mood == '3':
        print(f"Rest up, {name}. Tomorrow is a fresh start!")
    else:
        print("Invalid choice. Please try again.")
    
    if input("Do you want to continue? (yes/no): ").lower() != 'yes':
        break