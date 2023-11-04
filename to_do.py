import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.configure(bg="#EFEFEF")

entry = tk.Entry(root, width=30, font=("Helvetica", 14))
entry.pack(pady=20)

button_frame = tk.Frame(root, bg="#EFEFEF")
button_frame.pack()

# Set the text color to black
add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=("Helvetica", 12), bg="#008CBA", fg="black")
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=("Helvetica", 12), bg="#FF5733", fg="black")
add_button.grid(row=0, column=0, padx=10)
delete_button.grid(row=0, column=1)

listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 12), bg="#F0F0F0")
listbox.pack(pady=20, fill=tk.BOTH, expand=True)

root.mainloop()
