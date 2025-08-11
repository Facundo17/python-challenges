"""
In this project, your task is to create a program that checks whether a number entered by the user is negative or positive:

(1) Doing the checks inside a function definition and then calling that function.

(2) Including the number in the messages (e.g., “The number -5 is negative”).
"""

def check_number(num):
    if num < 0:
        print(f"The number {num} is negative.")
    elif num > 0:
        print(f"The number {num} is positive.")
    else:
        print("The number is zero, which is neither negative nor positive.")

try:
    user_input = int(input("Enter a number: "))
    check_number(user_input)
except ValueError:
    print("Please enter a valid number.")