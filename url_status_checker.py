import requests

def check_url_status(url):
    try:
        response = requests.get(url)
        return f"{url}: {response.status_code} - {response.reason}"
    except requests.RequestException as e:
        return f"{url}: Failed to connect - {e}"

def main():
    urls = input("Enter URLs separated by a comma: ").split(',')
    for url in urls:
        url = url.strip()
        print(check_url_status(url))

if __name__ == "__main__":
    main()
