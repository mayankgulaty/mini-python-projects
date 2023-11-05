import tkinter as tk

def on_click(btn_text):
    current_expression = expression.get()
    if btn_text == '=':
        try:
            result = str(eval(current_expression))
            expression.set(result)
        except Exception as e:
            expression.set("Error")
    elif btn_text == 'C':
        expression.set("")
    else:
        expression.set(current_expression + btn_text)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x400")

expression = tk.StringVar()
expression.set("")

entry = tk.Entry(root, textvariable=expression, font=("Helvetica", 20), bd=10, insertwidth=4, width=14, justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+',
]

row_val = 1
col_val = 0

for button_text in buttons:
    tk.Button(root, text=button_text, padx=20, pady=20, font=("Helvetica", 20), command=lambda text=button_text: on_click(text)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
