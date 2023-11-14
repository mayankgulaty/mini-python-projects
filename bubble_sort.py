import tkinter as tk
import random
import time

class BubbleSortAnimation:
    def __init__(self, master, array_size=20):
        self.master = master
        self.master.title("Bubble Sort Animation")
        self.canvas = tk.Canvas(self.master, width=600, height=400)
        self.canvas.pack()

        self.array = [random.randint(10, 300) for _ in range(array_size)]
        self.rectangles = []

        self.draw_rectangles()

        self.start_button = tk.Button(self.master, text="Start Sorting", command=self.bubble_sort)
        self.start_button.pack()

    def draw_rectangles(self):
        for i, height in enumerate(self.array):
            x1, y1 = i * 30 + 10, 400
            x2, y2 = x1 + 20, 400 - height
            rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
            self.rectangles.append(rect)

    def update_rectangles(self):
        for i, rect in enumerate(self.rectangles):
            height = self.array[i]
            x1, y1 = i * 30 + 10, 400
            x2, y2 = x1 + 20, 400 - height
            self.canvas.coords(rect, x1, y1, x2, y2)

    def bubble_sort(self):
        n = len(self.array)

        for i in range(n):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]

                    # Update the rectangles to show the swapping
                    self.update_rectangles()
                    self.master.update()
                    time.sleep(0.1)

# Create the main window
root = tk.Tk()
app = BubbleSortAnimation(root)

# Run the application
root.mainloop()
