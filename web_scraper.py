import requests
from bs4 import BeautifulSoup

# URL of the news website to scrape (you can replace it with your desired website)
url = 'https://www.nbcnews.com/'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the HTML elements containing news headlines
    # This will vary depending on the structure of the website
    headlines = soup.find_all('h2', class_='storyline__headline')

    if headlines:
        print("Latest News Headlines:")
        for index, headline in enumerate(headlines, 1):
            print(f"{index}. {headline.text}")
    else:
        print("No headlines found on the website.")

else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
