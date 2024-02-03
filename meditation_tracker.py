import json
import os
from datetime import datetime

def load_sessions(filename='meditation_sessions.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_sessions(sessions, filename='meditation_sessions.json'):
    with open(filename, 'w') as file:
        json.dump(sessions, file, indent=4)

def log_session(sessions):
    date = datetime.now().strftime('%Y-%m-%d')
    duration = input("Enter the duration of the session (in minutes): ")
    meditation_type = input("Enter the type of meditation: ")
    notes = input("Any notes on the session: ")

    sessions.append({
        'date': date,
        'duration': duration,
        'type': meditation_type,
        'notes': notes
    })
    save_sessions(sessions)
    print("Meditation session logged.")

def view_sessions(sessions):
    if not sessions:
        print("No sessions recorded.")
        return
    for session in sessions:
        print(f"\nDate: {session['date']}, Duration: {session['duration']} minutes, Type: {session['type']}, Notes: {session['notes']}")

def main():
    sessions = load_sessions()

    while True:
        action = input("\nChoose an action - Log Session (L), View History (V), Exit (E): ").upper()

        if action == 'L':
            log_session(sessions)

        elif action == 'V':
            view_sessions(sessions)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
