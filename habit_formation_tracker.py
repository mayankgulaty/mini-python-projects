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

def log_habit(habits):
    habit_name = input("Enter the habit name: ")
    status = input("Did you adhere to this habit today? (yes/no): ").lower() == 'yes'
    date = datetime.now().strftime('%Y-%m-%d')

    if habit_name not in habits:
        habits[habit_name] = {"dates": []}

    if status:
        habits[habit_name]["dates"].append(date)
        print(f"Logged success for '{habit_name}' on {date}.")
    else:
        print(f"Logged failure for '{habit_name}' on {date}.")

    save_habits(habits)

def view_streaks(habits):
    for habit, data in habits.items():
        streak = len(data["dates"])
        print(f"{habit}: Current streak is {streak} day(s).")

def main():
    habits = load_habits()

    while True:
        action = input("\nChoose an action - Log Habit (L), View Streaks (V), Exit (E): ").upper()

        if action == 'L':
            log_habit(habits)

        elif action == 'V':
            view_streaks(habits)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
