from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def scale_image(image, new_width=100):
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=25):
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value//range_width]
    return ascii_str

def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image, new_width)
    image = convert_to_grayscale(image)
    ascii_str = map_pixels_to_ascii_chars(image)

    img_ascii = [ascii_str[index:index + new_width] for index in range(0, len(ascii_str), new_width)]
    return "\n".join(img_ascii)

def main():
    path = input("Enter the path to the image file: ")
    width = int(input("Enter the desired width of the ASCII art: "))

    try:
        image = Image.open(path)
    except Exception as e:
        print(e)
        return

    ascii_art = convert_image_to_ascii(image, width)
    print(ascii_art)

if __name__ == "__main__":
    main()
