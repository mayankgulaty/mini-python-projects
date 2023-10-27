import requests
from bs4 import BeautifulSoup


def find_recipes(ingredients):
    query = '+'.join(ingredients)

    # Define the base URL for the Food Network search
    base_url = 'https://www.foodnetwork.com/recipes'

    # Create a session to manage cookies and headers
    session = requests.Session()

    # Perform a search on Food Network using a query
    search_url = f"{base_url}/search/{query}-"
    response = session.get(search_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        recipe_cards = soup.find_all('a', class_='o-ResultCard__a-Image')

        if recipe_cards:
            print("Here are some recipes you can make with your ingredients:\n")

            for i, card in enumerate(recipe_cards):
                title = card.find('img')['alt']
                link = card['href']
                print(f"{i + 1}. {title}")
                print(f"   Link: {link}\n")
        else:
            print("No recipes found with the given ingredients.")
    else:
        print("Error: Unable to access Food Network. Please check your internet connection.")


if __name__ == "__main__":
    ingredients = input("Enter the ingredients you have (space-separated): ").split()
    find_recipes(ingredients)
