import json
import os
from datetime import datetime

def load_goals(filename='savings_goals.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_goals(goals, filename='savings_goals.json'):
    with open(filename, 'w') as file:
        json.dump(goals, file, indent=4)

def set_goal(goals):
    goal_name = input("Enter the goal name: ")
    target_amount = float(input("Enter the target amount ($): "))

    goals.append({'goal_name': goal_name, 'target_amount': target_amount, 'current_amount': 0.0})
    save_goals(goals)
    print(f"Goal '{goal_name}' set with a target of ${target_amount}.")

def log_contribution(goals):
    goal_name = input("Enter the goal name to contribute to: ")
    amount = float(input("Enter the contribution amount ($): "))
    for goal in goals:
        if goal['goal_name'] == goal_name:
            goal['current_amount'] += amount
            save_goals(goals)
            print(f"Contributed ${amount} to '{goal_name}'.")
            return
    print("Goal not found.")

def view_progress(goals):
    for goal in goals:
        percentage = (goal['current_amount'] / goal['target_amount']) * 100
        print(f"\nGoal: {goal['goal_name']}, Progress: ${goal['current_amount']}/${goal['target_amount']} ({percentage:.2f}%)")

def main():
    goals = load_goals()

    while True:
        action = input("\nChoose an action - Set Goal (S), Log Contribution (L), View Progress (V), Exit (E): ").upper()

        if action == 'S':
            set_goal(goals)

        elif action == 'L':
            log_contribution(goals)

        elif action == 'V':
            view_progress(goals)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
