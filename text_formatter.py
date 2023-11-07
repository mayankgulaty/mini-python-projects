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

root.mainloop()
