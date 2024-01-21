import json
import os
from datetime import datetime

def load_events(filename='events.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_events(events, filename='events.json'):
    with open(filename, 'w') as file:
        json.dump(events, file, indent=4)

def add_event(events):
    title = input("Enter the event title: ")
    date = input("Enter the event date (YYYY-MM-DD): ")
    time = input("Enter the event time (HH:MM): ")
    location = input("Enter the event location: ")
    attendees = input("Enter the names of attendees (comma-separated): ").split(',')

    events[title] = {'date': date, 'time': time, 'location': location, 'attendees': attendees}
    save_events(events)
    print(f"Event '{title}' added.")

def view_events(events):
    for title, details in events.items():
        print(f"\nTitle: {title}\nDate: {details['date']}\nTime: {details['time']}\nLocation: {details['location']}\nAttendees: {', '.join(details['attendees'])}")

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
