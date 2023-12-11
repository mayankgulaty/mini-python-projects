def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            print(f"File '{file_name}' created successfully.")
    except Exception as e:
        print(f"Error creating the file: {e}")

def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Content written to '{file_name}' successfully.")
    except Exception as e:
        print(f"Error writing to the file: {e}")

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Contents of '{file_name}':\n{content}")
    except Exception as e:
        print(f"Error reading the file: {e}")

def append_to_file(file_name, additional_content):
    try:
        with open(file_name, 'a') as file:
            file.write(additional_content)
        print(f"Additional content appended to '{file_name}' successfully.")
    except Exception as e:
        print(f"Error appending to the file: {e}")

if __name__ == "__main__":
    print("Welcome to the File Operations Program!")

    file_name = input("Enter the name of the file (including extension): ")

    create_file(file_name)

    content_to_write = input("Enter content to write to the file: ")
    write_to_file(file_name, content_to_write)

    read_file(file_name)

    additional_content = input("Enter additional content to append to the file: ")
    append_to_file(file_name, additional_content)

    read_file(file_name)
