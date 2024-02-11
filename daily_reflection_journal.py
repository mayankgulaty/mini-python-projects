import json
import os
from datetime import datetime

def load_reflections(filename='reflections.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_reflections(reflections, filename='reflections.json'):
    with open(filename, 'w') as file:
        json.dump(reflections, file, indent=4)

def add_reflection(reflections):
    date = datetime.now().strftime('%Y-%m-%d')
    reflection = input("Write your reflection for today:\n")

    reflections[date] = reflection
    save_reflections(reflections)
    print("Reflection saved.")

def view_reflections(reflections):
    for date, reflection in reflections.items():
        print(f"\nDate: {date}\nReflection:\n{reflection}")

def search_reflection(reflections):
    date = input("Enter the date for the reflection you want to find (YYYY-MM-DD): ")
    if date in reflections:
        print(f"\nDate: {date}\nReflection:\n{reflections[date]}")
    else:
        print("No reflection found for this date.")

def main():
    reflections = load_reflections()

    while True:
        action = input("\nChoose an action - Add Reflection (A), View Reflections (V), Search Reflection (S), Exit (E): ").upper()

        if action == 'A':
            add_reflection(reflections)

        elif action == 'V':
            view_reflections(reflections)

        elif action == 'S':
            search_reflection(reflections)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
