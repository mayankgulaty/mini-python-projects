def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    # Input a number to check for primality
    input_number = int(input("Enter a number to check for primality: "))

    # Call the utility function to check if the number is prime
    if is_prime(input_number):
        print(f"{input_number} is a prime number.")
    else:
        print(f"{input_number} is not a prime number.")
