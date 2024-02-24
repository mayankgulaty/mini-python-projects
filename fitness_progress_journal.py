import json
import os
from datetime import datetime

def load_journal(filename='fitness_journal.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_journal(journal, filename='fitness_journal.json'):
    with open(filename, 'w') as file:
        json.dump(journal, file, indent=4)

def log_workout(journal):
    date = datetime.now().strftime('%Y-%m-%d')
    workout_type = input("Enter the workout type (e.g., Cardio, Strength Training): ")
    duration = input("Enter the workout duration: ")
    intensity = input("Enter the workout intensity: ")
    reflection = input("Write your reflections or notes about the workout: ")

    journal.append({
        'date': date,
        'workout_type': workout_type,
        'duration': duration,
        'intensity': intensity,
        'reflection': reflection
    })
    save_journal(journal)
    print("Workout logged successfully.")

def view_journal(journal):
    for entry in journal:
        print(f"\nDate: {entry['date']}, Workout Type: {entry['workout_type']}")
        print(f"Duration: {entry['duration']}, Intensity: {entry['intensity']}")
        print(f"Reflections: {entry['reflection']}")

def main():
    journal = load_journal()

    while True:
        action = input("\nChoose an action - Log Workout (L), View Journal (V), Exit (E): ").upper()

        if action == 'L':
            log_workout(journal)

        elif action == 'V':
            view_journal(journal)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
