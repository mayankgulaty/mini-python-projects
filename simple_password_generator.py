import random
import string

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    char_pool = string.ascii_lowercase
    if include_uppercase:
        char_pool += string.ascii_uppercase
    if include_numbers:
        char_pool += string.digits
    if include_symbols:
        char_pool += string.punctuation

    return ''.join(random.choice(char_pool) for _ in range(length))

def main():
    length = int(input("Enter the password length: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    password = generate_password(length, include_uppercase, include_numbers, include_symbols)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
