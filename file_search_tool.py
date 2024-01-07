import os

def search_files(directory, search_term=None, extension=None, size=None):
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            if search_term and search_term not in filename:
                continue
            if extension and not filename.endswith(extension):
                continue
            if size:
                file_path = os.path.join(foldername, filename)
                if size > 0 and os.path.getsize(file_path) < size:
                    continue
                elif size < 0 and os.path.getsize(file_path) > -size:
                    continue

            print(os.path.join(foldername, filename))

def main():
    directory = input("Enter the directory to search: ")
    search_term = input("Enter a search term (or leave blank): ")
    extension = input("Enter file extension to search for (or leave blank): ")
    size = input("Enter file size to search for in bytes (+ for above, - for below, or leave blank): ")
    size = int(size) if size else None

    search_files(directory, search_term, extension, size)

if __name__ == "__main__":
    main()
