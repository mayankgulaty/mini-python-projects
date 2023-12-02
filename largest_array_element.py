def find_largest_element(numbers):
    if not numbers:
        return None  # Return None if the list is empty

    largest_element = numbers[0]

    for number in numbers[1:]:
        if number > largest_element:
            largest_element = number

    return largest_element

if __name__ == "__main__":
    # Input elements for the array
    input_numbers = input("Enter numbers separated by spaces: ").split()

    # Convert input strings to integers
    numbers = [int(num) for num in input_numbers]

    # Call the utility function to find the largest element
    largest_element = find_largest_element(numbers)

    # Display the result
    if largest_element is not None:
        print(f"The largest element in the array is: {largest_element}")
    else:
        print("The array is empty.")
