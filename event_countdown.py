import json
import os
from datetime import datetime


def load_events(filename='events.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []


def save_events(events, filename='events.json'):
    with open(filename, 'w') as file:
        json.dump(events, file, indent=4)


def add_event(events):
    name = input("Enter the event name: ")
    date_str = input("Enter the event date (YYYY-MM-DD): ")
    event_date = datetime.strptime(date_str, '%Y-%m-%d').date()

    events.append({'name': name, 'date': date_str})
    save_events(events)
    print(f"Event '{name}' added for {date_str}.")


def calculate_countdown(event):
    today = datetime.now().date()
    event_date = datetime.strptime(event['date'], '%Y-%m-%d').date()
    days_left = (event_date - today).days
    return days_left


def view_events(events):
    for event in events:
        days_left = calculate_countdown(event)
        print(f"{event['name']} is in {days_left} day(s).")


def main():
    events = load_events()

    while True:
        action = input("\nChoose an action - Add Event (A), View Events (V), Exit (E): ").upper()

        if action == 'A':
            add_event(events)

        elif action == 'V':
            view_events(events)

        elif action == 'E':
            break


if __name__ == "__main__":
    main()
