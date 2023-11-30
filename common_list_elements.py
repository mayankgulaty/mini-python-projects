def find_common_elements(list1, list2):
    # Convert the input lists to sets for efficient intersection operation
    set1 = set(list1)
    set2 = set(list2)

    # Find the common elements using the intersection of sets
    common_elements = set1 & set2

    # Convert the result set back to a list
    return list(common_elements)

if __name__ == "__main__":
    # Input elements for the first list
    list1 = input("Enter elements for the first list (comma-separated): ").split(',')

    # Input elements for the second list
    list2 = input("Enter elements for the second list (comma-separated): ").split(',')

    # Call the utility function to find common elements
    common_elements = find_common_elements(list1, list2)

    # Display the result
    if common_elements:
        print(f"Common elements: {common_elements}")
    else:
        print("No common elements found.")
