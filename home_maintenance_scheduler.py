import json
import os
from datetime import datetime, timedelta

def load_tasks(filename='maintenance_tasks.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks, filename='maintenance_tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task_name = input("Enter the maintenance task: ")
    frequency = input("Enter the frequency (e.g., weekly, monthly, annually): ")
    last_completed = input("Enter the last completed date (YYYY-MM-DD) or leave blank if not yet completed: ")

    tasks.append({'task': task_name, 'frequency': frequency, 'last_completed': last_completed})
    save_tasks(tasks)
    print(f"Task '{task_name}' added.")

def calculate_next_due_date(last_completed, frequency):
    if not last_completed:
        return "Due Now"
    date_format = '%Y-%m-%d'
    last_completed_date = datetime.strptime(last_completed, date_format)
    if frequency == 'weekly':
        return (last_completed_date + timedelta(weeks=1)).strftime(date_format)
    elif frequency == 'monthly':
        return (last_completed_date + timedelta(weeks=4)).strftime(date_format)
    elif frequency == 'annually':
        return (last_completed_date + timedelta(weeks=52)).strftime(date_format)
    return "Unknown Frequency"

def view_tasks(tasks):
    for task in tasks:
        next_due = calculate_next_due_date(task['last_completed'], task['frequency'])
        print(f"Task: {task['task']}, Next Due: {next_due}")

def main():
    tasks = load_tasks()

    while True:
        action = input("\nChoose an action - Add Task (A), View Tasks (V), Exit (E): ").upper()

        if action == 'A':
            add_task(tasks)

        elif action == 'V':
            view_tasks(tasks)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
