from stats import word_count, get_char_count, sort_and_order_char_count
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():

    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    contents = get_book_text(path_to_file)
    num_words = word_count(contents)
    dictionary = get_char_count(contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    chars = sort_and_order_char_count(dictionary)
    for item in chars.values():
        print(f"{item.char}: {item.count}") if item.char.isalpha() else None
    print("============= END ===============")

main()