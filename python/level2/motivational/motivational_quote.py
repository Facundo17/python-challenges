"""
Create a program that reads a list of motivational quotes from a text file and selects one to display every Monday (or any day the user runs the program). 
It uses Python's date handling to check the current day and ensures you’re greeted with a new quote each time you run it.

The program checks what day it is. 
If it is Monday it displays the day and picks a random quote from the "quotes.txt" file.
If it is not Monday, it simply informs the user the day.

Required Libraries: random, datetime 
"""

import random
from datetime import datetime

def get_day_of_week():
    """Returns the current day of the week."""
    return datetime.now().strftime('%A')

def get_random_quote(file_path):
    """Reads quotes from a file and returns a random quote."""
    try:
        with open(file_path, 'r') as file:
            quotes = file.readlines()
            return random.choice(quotes).strip()
    except FileNotFoundError:
        return "Quotes file not found."

def main():
    """Main function to check the day and display a quote if it's Monday."""
    day_of_week = get_day_of_week()

    if day_of_week == 'Monday':
        print(f"It's {day_of_week}! Time for some motivation.")
        quote = get_random_quote('quotes.txt')
        print(f"Motivational Quote for today: {quote}")
    else:
        print(f"Today is {day_of_week}!, no motivational quote for today.")

if __name__ == "__main__":
    main()