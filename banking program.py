def show_balance(balance):
    print(f"Your balance is: ₹{balance:.2f}")

def deposit(balance):
    amount = float(input("Enter the amount to be deposited: "))
    if amount < 0:
        print("The amount entered is not valid...")
        return 0
    else:
        print(f"An amount of ₹{amount:.2f} has been successfully deposited in your bank account")
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to be withdraw: "))
    if amount > balance:
        print("Insufficient funds...")
        return 0
    elif amount < 0:
        print("Amount cannot be negative")
        return 0
    else:
        print(f"An amount of ₹{amount:.2f} has been successfully withdrawed from your bank account")
        return amount

def main():
    balance = 0
    is_running = True
    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice(1-4): ")
        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit(balance)
            case "3":
                balance -= withdraw(balance)  
            case "4":
                is_running = False
            case _:
                print("Please enter a valid input...")
    print("Have a nice day !!!")

if __name__ == "__main__":
    main()