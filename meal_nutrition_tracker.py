import json
import os
from datetime import datetime

def load_meal_data(filename='meal_data.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_meal_data(data, filename='meal_data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def log_meal_entry(data):
    date = datetime.now().strftime('%Y-%m-%d')
    meal_name = input("Enter the meal name: ")
    calories = int(input("Enter calories: "))
    protein = int(input("Enter protein (grams): "))
    carbs = int(input("Enter carbs (grams): "))
    fats = int(input("Enter fats (grams): "))

    meal_entry = {
        'date': date,
        'meal_name': meal_name,
        'nutrition': {
            'calories': calories,
            'protein': protein,
            'carbs': carbs,
            'fats': fats
        }
    }
    data.append(meal_entry)
    save_meal_data(data)
    print("Meal entry recorded.")

def view_nutritional_summary(data):
    nutrition_totals = {'calories': 0, 'protein': 0, 'carbs': 0, 'fats': 0}
    for entry in data:
        for key in nutrition_totals:
            nutrition_totals[key] += entry['nutrition'][key]
    print(f"Total Nutrition - Calories: {nutrition_totals['calories']}, Protein: {nutrition_totals['protein']}g, Carbs: {nutrition_totals['carbs']}g, Fats: {nutrition_totals['fats']}g")

def main():
    data = load_meal_data()

    while True:
        action = input("\nChoose an action - Log Meal (L), View Summary (S), Exit (E): ").upper()

        if action == 'L':
            log_meal_entry(data)

        elif action == 'S':
            view_nutritional_summary(data)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
