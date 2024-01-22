import json
import os

def load_transactions(filename='transactions.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_transactions(transactions, filename='transactions.json'):
    with open(filename, 'w') as file:
        json.dump(transactions, file, indent=4)

def log_transaction(transactions, type, amount, category):
    transactions.append({'type': type, 'amount': amount, 'category': category})
    save_transactions(transactions)
    print("Transaction logged successfully.")

def view_summary(transactions):
    income = sum(item['amount'] for item in transactions if item['type'] == 'income')
    expenses = sum(item['amount'] for item in transactions if item['type'] == 'expense')
    balance = income - expenses

    print(f"\nTotal Income: ${income}")
    print(f"Total Expenses: ${expenses}")
    print(f"Net Balance: ${balance}")

def main():
    transactions = load_transactions()

    while True:
        action = input("\nChoose an action - Log (L), Summary (S), Exit (E): ").upper()

        if action == 'L':
            type = input("Enter transaction type (income/expense): ").lower()
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            log_transaction(transactions, type, amount, category)

        elif action == 'S':
            view_summary(transactions)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
