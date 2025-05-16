def count_words(file_contents):
    word_count = file_contents.split()
    return len(word_count)

def count_chars(file_contents):
    char_count = {}
    for char in file_contents:
        current_char_count = 0
        char_lower = char.lower()
        if char_lower in char_count.keys():
            current_char_count = char_count[char_lower]
        char_count.update({char_lower:current_char_count + 1})
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_data(char_count):
    char_list = []
    for c in char_count:
        char_list.append({"char": c, "num": char_count[c]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

