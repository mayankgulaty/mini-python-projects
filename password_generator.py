import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()

    characters = ""

    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if characters:
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        password_var.set(generated_password)
    else:
        password_var.set("Select at least one character type")

root = tk.Tk()
root.title("Password Generator")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=20, pady=20)

length_label = ttk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, sticky="w")

length_entry = ttk.Entry(frame)
length_entry.grid(row=0, column=1, padx=5)

password_var = tk.StringVar()
password_var.set("")

password_label = ttk.Label(frame, text="Generated Password:")
password_label.grid(row=1, column=0, sticky="w")

password_display = ttk.Label(frame, textvariable=password_var, font=("Helvetica", 12))
password_display.grid(row=1, column=1, padx=5)

generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

lowercase_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

lowercase_checkbox = ttk.Checkbutton(frame, text="Lowercase", variable=lowercase_var)
uppercase_checkbox = ttk.Checkbutton(frame, text="Uppercase", variable=uppercase_var)
digits_checkbox = ttk.Checkbutton(frame, text="Digits", variable=digits_var)
symbols_checkbox = ttk.Checkbutton(frame, text="Symbols", variable=symbols_var)

lowercase_checkbox.grid(row=3, column=0, sticky="w")
uppercase_checkbox.grid(row=4, column=0, sticky="w")
digits_checkbox.grid(row=5, column=0, sticky="w")
symbols_checkbox.grid(row=6, column=0, sticky="w")

root.mainloop()
