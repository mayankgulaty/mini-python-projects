import json
import os
from datetime import datetime

def load_challenges(filename='challenges.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_challenges(challenges, filename='challenges.json'):
    with open(filename, 'w') as file:
        json.dump(challenges, file, indent=4)

def join_challenge(challenges):
    challenge_name = input("Enter the name of the challenge: ")
    goal = input("Enter the goal of the challenge: ")
    start_date = datetime.now().strftime('%Y-%m-%d')

    challenges[challenge_name] = {'goal': goal, 'start_date': start_date, 'progress': []}
    save_challenges(challenges)
    print(f"Joined challenge: {challenge_name}")

def log_activity(challenges):
    challenge_name = input("Enter the challenge name: ")
    if challenge_name not in challenges:
        print("Challenge not found.")
        return
    activity = input("Log today's activity: ")
    challenges[challenge_name]['progress'].append(activity)
    save_challenges(challenges)
    print("Activity logged.")

def view_progress(challenges):
    for challenge, details in challenges.items():
        print(f"\nChallenge: {challenge}\nGoal: {details['goal']}\nStart Date: {details['start_date']}")
        print("Progress:")
        for activity in details['progress']:
            print(f"  - {activity}")

def main():
    challenges = load_challenges()

    while True:
        action = input("\nChoose an action - Join Challenge (J), Log Activity (L), View Progress (V), Exit (E): ").upper()

        if action == 'J':
            join_challenge(challenges)

        elif action == 'L':
            log_activity(challenges)

        elif action == 'V':
            view_progress(challenges)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
