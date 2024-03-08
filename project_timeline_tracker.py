import json
import os
from datetime import datetime

def load_project(filename='project_timeline.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {"tasks": []}

def save_project(project, filename='project_timeline.json'):
    with open(filename, 'w') as file:
        json.dump(project, file, indent=4)

def add_task(project):
    task_description = input("Enter task description: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    project["tasks"].append({"description": task_description, "start_date": start_date, "end_date": end_date, "completed": False})
    save_project(project)
    print("Task added to project.")

def mark_task_completed(project):
    for index, task in enumerate(project["tasks"], start=1):
        print(f"{index}. {task['description']} - Completed: {task['completed']}")
    task_number = int(input("Enter the number of the task to mark as completed: ")) - 1
    project["tasks"][task_number]["completed"] = True
    save_project(project)
    print("Task marked as completed.")

def view_project_timeline(project):
    print("\nProject Timeline:")
    for task in project["tasks"]:
        status = "Completed" if task["completed"] else "Pending"
        print(f"{task['description']} - {status} (Start: {task['start_date']}, End: {task['end_date']})")

def main():
    project = load_project()

    while True:
        action = input("\nChoose an action - Add Task (A), Mark Task Completed (M), View Timeline (V), Exit (E): ").upper()

        if action == 'A':
            add_task(project)

        elif action == 'M':
            mark_task_completed(project)

        elif action == 'V':
            view_project_timeline(project)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
