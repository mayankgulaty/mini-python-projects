import requests
import os

def download_image(url, directory, filename=None):
    try:
        response = requests.get(url)
        response.raise_for_status()

        if not filename:
            filename = url.split("/")[-1]
        file_path = os.path.join(directory, filename)

        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"Image saved as {file_path}")
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")

def main():
    urls = input("Enter image URLs separated by a comma: ").split(',')
    directory = input("Enter directory to save images: ")

    if not os.path.exists(directory):
        os.makedirs(directory)

    for url in urls:
        download_image(url.strip(), directory)

if __name__ == "__main__":
    main()
