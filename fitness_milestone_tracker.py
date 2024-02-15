import json
import os
from datetime import datetime

def load_milestones(filename='milestones.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_milestones(milestones, filename='milestones.json'):
    with open(filename, 'w') as file:
        json.dump(milestones, file, indent=4)

def add_milestone(milestones):
    milestone = input("Enter the milestone achieved: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    notes = input("Any notes (optional): ")

    milestones.append({
        'milestone': milestone,
        'date': date,
        'notes': notes
    })
    save_milestones(milestones)
    print("Milestone added.")

def view_milestones(milestones):
    for ms in milestones:
        print(f"\nDate: {ms['date']}, Milestone: {ms['milestone']}, Notes: {ms['notes']}")

def main():
    milestones = load_milestones()

    while True:
        action = input("\nChoose an action - Add Milestone (A), View Milestones (V), Exit (E): ").upper()

        if action == 'A':
            add_milestone(milestones)

        elif action == 'V':
            view_milestones(milestones)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
