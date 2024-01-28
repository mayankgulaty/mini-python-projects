import json
import os
from datetime import datetime

def load_sleep_data(filename='sleep_data.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_sleep_data(data, filename='sleep_data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def log_sleep_entry(data):
    sleep_time = input("Enter the time you went to bed (HH:MM): ")
    wake_time = input("Enter the time you woke up (HH:MM): ")
    date = datetime.now().strftime('%Y-%m-%d')

    sleep_entry = {
        'date': date,
        'sleep_time': sleep_time,
        'wake_time': wake_time,
    }
    data.append(sleep_entry)
    save_sleep_data(data)
    print("Sleep entry recorded.")

def calculate_sleep_duration(sleep_time, wake_time):
    fmt = '%H:%M'
    tdelta = datetime.strptime(wake_time, fmt) - datetime.strptime(sleep_time, fmt)
    return tdelta.seconds / 3600  # Convert seconds to hours

def view_sleep_history(data):
    for entry in data:
        duration = calculate_sleep_duration(entry['sleep_time'], entry['wake_time'])
        print(f"Date: {entry['date']}, Duration: {duration:.2f} hours")

def main():
    data = load_sleep_data()

    while True:
        action = input("\nChoose an action - Log Sleep (L), View History (V), Exit (E): ").upper()

        if action == 'L':
            log_sleep_entry(data)

        elif action == 'V':
            view_sleep_history(data)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
