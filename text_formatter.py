import tkinter as tk
from tkinter import ttk

def convert_text():
    text = input_text.get("1.0", "end-1c")
    selected_option = case_option.get()

    if selected_option == "UPPERCASE":
        converted_text = text.upper()
    elif selected_option == "lowercase":
        converted_text = text.lower()
    elif selected_option == "Title Case":
        converted_text = text.title()
    elif selected_option == "Sentence case":
        converted_text = text.capitalize()

    output_text.delete("1.0", "end")
    output_text.insert("1.0", converted_text)

def remove_extra_spaces():
    text = input_text.get("1.0", "end-1c")
    cleaned_text = ' '.join(text.split())
    input_text.delete("1.0", "end")
    input_text.insert("1.0", cleaned_text)

def find_and_replace():
    find_text = find_entry.get()
    replace_text = replace_entry.get()
    text = input_text.get("1.0", "end-1c")
    replaced_text = text.replace(find_text, replace_text)
    input_text.delete("1.0", "end")
    input_text.insert("1.0", replaced_text)

def clear_text():
    input_text.delete("1.0", "end")
    output_text.delete("1.0", "end")
    find_entry.delete(0, tk.END)
    replace_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Text Case Converter")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=20, pady=20)

input_label = ttk.Label(frame, text="Input Text:")
input_label.grid(row=0, column=0, sticky="w")

input_text = tk.Text(frame, height=5, width=40)
input_text.grid(row=1, column=0, padx=5, pady=5)

output_label = ttk.Label(frame, text="Converted Text:")
output_label.grid(row=2, column=0, sticky="w")

output_text = tk.Text(frame, height=5, width=40)
output_text.grid(row=3, column=0, padx=5, pady=5)

case_option = tk.StringVar()
case_option.set("UPPERCASE")

case_label = ttk.Label(frame, text="Convert to:")
case_label.grid(row=4, column=0, sticky="w")

uppercase_radio = ttk.Radiobutton(frame, text="UPPERCASE", variable=case_option, value="UPPERCASE")
lowercase_radio = ttk.Radiobutton(frame, text="lowercase", variable=case_option, value="lowercase")
titlecase_radio = ttk.Radiobutton(frame, text="Title Case", variable=case_option, value="Title Case")
sentencecase_radio = ttk.Radiobutton(frame, text="Sentence case", variable=case_option, value="Sentence case")

uppercase_radio.grid(row=5, column=0, sticky="w")
lowercase_radio.grid(row=6, column=0, sticky="w")
titlecase_radio.grid(row=7, column=0, sticky="w")
sentencecase_radio.grid(row=8, column=0, sticky="w")

convert_button = ttk.Button(frame, text="Convert Text", command=convert_text)
convert_button.grid(row=9, column=0, pady=10)

space_button = ttk.Button(frame, text="Remove Extra Spaces", command=remove_extra_spaces)
space_button.grid(row=10, column=0, pady=5)

find_label = ttk.Label(frame, text="Find:")
find_label.grid(row=11, column=0, sticky="w")
find_entry = ttk.Entry(frame)
find_entry.grid(row=11, column=1, padx=5)

replace_label = ttk.Label(frame, text="Replace with:")
replace_label.grid(row=12, column=0, sticky="w")
replace_entry = ttk.Entry(frame)
replace_entry.grid(row=12, column=1, padx=5)

find_replace_button = ttk.Button(frame, text="Find and Replace", command=find_and_replace)
find_replace_button.grid(row=13, column=0, pady=5)

clear_button = ttk.Button(frame, text="Clear", command=clear_text)
clear_button.grid(row=13, column=1, pady=5)

root.mainloop()
