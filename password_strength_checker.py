import re

def check_password_strength(password):
    errors = []
    if len(password) < 8:
        errors.append("Password is less than 8 characters.")
    if not re.search("[0-9]", password):
        errors.append("Password does not contain a number.")
    if not re.search("[A-Z]", password):
        errors.append("Password does not contain an uppercase letter.")
    if not re.search("[a-z]", password):
        errors.append("Password does not contain a lowercase letter.")
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Password does not contain a special character.")

    if not errors:
        return "This is a strong password."
    else:
        return "Password weaknesses: " + ", ".join(errors)

def main():
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()
