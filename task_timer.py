import time
import json

def start_timer():
    return time.time()

def stop_timer(start_time):
    return time.time() - start_time

def save_log(task_name, duration, filename='task_log.json'):
    try:
        with open(filename, 'r') as file:
            logs = json.load(file)
    except FileNotFoundError:
        logs = []

    logs.append({'task': task_name, 'duration': duration})
    with open(filename, 'w') as file:
        json.dump(logs, file, indent=4)

def view_logs(filename='task_log.json'):
    try:
        with open(filename, 'r') as file:
            logs = json.load(file)
            for log in logs:
                print(f"Task: {log['task']}, Duration: {log['duration']:.2f} seconds")
    except FileNotFoundError:
        print("No logs found.")

def main():
    while True:
        action = input("\nChoose an action - Start (S), View Logs (V), Exit (E): ").upper()

        if action == 'S':
            task_name = input("Enter the task name: ")
            print("Timer started. Press Enter to stop.")
            start_time = start_timer()
            input()
            duration = stop_timer(start_time)
            save_log(task_name, duration)
            print(f"Timer stopped. Duration: {duration:.2f} seconds")

        elif action == 'V':
            view_logs()

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
