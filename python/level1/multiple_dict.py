"""
This project starts with a pre-defined dictionary representing a grocery list with quantities:

grocery_list = {
    "apples": 5,
    "bananas": 2,
    "milk": 1,
    "bread": 1
}

You task is to add some code that updates all the values of the dictionary by multiplying them by 10. 
Then, print out the updated dictionary.

The program should display the updated dictionary in the command line.
"""

def update_grocery_list(grocery_list):
    """Update the grocery list by multiplying all quantities by 10."""
    for item in grocery_list:
        grocery_list[item] *= 10
    return grocery_list

grocery_list = {
    "apples": 5,
    "bananas": 2,
    "milk": 1,
    "bread": 1
}

update_grocery_list(grocery_list)
print(grocery_list)