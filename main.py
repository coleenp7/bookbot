from stats import *
from sys import argv, exit
import os

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)  # Exit with error code 1
    
    book_path = argv[1]

    if not os.path.exists(book_path):
        print(f"Error: The file '{book_path}' does not exist.")
        exit(1) # Exit with error code 1

    with open(book_path) as f:
        file_contents = f.read()
    # print(file_contents)

    word_count = count_words(file_contents)
    characters = count_characters(file_contents)
    sorted_list = look_pretty(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
         if not item["char"].isalpha():
             continue
         print(f'{item['char']}: {item['num']}')
    print("============= END ===============")

main()
