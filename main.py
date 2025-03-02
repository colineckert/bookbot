import sys
from stats import get_num_words, get_char_count, get_sorted_char_counts

def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()

def main():
    input = sys.argv
    if len(input) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = input[1]

    print("============ BOOKBOT ============")

    print(f"Analyzing book found at {path_to_book}...")
    text = get_book_text(path_to_book)
    num_words = get_num_words(text)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    num_chars = get_char_count(text)
    sorted_chars_list = get_sorted_char_counts(num_chars)
    for char, count in sorted_chars_list:
        print(f"{char}: {count}")

    print("============= END ===============")

main()
