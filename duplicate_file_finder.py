import os
import hashlib
from collections import defaultdict

def hash_file(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicates(directory):
    duplicates = defaultdict(list)
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            filehash = hash_file(filepath)
            duplicates[filehash].append(filepath)
    return duplicates

def main():
    directory = input("Enter the directory to scan for duplicates: ")
    duplicate_files = find_duplicates(directory)

    for filehash, files in duplicate_files.items():
        if len(files) > 1:
            print(f"Duplicate files for hash {filehash}:")
            for file in files:
                print(f"\t{file}")

if __name__ == "__main__":
    main()
