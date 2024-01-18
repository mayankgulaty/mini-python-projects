import json
import os
from datetime import datetime

def load_entries(filename='journal.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_entries(entries, filename='journal.json'):
    with open(filename, 'w') as file:
        json.dump(entries, file, indent=4)

def add_entry(entries):
    date = datetime.now().strftime('%Y-%m-%d')
    entry = input("Write your journal entry:\n")
    entries[date] = entry
    save_entries(entries)
    print("Journal entry saved.")

def view_entries(entries):
    for date, entry in entries.items():
        print(f"\nDate: {date}\nEntry: {entry}")

def main():
    entries = load_entries()

    while True:
        action = input("\nChoose an action - Write (W), Read (R), Exit (E): ").upper()

        if action == 'W':
            add_entry(entries)

        elif action == 'R':
            view_entries(entries)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
