from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)

    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)

    with open(file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt a file? ").upper()
    file_path = input("Enter the path of the file: ")
    key = input("Enter the encryption/decryption key: ")

    if choice == 'E':
        encrypt_file(file_path, key)
        print("File encrypted successfully.")
    elif choice == 'D':
        decrypt_file(file_path, key)
        print("File decrypted successfully.")

if __name__ == "__main__":
    main()
