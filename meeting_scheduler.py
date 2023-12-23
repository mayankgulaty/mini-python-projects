from datetime import datetime, timedelta

class Meeting:
    def __init__(self, title, start, end):
        self.title = title
        self.start = start
        self.end = end

class MeetingScheduler:
    def __init__(self):
        self.meetings = []

    def add_meeting(self, title, start, end):
        new_meeting = Meeting(title, start, end)
        for meeting in self.meetings:
            if (meeting.start < new_meeting.end) and (new_meeting.start < meeting.end):
                print("Cannot schedule meeting due to a time conflict.")
                return
        self.meetings.append(new_meeting)
        print(f"Meeting '{title}' scheduled.")

    def list_meetings(self):
        for meeting in self.meetings:
            print(f"{meeting.title} - From {meeting.start} to {meeting.end}")

def main():
    scheduler = MeetingScheduler()
    while True:
        print("\n1. Schedule a meeting\n2. List all meetings\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter meeting title: ")
            start_time = datetime.strptime(input("Enter start time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(input("Enter end time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
            scheduler.add_meeting(title, start_time, end_time)
        elif choice == '2':
            scheduler.list_meetings()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
