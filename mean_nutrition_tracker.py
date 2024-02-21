import json
import os
from datetime import datetime

def load_meals(filename='meals.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_meals(meals, filename='meals.json'):
    with open(filename, 'w') as file:
        json.dump(meals, file, indent=4)

def add_meal(meals):
    meal_name = input("Enter the meal name: ")
    calories = float(input("Enter the number of calories: "))
    protein = float(input("Enter the amount of protein (in grams): "))
    carbs = float(input("Enter the amount of carbs (in grams): "))
    fats = float(input("Enter the amount of fats (in grams): "))
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')

    meals.append({
        'name': meal_name,
        'calories': calories,
        'protein': protein,
        'carbs': carbs,
        'fats': fats,
        'timestamp': timestamp
    })
    save_meals(meals)
    print("Meal added.")

def view_nutritional_summary(meals):
    total_calories, total_protein, total_carbs, total_fats = 0, 0, 0, 0
    for meal in meals:
        total_calories += meal['calories']
        total_protein += meal['protein']
        total_carbs += meal['carbs']
        total_fats += meal['fats']

    print(f"Total Calories: {total_calories}")
    print(f"Total Protein: {total_protein}g")
    print(f"Total Carbs: {total_carbs}g")
    print(f"Total Fats: {total_fats}g")

def main():
    meals = load_meals()

    while True:
        action = input("\nChoose an action - Add Meal (A), View Summary (V), Exit (E): ").upper()

        if action == 'A':
            add_meal(meals)

        elif action == 'V':
            view_nutritional_summary(meals)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
