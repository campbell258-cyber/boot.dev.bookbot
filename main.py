import sys
from stats import get_book_text,word_count, char_count, sort_on
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    char_dict = char_count(text)
    word_count(text)
    print("--------- Character Count -------")
    sort_on(char_dict)
    print("============= END ===============")