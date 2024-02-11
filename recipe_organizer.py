import json
import os


def load_recipes(filename='recipes.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}


def save_recipes(recipes, filename='recipes.json'):
    with open(filename, 'w') as file:
        json.dump(recipes, file, indent=4)


def add_recipe(recipes):
    name = input("Enter the recipe name: ")
    category = input("Enter the recipe category: ")
    ingredients = input("Enter the ingredients (separate by comma): ").split(',')
    instructions = input("Enter the cooking instructions: ")

    recipes[name] = {
        'category': category,
        'ingredients': ingredients,
        'instructions': instructions
    }
    save_recipes(recipes)
    print(f"Recipe '{name}' added.")


def search_recipes(recipes):
    category = input("Enter the category to search for: ")
    found_recipes = {name: details for name, details in recipes.items() if details['category'] == category}

    if found_recipes:
        for name, details in found_recipes.items():
            print(
                f"\n{name} - Ingredients: {', '.join(details['ingredients'])}\nInstructions: {details['instructions']}")
    else:
        print("No recipes found in this category.")


def view_recipe(recipes):
    name = input("Enter the recipe name to view: ")
    if name in recipes:
        recipe = recipes[name]
        print(
            f"\n{name} - Category: {recipe['category']}\nIngredients: {', '.join(recipe['ingredients'])}\nInstructions: {recipe['instructions']}")
    else:
        print("Recipe not found.")


def main():
    recipes = load_recipes()

    while True:
        action = input("\nChoose an action - Add (A), Search (S), View (V), Exit (E): ").upper()

        if action == 'A':
            add_recipe(recipes)

        elif action == 'S':
            search_recipes(recipes)

        elif action == 'V':
            view_recipe(recipes)

        elif action == 'E':
            break


if __name__ == "__main__":
    main()
