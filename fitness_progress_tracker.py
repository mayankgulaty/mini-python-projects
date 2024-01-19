import json
import os
from datetime import datetime

def load_data(filename='fitness_data.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_data(data, filename='fitness_data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def log_entry(data):
    date = datetime.now().strftime('%Y-%m-%d')
    category = input("Enter the fitness category (e.g., Workout, Weight): ")
    details = input("Enter the details for this entry: ")

    if date not in data:
        data[date] = {}
    if category not in data[date]:
        data[date][category] = []

    data[date][category].append(details)
    save_data(data)
    print("Entry saved successfully.")

def view_progress(data):
    for date, categories in data.items():
        print(f"\nDate: {date}")
        for category, details in categories.items():
            print(f"  {category}:")
            for detail in details:
                print(f"    - {detail}")

def main():
    data = load_data()

    while True:
        action = input("\nChoose an action - Log Entry (L), View Progress (V), Exit (E): ").upper()

        if action == 'L':
            log_entry(data)

        elif action == 'V':
            view_progress(data)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
