import json
import os
from datetime import datetime

def load_maintenance_log(filename='maintenance_log.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_maintenance_log(log, filename='maintenance_log.json'):
    with open(filename, 'w') as file:
        json.dump(log, file, indent=4)

def log_maintenance_activity(log):
    service_type = input("Enter the type of service (e.g., Oil Change, Tire Rotation): ")
    date = input("Enter the date of service (YYYY-MM-DD): ")
    notes = input("Additional notes (optional): ")

    log.append({'service_type': service_type, 'date': date, 'notes': notes})
    save_maintenance_log(log)
    print(f"Logged maintenance activity: {service_type}")

def view_maintenance_history(log):
    for entry in log:
        print(f"\nDate: {entry['date']}, Service: {entry['service_type']}, Notes: {entry['notes']}")

def main():
    log = load_maintenance_log()

    while True:
        action = input("\nChoose an action - Log Activity (L), View History (V), Exit (E): ").upper()

        if action == 'L':
            log_maintenance_activity(log)

        elif action == 'V':
            view_maintenance_history(log)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
