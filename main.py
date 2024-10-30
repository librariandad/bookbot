def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(count_chars(file_contents))

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_dict = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


main()
