import random

def generate_project_idea(categories):
    idea_elements = [random.choice(category) for category in categories.values()]
    return ' + '.join(idea_elements)

def main():
    categories = {
        'Application Type': ['Web App', 'Mobile App', 'Desktop App', 'CLI Tool'],
        'Theme': ['Education', 'Health', 'Productivity', 'Entertainment', 'Finance'],
        'Technology': ['Python', 'JavaScript', 'React', 'Flutter', 'Machine Learning']
    }

    print("Simple Project Idea Generator")
    while True:
        action = input("\nPress Enter to generate a new project idea or type 'exit' to quit: ")

        if action.lower() == 'exit':
            break

        project_idea = generate_project_idea(categories)
        print(f"Generated Project Idea: {project_idea}")

if __name__ == "__main__":
    main()
