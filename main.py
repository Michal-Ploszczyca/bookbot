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


    char_list = []
    for char, count in char_count.items():
        # Create a dictionary fo each key-value pair
        if char.isalpha():
            char_list.append({"character": char, "num": count})

    char_list.sort(reverse=True, key=lambda x: x["num"])
    # print(char_list)
    for item in char_list:
        print(f"The '{item["character"]}' character was found {item["num"]} times")

main()