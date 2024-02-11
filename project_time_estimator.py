import json
import os

def load_tasks(filename='tasks.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task_name = input("Enter the task name: ")
    estimated_hours = float(input("Enter estimated hours to complete the task: "))
    tasks.append({'task_name': task_name, 'estimated_hours': estimated_hours})
    save_tasks(tasks)
    print(f"Task '{task_name}' added with an estimate of {estimated_hours} hours.")

def calculate_total_time(tasks):
    total_hours = sum(task['estimated_hours'] for task in tasks)
    print(f"Total estimated time for project: {total_hours} hours")

def main():
    tasks = load_tasks()

    while True:
        action = input("\nChoose an action - Add Task (A), Calculate Time (C), Exit (E): ").upper()

        if action == 'A':
            add_task(tasks)

        elif action == 'C':
            calculate_total_time(tasks)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
