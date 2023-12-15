from PIL import Image
import os

def resize_images(folder_path, output_size, maintain_aspect_ratio=False):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            with Image.open(image_path) as img:
                if maintain_aspect_ratio:
                    img.thumbnail(output_size, Image.ANTIALIAS)
                else:
                    img = img.resize(output_size, Image.ANTIALIAS)
                img.save(image_path)
                print(f"Resized {filename}")

def main():
    folder_path = input("Enter the path of the folder containing images: ")
    width = int(input("Enter the new width: "))
    height = int(input("Enter the new height: "))
    maintain_aspect_ratio = input("Maintain aspect ratio? (yes/no): ").lower() == 'yes'

    resize_images(folder_path, (width, height), maintain_aspect_ratio)

if __name__ == "__main__":
    main()
