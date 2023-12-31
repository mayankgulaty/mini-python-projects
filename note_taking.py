import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

def save_note():
    title = title_entry.get()
    note_text = note_text_widget.get("1.0", "end-1c")

    if title:
        note_data = f"Title: {title}\n\n{note_text}"
        with open(f"notes/{title}.txt", "w") as file:
            file.write(note_data)
        messagebox.showinfo("Note Saved", "Note has been saved.")
    else:
        messagebox.showwarning("Empty Title", "Please enter a title for your note.")

def load_note():
    title = title_entry.get()

    if title:
        note_filename = f"notes/{title}.txt"
        if os.path.exists(note_filename):
            with open(note_filename, "r") as file:
                note_data = file.read()
                note_text_widget.delete("1.0", "end")
                note_text_widget.insert("1.0", note_data)
        else:
            messagebox.showerror("Note Not Found", "Note with the specified title not found.")
    else:
        messagebox.showwarning("Empty Title", "Please enter a title to load a note.")

def clear_note():
    title_entry.delete(0, tk.END)
    note_text_widget.delete("1.0", "end")

def list_notes():
    note_files = os.listdir("notes")
    note_titles = [file[:-4] for file in note_files if file.endswith(".txt")]
    notes_list_var.set(note_titles)

def search_note():
    search_text = search_entry.get()
    if search_text:
        matching_notes = [title for title in notes_list_var.get() if search_text.lower() in title.lower()]
        notes_list_var.set(matching_notes)
    else:
        list_notes()

def delete_note():
    selected_index = notes_listbox.curselection()
    if selected_index:
        selected_title = notes_list_var.get()[selected_index[0]]
        note_filename = f"notes/{selected_title}.txt"
        os.remove(note_filename)
        list_notes()

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
clear_button.grid(row=3, column=0, pady=10)

list_button = ttk.Button(frame, text="List Notes", command=list_notes)
list_button.grid(row=3, column=1, pady=10)

search_label = ttk.Label(frame, text="Search:")
search_label.grid(row=4, column=0, sticky="w")

search_entry = ttk.Entry(frame)
search_entry.grid(row=4, column=1, padx=5)

search_button = ttk.Button(frame, text="Search", command=search_note)
search_button.grid(row=4, column=2, padx=5)

delete_button = ttk.Button(frame, text="Delete Note", command=delete_note)
delete_button.grid(row=5, column=0, columnspan=2, pady=10)

notes_list_var = tk.StringVar()
notes_listbox = tk.Listbox(frame, listvariable=notes_list_var, height=10)
notes_listbox.grid(row=6, column=0, columnspan=3, padx=5, pady=10)

if not os.path.exists("notes"):
    os.mkdir("notes")

root.mainloop()
