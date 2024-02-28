import json
import os
from datetime import datetime

def load_activities(filename='pet_care_activities.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_activities(activities, filename='pet_care_activities.json'):
    with open(filename, 'w') as file:
        json.dump(activities, file, indent=4)

def add_activity(activities):
    activity_type = input("Enter the activity type (e.g., Feeding, Walking, Vet Visit): ")
    date_time = input("Enter the date and time for the activity (YYYY-MM-DD HH:MM): ")

    activities.append({'activity_type': activity_type, 'date_time': date_time})
    save_activities(activities)
    print(f"{activity_type} scheduled for {date_time}.")

def view_activities(activities):
    for activity in activities:
        print(f"\nActivity: {activity['activity_type']}, Scheduled for: {activity['date_time']}")

def main():
    activities = load_activities()

    while True:
        action = input("\nChoose an action - Add Activity (A), View Activities (V), Exit (E): ").upper()

        if action == 'A':
            add_activity(activities)

        elif action == 'V':
            view_activities(activities)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
