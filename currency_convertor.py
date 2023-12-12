import tkinter as tk
from tkinter import ttk, messagebox
import requests

def get_exchange_rates(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()['rates']
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch exchange rates: {e}")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    try:
        from_rate = rates[from_currency]
        to_rate = rates[to_currency]
        converted_amount = (amount / from_rate) * to_rate
        return converted_amount
    except Exception as e:
        messagebox.showerror("Conversion Error", str(e))

def on_convert():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        result = convert_currency(amount, from_currency, to_currency, rates)
        result_label.config(text=f"{result:.2f} {to_currency}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid amount.")

# Setup the GUI
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x250")

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
rates = get_exchange_rates(API_URL)
if not rates:
    root.destroy()

# Main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(expand=True, fill="both")

# Amount
amount_frame = ttk.Frame(main_frame)
amount_frame.pack(fill="x", pady=5)
tk.Label(amount_frame, text="Amount:").pack(side="left")
amount_entry = tk.Entry(amount_frame)
amount_entry.pack(side="right", expand=True, fill="x")

# From Currency
from_currency_var = tk.StringVar(value="USD")
from_currency_dropdown = ttk.Combobox(main_frame, textvariable=from_currency_var, values=list(rates.keys()), state="readonly")
from_currency_dropdown.pack(fill="x", pady=5)

# To Currency
to_currency_var = tk.StringVar(value="EUR")
to_currency_dropdown = ttk.Combobox(main_frame, textvariable=to_currency_var, values=list(rates.keys()), state="readonly")
to_currency_dropdown.pack(fill="x", pady=5)

# Convert Button
convert_button = tk.Button(main_frame, text="Convert", command=on_convert)
convert_button.pack(pady=10)

# Result
result_frame = ttk.Frame(main_frame)
result_frame.pack(fill="x")
result_label = tk.Label(result_frame, text="Result: ", font=("Arial", 12))
result_label.pack()

root.mainloop()
