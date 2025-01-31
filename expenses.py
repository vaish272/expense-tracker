# expenses.py
expenses = []

def add_expense(description, amount, category):
    expense = {"description": description, "amount": amount,"category": category}
    expenses.append(expense)

def list_expenses():
    for expense in expenses:
        print(f"{expense['description']}: ${expense['amount']}")

def main():
    while True:
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = input("Enter amount: ")
            if not amount.isdigit():
               print("Invalid amount. Please enter a number.")
               continue
            add_expense(description, amount)
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
