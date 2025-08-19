"""
Create file that generates random names from a predefined list in a text file.
This module allows users to read names from a file, add new names, and select a random name.
Exit the program when the user chooses the exit option.
"""

import random
# TODO: mejorar la entrada de usuario, no se está validando o manejando excepciones

# usando el name.txt
file = './names.txt'

def read_file() -> list:
    names = []
    with open(file, "r") as lines:
        linesText = lines.readlines()
        names = list(linesText)
    return names

def write_file(name):
    with open(file, "at") as lines:
        lines.write(f"\n{name}")
    
def select_random() -> str:
    names = read_file()
    return random.choice(names) # la función random devuelve una función aleatoria en una secuencia (list, tuple o string)

def welcome_message() -> str:
    print("""Please select an option:
1. Show the total of names
2. Add a new name
3. Select random name
4. Exit""")

def choice(num):
    match(num):
        case 1:
            print("\nTotal number of names: ", len(read_file()), "\n")
        case 2:
            newName = input("Enter the new name to add: ")
            
            write_file(newName)
            
            print(f"{newName} has been added to the file.")
        case 3:
            print(f"\nRandom name selected: {select_random()}")
        case 4:
            print("Exit")

while True:
    
    welcome_message()
    userInput = input("Enter your choice (1-4): ")
    
    choice(int(userInput))
    
    if int(userInput) == 4:
        break