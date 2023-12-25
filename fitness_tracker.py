class FitnessTracker:
    def __init__(self):
        self.activities = {}

    def log_activity(self, activity_type, duration, distance):
        if activity_type not in self.activities:
            self.activities[activity_type] = {'total_duration': 0, 'total_distance': 0, 'sessions': 0}

        self.activities[activity_type]['total_duration'] += duration
        self.activities[activity_type]['total_distance'] += distance
        self.activities[activity_type]['sessions'] += 1

    def get_average_speed(self, activity_type):
        activity = self.activities.get(activity_type)
        if activity and activity['total_duration'] > 0:
            return activity['total_distance'] / activity['total_duration']
        else:
            return 0

    def display_summary(self):
        for activity_type, data in self.activities.items():
            average_speed = self.get_average_speed(activity_type)
            print(
                f"{activity_type} - Sessions: {data['sessions']}, Total Distance: {data['total_distance']} km, Average Speed: {average_speed:.2f} km/h")


def main():
    tracker = FitnessTracker()

    while True:
        print("\nFitness Tracker")
        activity = input("Enter the type of activity (or 'exit' to stop): ")
        if activity.lower() == 'exit':
            break
        duration = float(input("Enter the duration of the activity in hours: "))
        distance = float(input("Enter the distance of the activity in kilometers: "))

        tracker.log_activity(activity, duration, distance)

    tracker.display_summary()


if __name__ == "__main__":
    main()
