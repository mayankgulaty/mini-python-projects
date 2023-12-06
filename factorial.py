def calculate_factorial(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    elif n == 0:
        return 1  # Factorial of 0 is 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    # Input a non-negative integer for factorial calculation
    input_number = int(input("Enter a non-negative integer for factorial calculation: "))

    # Call the utility function to calculate the factorial
    factorial_result = calculate_factorial(input_number)

    # Display the result
    if factorial_result is not None:
        print(f"The factorial of {input_number} is: {factorial_result}")
    else:
        print("Factorial is not defined for negative numbers.")
