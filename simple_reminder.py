import time
import datetime
import threading

def set_reminder(reminder_time, message):
    time_diff = (reminder_time - datetime.datetime.now()).total_seconds()
    if time_diff <= 0:
        print("Reminder time has already passed.")
        return

    threading.Timer(time_diff, lambda: print(f"Reminder: {message}")).start()
    print(f"Reminder set for {reminder_time} - '{message}'")

def main():
    while True:
        user_input = input("Set a reminder? (yes/no): ").lower()
        if user_input == 'no':
            break

        reminder_msg = input("Enter the reminder message: ")
        reminder_time_str = input("Enter the reminder time (YYYY-MM-DD HH:MM): ")
        reminder_time = datetime.datetime.strptime(reminder_time_str, "%Y-%m-%d %H:%M")

        set_reminder(reminder_time, reminder_msg)

if __name__ == "__main__":
    main()
