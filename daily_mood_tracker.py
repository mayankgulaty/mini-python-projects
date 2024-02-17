import json
import os
from datetime import datetime

def load_mood_entries(filename='mood_entries.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_mood_entries(entries, filename='mood_entries.json'):
    with open(filename, 'w') as file:
        json.dump(entries, file, indent=4)

def log_mood(entries):
    mood = input("How are you feeling? (Happy, Sad, Anxious, Excited, etc.): ")
    notes = input("Notes about your day (optional): ")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    entries.append({'mood': mood, 'notes': notes, 'timestamp': timestamp})
    save_mood_entries(entries)
    print("Mood entry added.")

def view_mood_history(entries):
    for entry in entries:
        print(f"\nDate/Time: {entry['timestamp']}, Mood: {entry['mood']}, Notes: {entry['notes']}")

def main():
    entries = load_mood_entries()

    while True:
        action = input("\nChoose an action - Log Mood (L), View History (V), Exit (E): ").upper()

        if action == 'L':
            log_mood(entries)

        elif action == 'V':
            view_mood_history(entries)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
