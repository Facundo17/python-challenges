"""
Create a script that checks the validity of a username based on specific criteria:
1. The username must be between 5 and 15 characters long.
2. It must contain only alphanumeric characters.
3. The first character must be a letter.
"""

valid = "Valid username"

def check_username_validity(username):
    
    if len(username) < 5 or len(username) > 15: return "The username is invalid, length must be between 5 and 15"
    
    if username.isalnum() == False: return "The username is invalid, only alphanumeric characters allowed"
    
    if str(username[0]).isalpha() == False: return "The username is invalid. First character must be a letter"
    
    return valid

while True:
    
    username = check_username_validity(input("Enter username: "))
    
    print(username)
    
    if username == valid:
        break
    