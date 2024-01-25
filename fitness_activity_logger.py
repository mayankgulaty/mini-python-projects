import json
import os
from datetime import datetime

def load_activities(filename='activities.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_activities(activities, filename='activities.json'):
    with open(filename, 'w') as file:
        json.dump(activities, file, indent=4)

def log_activity(activities):
    activity_type = input("Enter the activity type (e.g., Running, Cycling): ")
    duration = input("Enter the duration (e.g., 45 minutes): ")
    distance = input("Enter the distance (optional): ")
    notes = input("Any additional notes (optional): ")

    activity = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'type': activity_type,
        'duration': duration,
        'distance': distance,
        'notes': notes
    }

    activities.append(activity)
    save_activities(activities)
    print("Activity logged successfully.")

def view_activities(activities):
    for activity in activities:
        print(f"\nDate: {activity['date']}, Type: {activity['type']}")
        print(f"  Duration: {activity['duration']}, Distance: {activity['distance']}")
        if activity['notes']:
            print(f"  Notes: {activity['notes']}")

def main():
    activities = load_activities()

    while True:
        action = input("\nChoose an action - Log Activity (L), View Activities (V), Exit (E): ").upper()

        if action == 'L':
            log_activity(activities)

        elif action == 'V':
            view_activities(activities)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
