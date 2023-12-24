from datetime import datetime
import pytz

def convert_time(meeting_time, from_zone, to_zone):
    from_zone_tz = pytz.timezone(from_zone)
    to_zone_tz = pytz.timezone(to_zone)

    meeting_time_with_zone = from_zone_tz.localize(meeting_time)
    converted_time = meeting_time_with_zone.astimezone(to_zone_tz)

    return converted_time

def main():
    input_time_str = input("Enter the meeting time (YYYY-MM-DD HH:MM): ")
    from_zone = input("Enter the current time zone (e.g., 'US/Pacific'): ")
    to_zone = input("Enter the time zone to convert to (e.g., 'Asia/Tokyo'): ")

    meeting_time = datetime.strptime(input_time_str, "%Y-%m-%d %H:%M")
    converted_time = convert_time(meeting_time, from_zone, to_zone)

    print(f"The meeting time in {to_zone} is: {converted_time.strftime('%Y-%m-%d %H:%M')}")

if __name__ == "__main__":
    main()
