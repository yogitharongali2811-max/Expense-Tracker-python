from datetime import datetime


def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")

        date = datetime.now().strftime("%Y-%m-%d")

        with open("expenses.txt", "a") as file:
            file.write(f"{date},{amount},{category}\n")

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount! Please enter a number.")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            total = 0
            print("\nDate       | Amount | Category")
            print("-----------------------------------")

            for line in file:
                date, amount, category = line.strip().split(",")
                print(f"{date} | {amount} | {category}")
                total += float(amount)

            print("-----------------------------------")
            print("Total Expense:", total)

    except FileNotFoundError:
        print("No expenses recorded yet.")


# Main Program
while True:
    print("\n===== EXPENSE TRACKER MENU =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
