def generate_fibonacci(limit):
    fibonacci_numbers = [0, 1]

    while True:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]

        if next_number <= limit:
            fibonacci_numbers.append(next_number)
        else:
            break

    return fibonacci_numbers

if __name__ == "__main__":
    # Input the limit for the Fibonacci sequence
    limit = int(input("Enter the limit for the Fibonacci sequence: "))

    # Call the utility function to generate Fibonacci numbers
    fibonacci_sequence = generate_fibonacci(limit)

    # Display the result
    print("Fibonacci Sequence:")
    print(fibonacci_sequence)
