import os
import sys
import re

def count_word_in_file(file_path, word):
    """Count occurrences of 'word' in a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return re.findall(r'\bSancho\b.*\b[0-9]{4}\b', content)
    except Exception as e:
        print(f"Could not read {file_path}: {e}")
        return 0


def count_word_in_folder(folder_path, word):
    """Count occurrences of 'word' in each file in the folder"""
    # Check if the directory exists
    if not os.path.exists(folder_path):
        print(f"The directory {folder_path} does not exist.")
        return

    # List all files in the folder
    files = os.listdir(folder_path)

    # Iterate over all files
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        # Only process text files (or other files as needed)
        if os.path.isfile(file_path):
            word_count = count_word_in_file(file_path, word)
            if len(word_count) > 0:
                print(f"File: {file_name} - '{word}' appears {word_count} times.")


if __name__ == "__main__":
    folder = sys.argv[1]
    word = sys.argv[2]
    count_word_in_folder(folder, word)
