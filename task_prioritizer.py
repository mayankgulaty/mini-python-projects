import json
import os

def load_tasks(filename='tasks.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(sorted(tasks, key=lambda x: x['priority'], reverse=True), file, indent=4)

def add_task(tasks):
    task_name = input("Enter the task description: ")
    priority = input("Enter the priority (High, Medium, Low): ")
    tasks.append({'task': task_name, 'priority': priority})
    save_tasks(tasks)
    print("Task added.")

def list_tasks(tasks):
    for task in tasks:
        print(f"Task: {task['task']}, Priority: {task['priority']}")

def update_task_priority(tasks):
    task_name = input("Enter the task you want to update: ")
    new_priority = input("Enter the new priority (High, Medium, Low): ")
    found = False
    for task in tasks:
        if task['task'] == task_name:
            task['priority'] = new_priority
            found = True
            break
    if found:
        save_tasks(tasks)
        print("Task priority updated.")
    else:
        print("Task not found.")

def main():
    tasks = load_tasks()

    while True:
        action = input("\nChoose an action - Add Task (A), List Tasks (L), Update Priority (U), Exit (E): ").upper()

        if action == 'A':
            add_task(tasks)

        elif action == 'L':
            list_tasks(tasks)

        elif action == 'U':
            update_task_priority(tasks)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
