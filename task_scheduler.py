import schedule
import time
import subprocess
import datetime

def run_task(task):
    print(f"Executing task at {datetime.datetime.now()}: {task}")
    try:
        result = subprocess.run(task, shell=True, capture_output=True, text=True)
        print(f"Output:\n{result.stdout}")
        if result.stderr:
            print(f"Error:\n{result.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Example of scheduling a task
    task = input("Enter the command to schedule: ")
    schedule_type = input("Enter 'daily' or 'interval' for the schedule type: ")
    if schedule_type == 'daily':
        time = input("Enter the time to run the task (HH:MM format): ")
        schedule.every().day.at(time).do(run_task, task)
    elif schedule_type == 'interval':
        interval = int(input("Enter the interval in seconds: "))
        schedule.every(interval).seconds.do(run_task, task)
    else:
        print("Invalid schedule type")
        return

    print("Task Scheduler running. Press Ctrl+C to exit.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Task Scheduler stopped.")

if __name__ == "__main__":
    main()
