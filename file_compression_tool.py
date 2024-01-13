import zipfile
import os


def compress_files(file_paths, output_path):
    with zipfile.ZipFile(output_path, 'w') as zipf:
        for file in file_paths:
            zipf.write(file)
            print(f"Compressed: {file}")
    print(f"Created archive: {output_path}")


def decompress_file(zip_path, output_folder):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(output_folder)
        print(f"Extracted all files in {zip_path} to {output_folder}")


def main():
    action = input("Choose an action - Compress (C) or Decompress (D): ").upper()

    if action == 'C':
        files_to_compress = input("Enter the path of files to compress, separated by space: ").split()
        output_archive = input("Enter the path of the output ZIP file: ")
        compress_files(files_to_compress, output_archive)

    elif action == 'D':
        zip_to_decompress = input("Enter the path of the ZIP file to decompress: ")
        output_folder = input("Enter the path of the output folder: ")
        decompress_file(zip_to_decompress, output_folder)


if __name__ == "__main__":
    main()
