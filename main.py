def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    get_num_letters(text)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_letters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    sort_char_count = list(char_count.values())
    sort_char_count.sort()
    dict(sort_char_count)
    for key, value in sort_char_count():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")
    return char_count
    

    # print(to_lower)

main()