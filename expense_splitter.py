def calculate_balances(expenses):
    total_expense = sum(expense['amount'] for expense in expenses)
    per_person = total_expense / len(expenses)

    balances = {}
    for expense in expenses:
        payer = expense['payer']
        balances[payer] = balances.get(payer, 0) + expense['amount'] - per_person

    return balances

def display_balances(balances):
    for person, balance in balances.items():
        if balance > 0:
            print(f"{person} is owed ${balance:.2f}")
        elif balance < 0:
            print(f"{person} owes ${-balance:.2f}")
        else:
            print(f"{person} is settled up")

def main():
    expenses = []
    while True:
        action = input("Add an expense (A), Calculate balances (C), or Exit (E): ").upper()
        if action == 'A':
            payer = input("Who paid? ")
            amount = float(input("How much? $"))
            expenses.append({'payer': payer, 'amount': amount})
        elif action == 'C':
            balances = calculate_balances(expenses)
            display_balances(balances)
        elif action == 'E':
            break

if __name__ == "__main__":
    main()
