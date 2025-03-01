def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def count_words(text):
    return len(text.split())

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

main()
