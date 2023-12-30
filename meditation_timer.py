import time
# Optional: from playsound import playsound

def meditation_timer(duration, interval=0):
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        remaining = end_time - time.time()
        print(f"Time remaining: {int(remaining // 60)}:{int(remaining % 60):02d}", end="\r")
        time.sleep(1)

        if interval and time.time() - start_time >= interval:
            start_time += interval
            # Optional: playsound('bell_sound.mp3')

    print("\nMeditation session ended.")
    # Optional: playsound('end_sound.mp3')

def main():
    duration = int(input("Enter meditation duration in seconds: "))
    interval = int(input("Enter interval for reminders in seconds (0 for no reminders): "))
    meditation_timer(duration, interval)

if __name__ == "__main__":
    main()
