def binary_search(sorted_list, target):
    low, high = 0, len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = sorted_list[mid]

        if mid_element == target:
            return mid  # Target found, return its index
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

if __name__ == "__main__":
    # Input a sorted list of numbers
    sorted_numbers = [int(num) for num in input("Enter sorted numbers separated by spaces: ").split()]

    # Input the target number to search
    target_number = int(input("Enter the target number to search: "))

    # Call the utility function for binary search
    result_index = binary_search(sorted_numbers, target_number)

    # Display the result
    if result_index != -1:
        print(f"{target_number} found at index {result_index}.")
    else:
        print(f"{target_number} not found in the list.")
