def text_to_words(text) ->str:
    words = text.split()
    count = 0
    for word in words:
        count +=1
    return count  

def count_all_words(text) -> dict[str, int]:
    all_text = text.lower()
    char_count = {}
    for character in all_text:
        if character in char_count:
            char_count[character] = char_count[character] + 1
        else:
            char_count[character] = 1    

    return char_count  

def sort_on(char_count_tuple: tuple[str,int]) -> int:
    return char_count_tuple[1]


def chars_dict_to_sorted_list(char_count: dict[str, int]) -> list[tuple[str, int]]:
    empty_list = []
    for char in char_count:
        empty_list.append((char, char_count[char]))
    sorted_list = sorted(empty_list, reverse=True, key=sort_on)
    return sorted_list
