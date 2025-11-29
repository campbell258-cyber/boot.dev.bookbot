def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        return file_contents
def word_count():
    text = get_book_text()
    words = text.split()
    num_words = 0
    for w in words:
        num_words += 1
    print(f"Found {num_words} total words")


word_count()