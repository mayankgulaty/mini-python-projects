import json
import os
from datetime import datetime

def load_intake_log(filename='water_intake.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {"goal": 0, "logs": {}}

def save_intake_log(data, filename='water_intake.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def set_daily_goal(data):
    goal = float(input("Enter your daily water intake goal (in liters): "))
    data["goal"] = goal
    save_intake_log(data)
    print(f"Daily water intake goal set to {goal} liters.")

def log_water_intake(data):
    date = datetime.now().strftime('%Y-%m-%d')
    amount = float(input("Enter the amount of water consumed (in liters): "))
    if date not in data["logs"]:
        data["logs"][date] = 0.0
    data["logs"][date] += amount
    save_intake_log(data)
    print(f"Logged {amount} liters of water.")

def view_progress(data):
    date = datetime.now().strftime('%Y-%m-%d')
    intake = data["logs"].get(date, 0)
    print(f"\nToday's Water Intake: {intake} liters")
    print(f"Daily Goal: {data['goal']} liters")
    if intake >= data["goal"]:
        print("Congratulations! You've reached your daily goal.")
    else:
        print(f"You're {data['goal'] - intake} liters away from your daily goal.")

def main():
    data = load_intake_log()

    while True:
        action = input("\nChoose an action - Set Goal (S), Log Intake (L), View Progress (V), Exit (E): ").upper()

        if action == 'S':
            set_daily_goal(data)

        elif action == 'L':
            log_water_intake(data)

        elif action == 'V':
            view_progress(data)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
