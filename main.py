from stats import get_num_words, get_char_count, get_sorted_char_counts

def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()

def main():
    print("============ BOOKBOT ============")

    file_path = "books/frankenstein.txt"
    print(f"Analyzing book found at {file_path}...")

    text = get_book_text(file_path)
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
