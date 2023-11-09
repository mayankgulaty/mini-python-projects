import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def save_note():
    title = title_entry.get()
    note_text = note_text_widget.get("1.0", "end-1c")

    if title:
        note_data = f"Title: {title}\n\n{note_text}"
        with open(f"{title}.txt", "w") as file:
            file.write(note_data)
        messagebox.showinfo("Note Saved", "Note has been saved.")
    else:
        messagebox.showwarning("Empty Title", "Please enter a title for your note.")

def load_note():
    title = title_entry.get()

    if title:
        try:
            with open(f"{title}.txt", "r") as file:
                note_data = file.read()
                note_text_widget.delete("1.0", "end")
                note_text_widget.insert("1.0", note_data)
        except FileNotFoundError:
            messagebox.showerror("Note Not Found", "Note with the specified title not found.")
    else:
        messagebox.showwarning("Empty Title", "Please enter a title to load a note.")

def clear_note():
    title_entry.delete(0, tk.END)
    note_text_widget.delete("1.0", "end")

root = tk.Tk()
root.title("Note-taking Application")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=20, pady=20)

title_label = ttk.Label(frame, text="Title:")
title_label.grid(row=0, column=0, sticky="w")

title_entry = ttk.Entry(frame)
title_entry.grid(row=0, column=1, padx=5)

note_text_widget = tk.Text(frame, height=10, width=40)
note_text_widget.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

save_button = ttk.Button(frame, text="Save Note", command=save_note)
save_button.grid(row=2, column=0, pady=10)

load_button = ttk.Button(frame, text="Load Note", command=load_note)
load_button.grid(row=2, column=1, pady=10)

clear_button = ttk.Button(frame, text="Clear", command=clear_note)
clear_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
