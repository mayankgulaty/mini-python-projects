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

def add_habit(habits):
    habit_name = input("Enter the habit you want to track: ")
    description = input("Enter a brief description of the habit: ")

    habits[habit_name] = {"description": description, "log": {}}
    save_habits(habits)
    print(f"Added habit: {habit_name}")

def log_progress(habits):
    habit_name = input("Enter the habit name: ")
    date = datetime.now().strftime('%Y-%m-%d')
    success = input("Did you perform this habit today? (yes/no): ").lower()

    if habit_name in habits:
        habits[habit_name]["log"][date] = success == 'yes'
        save_habits(habits)
        print(f"Logged progress for {habit_name}")
    else:
        print("Habit not found.")

def view_streaks(habits):
    for habit, details in habits.items():
        streak = 0
        for date, success in sorted(details["log"].items(), reverse=True):
            if success:
                streak += 1
            else:
                break
        print(f"{habit}: Current streak is {streak} day(s)")

def main():
    habits = load_habits()

    while True:
        action = input("\nChoose an action - Add Habit (A), Log Progress (L), View Streaks (V), Exit (E): ").upper()

        if action == 'A':
            add_habit(habits)

        elif action == 'L':
            log_progress(habits)

        elif action == 'V':
            view_streaks(habits)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
