import json
from datetime import datetime

# Function to add an expense
def add_expense(expenses, date, amount, description, category):
    expense = {
        "date": date,
        "amount": amount,
        "description": description,
        "category": category
    }
    expenses.append(expense)

# Function to get user input
def get_user_input():
    while True:
        try:
            date = input("Enter the date (YYYY-MM-DD): ")
            datetime.strptime(date, "%Y-%m-%d")  # Validate date format
            amount = float(input("Enter the amount: "))
            if amount < 0:
                raise ValueError("Amount must be positive")
            description = input("Enter a description: ")

            categories = ['Food', 'Transportation', 'Entertainment', 'Other']
            print("Select a category:")
            for i, category in enumerate(categories, 1):
                print(f"{i}. {category}")
            
            category_choice = int(input("Enter the number of the category: "))
            category = categories[category_choice - 1]

            return date, amount, description, category
        except ValueError as e:
            print(f"Invalid input: {e}")
        except IndexError:
            print("Invalid category choice. Please select a valid number.")

# Function to display the menu
def display_menu():
    print("1. Add an expense")
    print("2. View monthly summary")
    print("3. View category summary")
    print("4. Exit")

# Function to get monthly summary
def get_monthly_summary(expenses, year, month):
    total = 0
    for expense in expenses:
        expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")
        if expense_date.year == year and expense_date.month == month:
            total += expense["amount"]
    return total

# Function to get category summary
def get_category_summary(expenses):
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        if category not in category_totals:
            category_totals[category] = 0
        category_totals[category] += expense["amount"]
    return category_totals

# Main function
def main():
    expenses = []

    # Load existing expenses from file
    try:
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        pass

    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            date, amount, description, category = get_user_input()
            add_expense(expenses, date, amount, description, category)
            with open('expenses.json', 'w') as file:
                json.dump(expenses, file, indent=4)

        elif choice == 2:
            year = int(input("Enter the year for the summary: "))
            month = int(input("Enter the month for the summary: "))
            print(f"Total expenses for {year}-{month}: {get_monthly_summary(expenses, year, month)}")

        elif choice == 3:
            print("Category-wise summary:", get_category_summary(expenses))

        elif choice == 4:
            break

if __name__ == "__main__":
    main()
