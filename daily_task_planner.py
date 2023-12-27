import json

class TaskPlanner:
    def __init__(self):
        self.tasks = []

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task, priority):
        self.tasks.append({'task': task, 'priority': priority, 'completed': False})
        self.save_tasks()

    def display_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            status = 'Done' if task['completed'] else 'Pending'
            print(f"{idx}. {task['task']} [Priority: {task['priority']}] - {status}")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            self.save_tasks()
        else:
            print("Invalid task number.")

def main():
    planner = TaskPlanner()
    planner.load_tasks()

    while True:
        print("\nTask Planner")
        action = input("Choose an action - Add (A), View (V), Mark Complete (M), Exit (E): ").upper()

        if action == 'A':
            task = input("Enter the task: ")
            priority = input("Enter the priority (High/Medium/Low): ")
            planner.add_task(task, priority)

        elif action == 'V':
            planner.display_tasks()

        elif action == 'M':
            task_number = int(input("Enter the task number to mark as completed: "))
            planner.mark_task_completed(task_number)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
