import json
import os

def load_exercise_plan(filename='exercise_plan.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {day: [] for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}

def save_exercise_plan(plan, filename='exercise_plan.json'):
    with open(filename, 'w') as file:
        json.dump(plan, file, indent=4)

def add_exercise(plan):
    day = input("Enter the day of the week: ")
    exercise = input("Enter the exercise: ")
    if day in plan:
        plan[day].append(exercise)
        save_exercise_plan(plan)
        print(f"Exercise added to {day}.")
    else:
        print("Invalid day of the week.")

def view_exercise_plan(plan):
    for day, exercises in plan.items():
        print(f"\n{day}:")
        for exercise in exercises:
            print(f"- {exercise}")

def update_exercise_plan(plan):
    day = input("Enter the day of the week to update: ")
    if day in plan:
        print(f"Current exercises on {day}:")
        for i, exercise in enumerate(plan[day], start=1):
            print(f"{i}. {exercise}")
        exercise_index = int(input("Enter the number of the exercise to remove: ")) - 1
        if 0 <= exercise_index < len(plan[day]):
            del plan[day][exercise_index]
            add_exercise(plan)  # Prompt to add a new exercise
        else:
            print("Invalid exercise number.")
    else:
        print("Invalid day of the week.")

def main():
    exercise_plan = load_exercise_plan()

    while True:
        action = input("\nChoose an action - Add Exercise (A), View Plan (V), Update Plan (U), Exit (E): ").upper()

        if action == 'A':
            add_exercise(exercise_plan)

        elif action == 'V':
            view_exercise_plan(exercise_plan)

        elif action == 'U':
            update_exercise_plan(exercise_plan)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
