import random

def load_recipes(filename='recipes.txt'):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_recipes(recipes, filename='recipes.txt'):
    with open(filename, 'w') as file:
        file.writelines(f"{recipe}\n" for recipe in recipes)

def add_recipe(recipes):
    new_recipe = input("Enter the name of the new recipe: ")
    recipes.append(new_recipe)
    save_recipes(recipes)
    print(f"Added recipe: {new_recipe}")

def remove_recipe(recipes):
    recipe_to_remove = input("Enter the name of the recipe to remove: ")
    if recipe_to_remove in recipes:
        recipes.remove(recipe_to_remove)
        save_recipes(recipes)
        print(f"Removed recipe: {recipe_to_remove}")
    else:
        print("Recipe not found.")

def randomize_recipe(recipes):
    if recipes:
        print("How about trying this recipe today?")
        print(random.choice(recipes))
    else:
        print("No recipes available. Please add some recipes first.")

def main():
    recipes = load_recipes()

    while True:
        print("\nRecipe Randomizer")
        action = input("Choose an action - Add (A), Remove (R), Randomize (RND), Exit (E): ").upper()

        if action == 'A':
            add_recipe(recipes)

        elif action == 'R':
            remove_recipe(recipes)

        elif action == 'RND':
            randomize_recipe(recipes)

        elif action == 'E':
            break

if __name__ == "__main__":
    main()
