import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

# Function to mark a task as completed
def mark_completed():
    try:
        selected_task_index = listbox.curselection()[0]
        selected_task = listbox.get(selected_task_index)
        if selected_task[:4] != "[✓] ":
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, "[✓] " + selected_task)
    except IndexError:
        pass

# Function to save tasks to a file
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        for task in tasks:
            listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def quit_app():
    save_tasks()
    root.destroy()


root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.configure(bg="#EFEFEF")

entry = tk.Entry(root, width=30, font=("Helvetica", 14))
entry.pack(pady=20)

button_frame = tk.Frame(root, bg="#EFEFEF")
button_frame.pack()

add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=("Helvetica", 12), bg="#008CBA", fg="black")
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=("Helvetica", 12), bg="#FF5733", fg="black")
complete_button = tk.Button(button_frame, text="Mark Completed", command=mark_completed, font=("Helvetica", 12), bg="#55AA55", fg="black")
add_button.grid(row=0, column=0, padx=10)
delete_button.grid(row=0, column=1)
complete_button.grid(row=0, column=2)

# Create a Quit button
quit_button = tk.Button(button_frame, text="Quit", command=quit_app, font=("Helvetica", 12), bg="#AA5555", fg="black")
quit_button.grid(row=0, column=3)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 12), bg="#F0F0F0")
listbox.pack(pady=20, fill=tk.BOTH, expand=True)

load_tasks()  # Load tasks from a file when the application starts

root.protocol("WM_DELETE_WINDOW", save_tasks)  # Save tasks to a file when the window is closed

root.mainloop()