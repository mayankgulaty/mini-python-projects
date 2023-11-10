import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class WaterTracker:
    def __init__(self):
        self.daily_goal = 8  # Set default daily water goal to 8 cups
        self.daily_intake = 0

    def set_daily_goal(self, goal):
        self.daily_goal = goal

    def log_water_intake(self, amount):
        self.daily_intake += amount

    def get_progress(self):
        return min(self.daily_intake / self.daily_goal * 100, 100)

class WaterTrackerApp:
    def __init__(self, root):
        self.water_tracker = WaterTracker()

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, padx=20, pady=20)

        self.goal_label = ttk.Label(self.frame, text="Daily Water Goal (cups):")
        self.goal_label.grid(row=0, column=0, sticky="w")

        self.goal_entry = ttk.Entry(self.frame)
        self.goal_entry.grid(row=0, column=1, padx=5)

        self.set_goal_button = ttk.Button(self.frame, text="Set Goal", command=self.set_goal)
        self.set_goal_button.grid(row=0, column=2, pady=10)

        self.log_label = ttk.Label(self.frame, text="Log Water Intake (cups):")
        self.log_label.grid(row=1, column=0, sticky="w")

        self.log_entry = ttk.Entry(self.frame)
        self.log_entry.grid(row=1, column=1, padx=5)

        self.log_button = ttk.Button(self.frame, text="Log Intake", command=self.log_intake)
        self.log_button.grid(row=1, column=2, pady=10)

        self.progress_label = ttk.Label(self.frame, text="Progress:")
        self.progress_label.grid(row=2, column=0, sticky="w")

        self.progressbar = ttk.Progressbar(self.frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.progressbar.grid(row=2, column=1, columnspan=2, pady=10)

        self.update_progress()

    def set_goal(self):
        try:
            goal = float(self.goal_entry.get())
            if goal > 0:
                self.water_tracker.set_daily_goal(goal)
                messagebox.showinfo("Goal Set", f"Daily water goal set to {goal} cups.")
                self.goal_entry.delete(0, tk.END)
                self.update_progress()
            else:
                messagebox.showwarning("Invalid Goal", "Please enter a positive number for the goal.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the goal.")

    def log_intake(self):
        try:
            amount = float(self.log_entry.get())
            if amount >= 0:
                self.water_tracker.log_water_intake(amount)
                messagebox.showinfo("Intake Logged", f"Water intake of {amount} cups logged.")
                self.log_entry.delete(0, tk.END)
                self.update_progress()
            else:
                messagebox.showwarning("Invalid Intake", "Please enter a non-negative number for the intake.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the intake.")

    def update_progress(self):
        progress = self.water_tracker.get_progress()
        self.progressbar['value'] = progress
        self.progress_label.config(text=f"Progress: {progress:.1f}%")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Water Tracker")
    app = WaterTrackerApp(root)
    root.mainloop()
