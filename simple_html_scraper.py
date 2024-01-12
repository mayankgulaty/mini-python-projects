import requests
from bs4 import BeautifulSoup


def fetch_and_parse_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")


def extract_data(soup, tag, attribute=None):
    if attribute:
        elements = soup.find_all(tag, attrs=attribute)
    else:
        elements = soup.find_all(tag)

    for element in elements:
        print(element.get_text())


def main():
    url = input("Enter the URL to scrape: ")
    tag = input("Enter the HTML tag to extract: ")
    attribute = input("Enter the HTML attribute (key=value) or leave blank: ")

    attr_dict = {}
    if attribute:
        key, value = attribute.split('=')
        attr_dict[key] = value

    soup = fetch_and_parse_url(url)
    if soup:
        extract_data(soup, tag, attr_dict)


if __name__ == "__main__":
    main()
