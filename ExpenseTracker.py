# Personal Expense Tracker
# Skills: lists, dictionaries, loops, conditionals, file/database

print("Welcome to Expense Tracker!")
name = input("Enter your name: ")

expenses = []  # list to store expense records

while True:
    print("\nPress + to add a new expense")
    print("Press # to view expense history")
    print("Press * to exit")

    choice = input("\nEnter your choice: ")

    if choice == '+':
        category = input("Enter category (e.g., Food, Travel, Shopping): ")
        amount = float(input("Enter amount: ₹"))
        description = input("Enter description (optional): ")

        # store expense as a dictionary
        expense = {
            "category": category,
            "amount": amount,
            "description": description
        }

        expenses.append(expense)
        print(f"Added expense: ₹{amount} under '{category}'")

    elif choice == '#':
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print(f"\n{name}'s Expense History:")
            total = 0
            category_summary = {}

            for exp in expenses:
                print(f" - {exp['category']}: ₹{exp['amount']} ({exp['description']})")
                total += exp['amount']

                # track totals by category
                if exp['category'] in category_summary:
                    category_summary[exp['category']] += exp['amount']
                else:
                    category_summary[exp['category']] = exp['amount']

            print(f"\nTotal Expenses: ₹{total}")
            print("\nCategory Summary:")
            for cat, amt in category_summary.items():
                print(f"  {cat}: ₹{amt}")

    elif choice == '*':
        print(f"\nGoodbye, {name}! Your expense session has ended.")
        break

    else:
        print("Invalid choice. Please try again.")
