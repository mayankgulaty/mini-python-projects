def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    return list(common_elements)

if __name__ == "__main__":
    list1 = input("Enter elements for the first list (comma-separated): ").split(',')
    list2 = input("Enter elements for the second list (comma-separated): ").split(',')

    common_elements = find_common_elements(list1, list2)

    if common_elements:
        print(f"Common elements: {common_elements}")
    else:
        print("No common elements found.")
