import json
import os
from collections import defaultdict

def load_meal_plan(filename='meal_plan.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

def save_meal_plan(meal_plan, filename='meal_plan.json'):
    with open(filename, 'w') as file:
        json.dump(meal_plan, file, indent=4)

def add_meal(meal_plan):
    day = input("Enter the day of the week: ")
    meal_name = input("Enter the meal name: ")
    ingredients = input("Enter the ingredients needed (separate by comma): ").split(',')

    if day not in meal_plan:
        meal_plan[day] = {}
    meal_plan[day][meal_name] = ingredients
    save_meal_plan(meal_plan)
    print(f"Meal '{meal_name}' added for {day}.")

def generate_grocery_list(meal_plan):
    grocery_list = defaultdict(int)
    for day, meals in meal_plan.items():
        for ingredients in meals.values():
            for ingredient in ingredients:
                grocery_list[ingredient.strip()] += 1

    print("\nGrocery List:")
    for ingredient, count in grocery_list.items():
        print(f"- {ingredient} ({count})")

def main():
    meal_plan = load_meal_plan()

    while True:
        action = input("\nChoose an action - Add Meal (A), Generate Grocery List (G), Exit (E): ").upper()

        if action == 'A':
            add_meal(meal_plan)

        elif action == 'G':
            generate_grocery_list(meal_plan)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
