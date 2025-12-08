print("Welcome to Mini Wallet!!")

name = input("Enter Your Name: ")
balance = 0.0

while True:
    try:
        balance = float(input("Enter your starting balance: "))
        if balance < 0:
            print("Balance cannot be negative. Try again.")
            continue
        break
    except ValueError:
        print("Enter a valid number.")


def deposit(balance):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Deposit must be positive.")
            return balance
        balance += amount
        print(f"{name}, new balance: {balance}")
        return balance
    except ValueError:
        print("Invalid amount.")
        return balance


def withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Are you DUMB??? How are you wihtdrawing in negative??.")
            return balance
        if amount > balance:
            print("Insufficient funds, Please Earn Some Money and comeback later.")
            return balance
        balance -= amount
        print(f"{name}, new balance: {balance}")
        return balance
    except ValueError:
        print("Invalid amount.")
        return balance


def check_balance(balance):
    print(f"{name}, your balance is: {balance}")


while True:
    print("""
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
""")

    choice = input("Enter your choice: ")

    if choice == '1':
        balance = deposit(balance)

    elif choice == '2':
        balance = withdraw(balance)

    elif choice == '3':
        check_balance(balance)

    elif choice == '4':
        print("Exiting... Thank you for using Mini Wallet!")
        break

    else:
        print("Invalid choice, try again.")
