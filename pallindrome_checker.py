def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    return s == s[::-1]

if __name__ == "__main__":
    # Input a string to check for palindrome
    input_string = input("Enter a string to check for palindrome: ")

    # Call the utility function to check if the string is a palindrome
    if is_palindrome(input_string):
        print(f"{input_string} is a palindrome.")
    else:
        print(f"{input_string} is not a palindrome.")
