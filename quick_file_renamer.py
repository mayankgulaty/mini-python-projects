import os

def rename_files(directory, pattern, dry_run=True):
    files = os.listdir(directory)
    for idx, filename in enumerate(files, start=1):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            new_name = pattern.replace('#', str(idx)) + file_extension
            new_file_path = os.path.join(directory, new_name)

            print(f"Renaming '{filename}' to '{new_name}'")
            if not dry_run:
                os.rename(file_path, new_file_path)

def main():
    directory = input("Enter the directory path: ")
    pattern = input("Enter the renaming pattern (use '#' for numbering): ")
    dry_run = input("Perform a dry run? (yes/no): ").lower() == 'yes'

    rename_files(directory, pattern, dry_run=dry_run)

    if dry_run:
        print("\nThis was a dry run. No files were actually renamed. Run again without dry run to rename files.")

if __name__ == "__main__":
    main()
