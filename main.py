
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def count_words(file_contents):
    words = file_contents.split()
    # print(words)
    counter = 0
    print(len(words))


count_words(file_contents)