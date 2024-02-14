import json
import os
from datetime import datetime

def load_subscriptions(filename='subscriptions.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_subscriptions(subscriptions, filename='subscriptions.json'):
    with open(filename, 'w') as file:
        json.dump(subscriptions, file, indent=4)

def add_subscription(subscriptions):
    name = input("Enter subscription name: ")
    cost = float(input("Enter monthly cost: "))
    renewal_date = input("Enter renewal date (YYYY-MM-DD): ")
    notes = input("Any notes (optional): ")

    subscriptions.append({
        'name': name,
        'cost': cost,
        'renewal_date': renewal_date,
        'notes': notes
    })
    save_subscriptions(subscriptions)
    print(f"Subscription '{name}' added.")

def view_subscriptions(subscriptions):
    subscriptions.sort(key=lambda x: datetime.strptime(x['renewal_date'], '%Y-%m-%d'))
    for sub in subscriptions:
        print(f"\nName: {sub['name']}, Cost: ${sub['cost']}, Renewal Date: {sub['renewal_date']}, Notes: {sub['notes']}")

def calculate_total_cost(subscriptions):
    total_cost = sum(sub['cost'] for sub in subscriptions)
    print(f"Total Monthly Cost: ${total_cost:.2f}")
    print(f"Total Yearly Cost: ${total_cost * 12:.2f}")

def main():
    subscriptions = load_subscriptions()

    while True:
        action = input("\nChoose an action - Add (A), View (V), Total Cost (T), Exit (E): ").upper()

        if action == 'A':
            add_subscription(subscriptions)

        elif action == 'V':
            view_subscriptions(subscriptions)

        elif action == 'T':
            calculate_total_cost(subscriptions)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
