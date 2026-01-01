from stats import split_book, count_characters, chars_dict_to_sorted_list
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

#"books/frankenstein.txt"

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    pass

def main():
    book = get_book_text(sys.argv[1])
    book_words = split_book(book)
    #print(f"Found {book_words} total words")
    #print(count_characters(book))

    chars = count_characters(book)
    sorted = chars_dict_to_sorted_list(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {book_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()