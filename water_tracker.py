import json
import os
from datetime import date

def load_data(filename='water_data.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {"goal": 2000, "logs": {}}

def save_data(data, filename='water_data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def log_intake(data, amount):
    today = str(date.today())
    if today not in data["logs"]:
        data["logs"][today] = 0
    data["logs"][today] += amount
    print(f"Logged {amount}ml of water.")
    save_data(data)

def set_goal(data, goal):
    data["goal"] = goal
    print(f"Daily water goal set to {goal}ml.")
    save_data(data)

def view_progress(data):
    today = str(date.today())
    today_intake = data["logs"].get(today, 0)
    print(f"Today's water intake: {today_intake}ml")
    print(f"Daily goal: {data['goal']}ml")
    print(f"Progress: {today_intake/data['goal']*100:.2f}%")

def main():
    data = load_data()

    while True:
        action = input("Choose an action - Log (L), Set Goal (G), View (V), Exit (E): ").upper()

        if action == 'L':
            amount = int(input("Enter the amount of water in ml: "))
            log_intake(data, amount)

        elif action == 'G':
            goal = int(input("Enter your daily water goal in ml: "))
            set_goal(data, goal)

        elif action == 'V':
            view_progress(data)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
