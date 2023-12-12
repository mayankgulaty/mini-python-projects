import tkinter as tk
from tkinter import ttk
import requests

def get_exchange_rates(api_url):
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception("Error fetching exchange rates")
    return response.json()['rates']

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        raise ValueError("Currency not supported")
    from_rate = rates[from_currency]
    to_rate = rates[to_currency]
    converted_amount = (amount / from_rate) * to_rate
    return converted_amount

def on_convert():
    amount = float(amount_entry.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()

    try:
        result = convert_currency(amount, from_currency, to_currency, rates)
        result_label.config(text=f"{result:.2f}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Setup the GUI
root = tk.Tk()
root.title("Currency Converter")

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
rates = get_exchange_rates(API_URL)

# Create widgets
amount_label = tk.Label(root, text="Amount:")
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

from_currency_var = tk.StringVar(value="USD")
from_currency_dropdown = ttk.Combobox(root, textvariable=from_currency_var, values=list(rates.keys()))
from_currency_dropdown.pack()

to_currency_var = tk.StringVar(value="EUR")
to_currency_dropdown = ttk.Combobox(root, textvariable=to_currency_var, values=list(rates.keys()))
to_currency_dropdown.pack()

convert_button = tk.Button(root, text="Convert", command=on_convert)
convert_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
