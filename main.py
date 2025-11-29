def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        return file_contents
    
from stats import word_count, char_count
word_count()
print(char_count())

