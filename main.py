import sys
from stats import count_words
from stats import count_chars
from stats import sort_data

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    num_words = count_words(file_contents)
    char_count = count_chars(file_contents)
    sorted_list = sort_data(char_count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        char = dict["char"]
        if char.isalpha():
            print(f"{char}: {dict["num"]}")
    print("============= END ===============")

main()
