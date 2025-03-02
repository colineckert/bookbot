def get_num_words(text: str) -> int:
    return len(text.split())

def get_char_count(text: str) -> "dict[str, int]":
    char_dict = {}
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in char_dict:
                char_dict[lower_char] += 1
            else:
                char_dict[lower_char] = 1
    return char_dict

def get_sorted_char_counts(char_dict: "dict[str, int]"):
    return sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
