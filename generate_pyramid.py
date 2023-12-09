def generate_pyramid(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

if __name__ == "__main__":
    print("Welcome to the ASCII Art Pyramid Generator!")

    try:
        pyramid_height = int(input("Enter the height of the pyramid: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
    else:
        generate_pyramid(pyramid_height)
