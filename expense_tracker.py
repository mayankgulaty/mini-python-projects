import tkinter as tk
from tkinter import ttk

expense_amounts = []

def add_expense():
    expense_description = description_entry.get()
    expense_amount = float(amount_entry.get())

    if expense_description and expense_amount:
        expenses_listbox.insert(tk.END, f"{expense_description}: ${expense_amount:.2f}")
        total_expenses_var.set(f"Total Expenses: ${sum(expense_amounts):.2f}")
        expense_description_var.set("")
        amount_entry.delete(0, tk.END)
        expense_amounts.append(expense_amount)

def remove_expense():
    selected_expense_index = expenses_listbox.curselection()
    if selected_expense_index:
        selected_amount = expense_amounts[selected_expense_index[0]]
        expenses_listbox.delete(selected_expense_index)
        expense_amounts.remove(selected_amount)
        total_expenses_var.set(f"Total Expenses: ${sum(expense_amounts):.2f}")

def clear_expenses():
    expenses_listbox.delete(0, tk.END)
    total_expenses_var.set("Total Expenses: $0.00")
    expense_amounts.clear()

root = tk.Tk()
root.title("Expense Tracker")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=20, pady=20)

description_label = ttk.Label(frame, text="Expense Description:")
description_label.grid(row=0, column=0, sticky="w")

description_entry = ttk.Entry(frame)
description_entry.grid(row=0, column=1, padx=5)

amount_label = ttk.Label(frame, text="Expense Amount ($):")
amount_label.grid(row=1, column=0, sticky="w")

amount_entry = ttk.Entry(frame)
amount_entry.grid(row=1, column=1, padx=5)

add_button = ttk.Button(frame, text="Add Expense", command=add_expense)
add_button.grid(row=2, column=0, pady=10)

remove_button = ttk.Button(frame, text="Remove Expense", command=remove_expense)
remove_button.grid(row=2, column=1, pady=10)

clear_button = ttk.Button(frame, text="Clear Expenses", command=clear_expenses)
clear_button.grid(row=3, column=0, pady=10)

expenses_listbox = tk.Listbox(frame, height=10, selectmode=tk.SINGLE)
expenses_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

total_expenses_var = tk.StringVar()
total_expenses_var.set("Total Expenses: $0.00")

total_expenses_label = ttk.Label(frame, textvariable=total_expenses_var)
total_expenses_label.grid(row=5, column=0, columnspan=2, pady=5)

expense_description_var = tk.StringVar()
expense_description_var.set("")

root.mainloop()
