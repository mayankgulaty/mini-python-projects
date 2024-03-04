import json
import os
from datetime import datetime, timedelta

def load_schedule(filename='daily_schedule.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_schedule(schedule, filename='daily_schedule.json'):
    with open(filename, 'w') as file:
        json.dump(schedule, file, indent=4)

def add_task(schedule):
    task_name = input("Enter the task name: ")
    time_slot = input("Enter the time slot for the task (HH:MM-HH:MM): ")
    description = input("Enter a brief description of the task: ")

    date = datetime.now().strftime('%Y-%m-%d')
    if date not in schedule:
        schedule[date] = {}
    schedule[date][time_slot] = {"task": task_name, "description": description, "completed": False}
    save_schedule(schedule)
    print(f"Task '{task_name}' added to the schedule.")

def mark_task_completed(schedule):
    date = datetime.now().strftime('%Y-%m-%d')
    if date in schedule:
        for time_slot, task_info in schedule[date].items():
            print(f"{time_slot}: {task_info['task']} - Completed: {task_info['completed']}")
        time_slot = input("Enter the time slot of the task to mark as completed: ")
        if time_slot in schedule[date]:
            schedule[date][time_slot]["completed"] = True
            save_schedule(schedule)
            print("Task marked as completed.")
        else:
            print("Time slot not found.")
    else:
        print("No tasks scheduled for today.")

def view_schedule(schedule):
    date = datetime.now().strftime('%Y-%m-%d')
    if date in schedule:
        print(f"\nSchedule for {date}:")
        for time_slot, task_info in schedule[date].items():
            completion_status = "Completed" if task_info["completed"] else "Pending"
            print(f"{time_slot}: {task_info['task']} - {completion_status} - {task_info['description']}")
    else:
        print("No tasks scheduled for today.")

def main():
    schedule = load_schedule()

    while True:
        action = input("\nChoose an action - Add Task (A), Mark Task Completed (M), View Schedule (V), Exit (E): ").upper()

        if action == 'A':
            add_task(schedule)

        elif action == 'M':
            mark_task_completed(schedule)

        elif action == 'V':
            view_schedule(schedule)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
