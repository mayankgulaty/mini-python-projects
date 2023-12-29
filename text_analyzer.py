from collections import Counter
import re

def analyze_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    words = re.findall(r'\w+', text.lower())
    word_count = len(words)
    char_count = len(text)
    word_freq = Counter(words)
    most_common_words = word_freq.most_common(5)

    print(f"Total Words: {word_count}")
    print(f"Total Characters: {char_count}")
    print("Most Common Words:")
    for word, freq in most_common_words:
        print(f"  {word}: {freq} times")

def main():
    file_path = input("Enter the path to the text file: ")
    analyze_text(file_path)

if __name__ == "__main__":
    main()
