import requests

# Define the ImgFlip API URL
IMGFLIP_API = "https://api.imgflip.com/caption_image"

# Replace with your ImgFlip API username and password
USERNAME = 'YourImgFlipUsername'
PASSWORD = 'YourImgFlipPassword'

def generate_meme(template_id, text_top, text_bottom):
    params = {
        'template_id': template_id,
        'username': USERNAME,
        'password': PASSWORD,
        'text0': text_top,
        'text1': text_bottom,
    }

    response = requests.post(IMGFLIP_API, params=params)

    if response.status_code == 200:
        data = response.json()
        meme_url = data['data']['url']
        return meme_url
    else:
        return None

if __name__ == "__main__":
    template_id = 61579  # Replace with the template ID of the meme you want to use
    text_top = "Text at the top"
    text_bottom = "Bottom text"

    meme_url = generate_meme(template_id, text_top, text_bottom)

    if meme_url:
        print(f"Meme URL: {meme_url}")
    else:
        print("Failed to generate the meme. Check your credentials and template ID.")
