import json
import os
from datetime import datetime, timedelta

def load_plant_care(filename='plant_care.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_plant_care(care_data, filename='plant_care.json'):
    with open(filename, 'w') as file:
        json.dump(care_data, file, indent=4)

def log_care_activity(care_data):
    plant_name = input("Enter the plant name: ")
    activity_type = input("Enter the care activity type (e.g., Watering, Fertilizing): ")
    date = input("Enter the date of the activity (YYYY-MM-DD): ")
    notes = input("Additional notes (optional): ")

    if plant_name not in care_data:
        care_data[plant_name] = []

    care_data[plant_name].append({
        'activity_type': activity_type,
        'date': date,
        'notes': notes
    })
    save_plant_care(care_data)
    print(f"Logged {activity_type} for '{plant_name}'.")

def view_upcoming_care(care_data):
    today = datetime.now().date()
    for plant, activities in care_data.items():
        for activity in activities:
            activity_date = datetime.strptime(activity['date'], '%Y-%m-%d').date()
            if activity_date >= today:
                print(f"Plant: {plant}, Activity: {activity['activity_type']}, Date: {activity['date']}, Notes: {activity['notes']}")

def main():
    care_data = load_plant_care()

    while True:
        action = input("\nChoose an action - Log Activity (L), View Upcoming Care (V), Exit (E): ").upper()

        if action == 'L':
            log_care_activity(care_data)

        elif action == 'V':
            view_upcoming_care(care_data)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
