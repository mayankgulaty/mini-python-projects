import shutil
import os
import datetime

def backup_files(source, destination, incremental=False):
    if incremental and os.path.exists(destination):
        # Implement incremental backup logic (skip if file exists)
        pass
    else:
        if os.path.isdir(source):
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)
    print(f"Backup of '{source}' completed to '{destination}'")

def main():
    source_path = input("Enter the path of the file/directory to backup: ")
    backup_path = input("Enter the backup destination path: ")
    incremental = input("Perform incremental backup? (yes/no): ").lower() == 'yes'

    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    destination_path = os.path.join(backup_path, f"backup_{timestamp}")

    try:
        backup_files(source_path, destination_path, incremental)
    except Exception as e:
        print(f"Error during backup: {e}")

if __name__ == "__main__":
    main()
