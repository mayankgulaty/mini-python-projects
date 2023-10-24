# todo.py

# Initialize an empty to-do list
todo_list = []

while True:
    print("To-Do List:")
    for i, task in enumerate(todo_list):
        print(f"{i+1}. {task}")

    action = input("Enter 'a' to add a task, 'r' to remove a task, or 'q' to quit: ")

    if action == 'a':
        task = input("Enter the task: ")
        todo_list.append(task)
    elif action == 'r':
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list.pop(index)
        else:
            print("Invalid task number.")
    elif action == 'q':
        break
    else:
        print("Invalid action. Please try again.")
