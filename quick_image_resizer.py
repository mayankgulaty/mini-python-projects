from PIL import Image
import os

def resize_image(input_path, output_path, size, maintain_aspect_ratio=False):
    with Image.open(input_path) as img:
        if maintain_aspect_ratio:
            img.thumbnail(size, Image.ANTIALIAS)
        else:
            img = img.resize(size, Image.ANTIALIAS)
        img.save(output_path)

def batch_resize(directory, output_directory, size, maintain_aspect_ratio=False):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(output_directory, filename)
            resize_image(input_path, output_path, size, maintain_aspect_ratio)

def main():
    directory = input("Enter the directory of images to resize: ")
    output_directory = input("Enter the output directory for resized images: ")
    width = int(input("Enter the new width: "))
    height = int(input("Enter the new height: "))
    maintain_aspect_ratio = input("Maintain aspect ratio? (yes/no): ").lower() == 'yes'

    batch_resize(directory, output_directory, (width, height), maintain_aspect_ratio)

if __name__ == "__main__":
    main()
