def find_meals_by_ingredients(available_ingredients, meal_database):
    suggested_meals = []
    for meal, ingredients in meal_database.items():
        if all(item in available_ingredients for item in ingredients):
            suggested_meals.append(meal)
    return suggested_meals

def main():
    meal_database = {
        'Spaghetti Carbonara': ['pasta', 'eggs', 'bacon', 'parmesan cheese'],
        'Vegetable Stir Fry': ['vegetables', 'soy sauce', 'ginger', 'garlic'],
        'Tomato Soup': ['tomato', 'onion', 'garlic', 'vegetable broth'],
        # Add more meals and ingredients as desired
    }

    print("Enter the ingredients you have (separate each by comma): ")
    available_ingredients = input().split(',')

    available_ingredients = [ingredient.strip().lower() for ingredient in available_ingredients]

    suggested_meals = find_meals_by_ingredients(available_ingredients, meal_database)

    if suggested_meals:
        print("\nBased on the ingredients you have, you can make:")
        for meal in suggested_meals:
            print(f"- {meal}")
    else:
        print("No meal suggestions available with the given ingredients.")

if __name__ == "__main__":
    main()
