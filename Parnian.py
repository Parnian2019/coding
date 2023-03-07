import os
import re
from collections import Counter

def get_files(path):
    """
    Returns a list of all files in the given path and subdirectories
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_word_counts(file_list):
    """
    Returns a Counter object of all the unique words in the files with their counts
    """
    word_counts = Counter()
    for file in file_list:
        with open(file, "r") as f:
            content = f.read().lower()
            words = re.findall(r'\b\w+\b', content)
            word_counts.update(words)
    return word_counts

def print_word_counts(word_counts):
    """
    Prints the unique words in the files with their counts in descending order
    """
    for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
        if count > 2:
            print(f"{word} {count}")

if __name__ == "__main__":
    path ="C:/Program Files"
    file_list = get_files(path)
    word_counts = get_word_counts(file_list)
    print_word_counts(word_counts)
