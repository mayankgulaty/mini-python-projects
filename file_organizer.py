import os
import shutil

def organize_directory(path, custom_folders=None):
    if custom_folders is None:
        custom_folders = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif'],
            'Documents': ['.pdf', '.docx', '.txt'],
            'Music': ['.mp3', '.wav'],
            # Add more types as needed
        }

    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file)[1].lower()
            folder_name = next((folder for folder, exts in custom_folders.items() if file_ext in exts), 'Others')
            folder_path = os.path.join(path, folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            shutil.move(file_path, os.path.join(folder_path, file))
            print(f"Moved: {file} -> {folder_path}")

if __name__ == "__main__":
    directory_path = input("Enter the directory path to organize: ")
    organize_directory(directory_path)
