import json
import os
from datetime import datetime

def load_habits(filename='habits.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_habits(habits, filename='habits.json'):
    with open(filename, 'w') as file:
        json.dump(habits, file, indent=4)

def log_habit(habits, habit_name):
    today = datetime.now().strftime('%Y-%m-%d')
    if habit_name not in habits:
        habits[habit_name] = []
    habits[habit_name].append(today)
    save_habits(habits)
    print(f"Habit '{habit_name}' logged for today.")

def view_habits(habits):
    for habit_name, dates in habits.items():
        streak = len(dates)
        print(f"{habit_name}: {streak} day(s) - Dates: {', '.join(dates)}")

def main():
    habits = load_habits()

    while True:
        action = input("\nChoose an action - Log Habit (L), View Habits (V), Exit (E): ").upper()

        if action == 'L':
            habit_name = input("Enter the name of the habit to log: ")
            log_habit(habits, habit_name)

        elif action == 'V':
            view_habits(habits)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
