# Expense Tracker (Simple Python Project)

expenses = []

while True:
    print("\n==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        expenses.append((name, amount))
        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\nYour Expenses:")
            for i, (name, amount) in enumerate(expenses, start=1):
                print(f"{i}. {name} - {amount}")

    elif choice == "3":
        total = sum(amount for _, amount in expenses)
        print("Total Expense:", total)

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
