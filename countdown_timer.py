import tkinter as tk
from tkinter import ttk
import time
from tkinter import messagebox

class CountdownTimer:
    def __init__(self):
        self.duration = 0
        self.start_time = 0
        self.running = False

    def set_duration(self, minutes):
        self.duration = minutes * 60  # Convert minutes to seconds

    def start_timer(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            self.update_timer()

    def pause_timer(self):
        if self.running:
            self.running = False

    def reset_timer(self):
        self.running = False
        self.duration = 0

    def update_timer(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            remaining_time = max(0, self.duration - elapsed_time)
            if remaining_time > 0:
                root.after(1000, self.update_timer)
            else:
                self.running = False
                messagebox.showinfo("Timer Complete", "Time's up!")

class CountdownTimerApp:
    def __init__(self, root):
        self.countdown_timer = CountdownTimer()

        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, padx=20, pady=20)

        self.duration_label = ttk.Label(self.frame, text="Set Timer Duration (minutes):")
        self.duration_label.grid(row=0, column=0, sticky="w")

        self.duration_entry = ttk.Entry(self.frame)
        self.duration_entry.grid(row=0, column=1, padx=5)

        self.set_button = ttk.Button(self.frame, text="Set Timer", command=self.set_timer)
        self.set_button.grid(row=0, column=2, pady=10)

        self.start_button = ttk.Button(self.frame, text="Start Timer", command=self.start_timer)
        self.start_button.grid(row=1, column=0, pady=5)

        self.pause_button = ttk.Button(self.frame, text="Pause Timer", command=self.pause_timer)
        self.pause_button.grid(row=1, column=1, pady=5)

        self.reset_button = ttk.Button(self.frame, text="Reset Timer", command=self.reset_timer)
        self.reset_button.grid(row=1, column=2, pady=5)

    def set_timer(self):
        try:
            duration = int(self.duration_entry.get())
            if duration > 0:
                self.countdown_timer.set_duration(duration)
                messagebox.showinfo("Timer Set", f"Timer set for {duration} minutes.")
            else:
                messagebox.showwarning("Invalid Duration", "Please enter a positive number for the duration.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for the duration.")

    def start_timer(self):
        self.countdown_timer.start_timer()

    def pause_timer(self):
        self.countdown_timer.pause_timer()

    def reset_timer(self):
        self.countdown_timer.reset_timer()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Countdown Timer")
    app = CountdownTimerApp(root)
    root.mainloop()
