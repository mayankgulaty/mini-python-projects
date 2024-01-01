from PIL import Image, ImageDraw

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def complementary_color(rgb_color):
    comp_color = tuple(255 - x for x in rgb_color)
    return comp_color

def create_palette_image(base_color, complementary):
    img = Image.new('RGB', (200, 100), '#FFFFFF')
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, 100, 100], fill=base_color)
    draw.rectangle([100, 0, 200, 100], fill=complementary)

    img.show()

def main():
    base_hex = input("Enter a base color in HEX format (e.g., #FF5733): ")
    base_rgb = hex_to_rgb(base_hex)
    complementary = complementary_color(base_rgb)

    print(f"Base Color: {base_rgb}, Complementary Color: {complementary}")
    create_palette_image(base_rgb, complementary)

if __name__ == "__main__":
    main()
