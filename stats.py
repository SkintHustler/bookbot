def word_count(book_text):
    count = book_text.split()
    num_count = len(count)

    return num_count

def count_characters(text):
    char_dict= {}

    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]


def sort_char_count(counts):
    result = []
    for char, num in counts.items():
            result.append({"char": char, "num": num})

    result.sort(reverse=True, key=sort_on)

    return result
