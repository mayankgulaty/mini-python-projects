def create_meal_plan():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meal_plan = {day: {"Breakfast": "", "Lunch": "", "Dinner": "", "Snacks": ""} for day in days_of_week}

    for day in days_of_week:
        print(f"\n{day}:")
        for meal in meal_plan[day]:
            meal_plan[day][meal] = input(f"  Enter {meal}: ")

    return meal_plan

def display_meal_plan(meal_plan):
    for day, meals in meal_plan.items():
        print(f"\n{day}:")
        for meal, dish in meals.items():
            print(f"  {meal}: {dish}")

def main():
    print("Simple Meal Planner")
    meal_plan = create_meal_plan()

    print("\nYour Weekly Meal Plan:")
    display_meal_plan(meal_plan)

if __name__ == "__main__":
    main()
