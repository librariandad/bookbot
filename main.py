def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(count_words(file_contents))

def count_words(chunk_o_text):
    words = chunk_o_text.split()
    return len(words)

main()
