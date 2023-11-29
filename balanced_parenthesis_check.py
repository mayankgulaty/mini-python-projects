def is_balanced_parentheses(s):
    stack = []

    # Define a mapping for opening and closing parentheses
    parentheses_mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in parentheses_mapping.values():
            stack.append(char)
        elif char in parentheses_mapping.keys():
            if not stack or stack.pop() != parentheses_mapping[char]:
                return False

    return not stack


if __name__ == "__main__":
    expression = input("Enter a string with parentheses: ")

    if is_balanced_parentheses(expression):
        print("The parentheses are balanced.")
    else:
        print("The parentheses are not balanced.")
