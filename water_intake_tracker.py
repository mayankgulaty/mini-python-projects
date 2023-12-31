class WaterIntakeTracker:
    def __init__(self):
        self.total_intake = 0
        self.goal = 2000  # default goal in milliliters

    def log_intake(self, amount):
        self.total_intake += amount
        print(f"Logged {amount} ml. Total for today: {self.total_intake} ml.")

    def set_goal(self, goal_amount):
        self.goal = goal_amount
        print(f"Daily goal set to {self.goal} ml.")

    def check_goal(self):
        if self.total_intake >= self.goal:
            print("Congratulations! You've reached your daily water intake goal.")
        else:
            print(f"You are {self.goal - self.total_intake} ml away from your goal.")

def main():
    tracker = WaterIntakeTracker()
    tracker.set_goal(int(input("Set your daily water intake goal in ml: ")))

    while True:
        action = input("\nChoose an action - Log (L), Check Goal (C), Exit (E): ").upper()

        if action == 'L':
            amount = int(input("Enter the amount of water in ml you've just drunk: "))
            tracker.log_intake(amount)

        elif action == 'C':
            tracker.check_goal()

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
