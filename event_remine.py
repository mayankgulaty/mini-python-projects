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
    event_name = input("Enter the event name: ")
    event_date = input("Enter the event date (YYYY-MM-DD): ")

    events.append({'name': event_name, 'date': event_date})
    save_events(events)
    print(f"Event '{event_name}' added for {event_date}.")

def view_upcoming_events(events):
    today = datetime.now().strftime('%Y-%m-%d')
    upcoming_events = [event for event in events if event['date'] >= today]
    upcoming_events.sort(key=lambda x: x['date'])

    if not upcoming_events:
        print("No upcoming events.")
        return

    print("\nUpcoming Events:")
    for event in upcoming_events:
        print(f"{event['name']} on {event['date']}")

def main():
    events = load_events()

    while True:
        action = input("\nChoose an action - Add Event (A), View Upcoming Events (V), Exit (E): ").upper()

        if action == 'A':
            add_event(events)

        elif action == 'V':
            view_upcoming_events(events)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
