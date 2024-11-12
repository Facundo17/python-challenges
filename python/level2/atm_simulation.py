
print("Welcome to the ATM!")

options = {
    "1": "Check Balance",
    "2": "Deposit Money",
    "3": "Withdraw Money",
    "4": "Exit"
}

balance = 100

def enter_money(balance):
    deposit = input("Enter amount to deposit: ")
    value = balance + int(deposit)
    return value

def withdraw_money(balance):
    deposit = input("Enter amount to withdraw: ")
    value = balance - int(deposit)
    return value

def check_money(balance):
    print(f"Your current balance is: ${balance}")

print(f"Current Balance: ${balance}")

while True:
    print("")
    
    for i in options:
        print(f"{i}. {options[i]}")
    
    try:
        inputUser = input("Choose an option: ")
        
        if int(inputUser) <= 0 or int(inputUser) > len(options):
            raise # lanzar una excepción
         
        # python no tiene un switch case, pero tiene un match
        match int(inputUser):
            case 1:
                check_money(balance)
            case 2:
                balance = enter_money(balance)
                print(f"Deposit successful! Your new balance is: ${balance}")
            case 3:
                balance = withdraw_money(balance)
                print(f"Withdrawal successful! Your new balance is: ${balance}")
            case 4:
                print("Exit.")
                break
    except:
        print(f"Please, insert only numbers from 1 to {len(options)}")
            
    