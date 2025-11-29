def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        #print(file_contents)
        return file_contents

def word_count(text):
    words = text.split()
    num_words = 0
    for w in words:
        num_words += 1
    print(f"Found {num_words} total words")

def char_count(text):
    char_list_dict = {}
    text = text.lower()
    for c in text:
        if c.isalpha() == True:
            if c in char_list_dict:
                char_list_dict[c] = char_list_dict[c] + 1
            else:
                char_list_dict[c] = 1
    return char_list_dict
    
def sort_on(input_dict):
    sorted_items = sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
    for key, value in sorted_items:
        print(f"{key}: {value}")