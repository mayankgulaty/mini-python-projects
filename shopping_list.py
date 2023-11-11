import tkinter as tk
from tkinter import ttk

class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append({"name": item, "purchased": False})

    def mark_as_purchased(self, index):
        if 0 <= index < len(self.items):
            self.items[index]["purchased"] = True

    def clear_list(self):
        self.items.clear()

class ShoppingListApp:
    def __init__(self, root):
        self.shopping_list = ShoppingList()

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, padx=20, pady=20)

        self.item_label = ttk.Label(self.frame, text="Add Item to Shopping List:")
        self.item_label.grid(row=0, column=0, sticky="w")

        self.item_entry = ttk.Entry(self.frame)
        self.item_entry.grid(row=0, column=1, padx=5)

        self.add_button = ttk.Button(self.frame, text="Add Item", command=self.add_item)
        self.add_button.grid(row=0, column=2, pady=10)

        self.shopping_listbox = tk.Listbox(self.frame, height=10, selectmode=tk.SINGLE)
        self.shopping_listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=10)

        self.purchase_button = ttk.Button(self.frame, text="Mark as Purchased", command=self.mark_as_purchased)
        self.purchase_button.grid(row=2, column=0, pady=5)

        self.clear_button = ttk.Button(self.frame, text="Clear List", command=self.clear_list)
        self.clear_button.grid(row=2, column=1, pady=5)

        self.update_list()

    def add_item(self):
        item = self.item_entry.get()
        if item:
            self.shopping_list.add_item(item)
            self.update_list()
            self.item_entry.delete(0, tk.END)

    def mark_as_purchased(self):
        selected_index = self.shopping_listbox.curselection()
        if selected_index:
            self.shopping_list.mark_as_purchased(selected_index[0])
            self.update_list()

    def clear_list(self):
        self.shopping_list.clear_list()
        self.update_list()

    def update_list(self):
        self.shopping_listbox.delete(0, tk.END)
        for item in self.shopping_list.items:
            status = " (Purchased)" if item["purchased"] else ""
            self.shopping_listbox.insert(tk.END, f"{item['name']}{status}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Shopping List")
    app = ShoppingListApp(root)
    root.mainloop()
