import json
import os

def load_itinerary(filename='itinerary.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_itinerary(itinerary, filename='itinerary.json'):
    with open(filename, 'w') as file:
        json.dump(itinerary, file, indent=4)

def add_travel_detail(itinerary):
    category = input("Enter the category (Flight, Hotel, Activity, Dining): ")
    detail = input("Enter the detail for this category: ")

    if category not in itinerary:
        itinerary[category] = []
    itinerary[category].append(detail)
    save_itinerary(itinerary)
    print(f"Detail added under {category}.")

def view_itinerary(itinerary):
    if not itinerary:
        print("Your travel itinerary is empty.")
        return
    for category, details in itinerary.items():
        print(f"\n{category}:")
        for detail in details:
            print(f"  - {detail}")

def main():
    itinerary = load_itinerary()

    while True:
        action = input("\nChoose an action - Add Detail (A), View Itinerary (V), Exit (E): ").upper()

        if action == 'A':
            add_travel_detail(itinerary)

        elif action == 'V':
            view_itinerary(itinerary)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
