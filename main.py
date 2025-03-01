from stats import get_num_words

def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

main()
