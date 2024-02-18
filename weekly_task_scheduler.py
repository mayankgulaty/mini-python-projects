import json
import os

def load_tasks(filename='weekly_tasks.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_tasks(tasks, filename='weekly_tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    day = input("Enter the day of the week for the task: ")
    task_description = input("Enter the task description: ")

    if day not in tasks:
        tasks[day] = []
    tasks[day].append(task_description)
    save_tasks(tasks)
    print(f"Task added for {day}.")

def view_schedule(tasks):
    for day, tasks_for_day in tasks.items():
        print(f"\n{day}:")
        for task in tasks_for_day:
            print(f"  - {task}")

def update_task(tasks):
    day = input("Enter the day of the week for the task to update: ")
    if day in tasks:
        print(f"Current tasks for {day}:")
        for i, task in enumerate(tasks[day], start=1):
            print(f"{i}. {task}")
        task_number = int(input("Enter the number of the task to update: ")) - 1
        if 0 <= task_number < len(tasks[day]):
            new_description = input("Enter the new task description: ")
            tasks[day][task_number] = new_description
            save_tasks(tasks)
            print("Task updated.")
        else:
            print("Invalid task number.")
    else:
        print("No tasks found for the specified day.")

def remove_task(tasks):
    day = input("Enter the day of the week for the task to remove: ")
    if day in tasks:
        print(f"Current tasks for {day}:")
        for i, task in enumerate(tasks[day], start=1):
            print(f"{i}. {task}")
        task_number = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_number < len(tasks[day]):
            removed_task = tasks[day].pop(task_number)
            save_tasks(tasks)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task number.")
    else:
        print("No tasks found for the specified day.")

def main():
    tasks = load_tasks()

    while True:
        action = input("\nChoose an action - Add Task (A), View Schedule (V), Update Task (U), Remove Task (R), Exit (E): ").upper()

        if action == 'A':
            add_task(tasks)

        elif action == 'V':
            view_schedule(tasks)

        elif action == 'U':
            update_task(tasks)

        elif action == 'R':
            remove_task(tasks)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
