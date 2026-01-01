def split_book(book_text):
    book_split = book_text.split()
    num_words = len(book_split)
    return num_words

def count_characters(book_text):
    char_dict = {}
    for char in book_text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def sort_chars(chars_dict):
    return chars_dict["num"]

def chars_dict_to_sorted_list(chars_dict):
    ordered_list = []
    for char in chars_dict:
        ordered_list.append({"char": char, "num": chars_dict[char]})
    ordered_list.sort(reverse=True, key=sort_chars)
    return ordered_list