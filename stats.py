def get_num_words (text):
    words = text.split()
    print(f"Found {len(words)} total words")

def calculate_characters(text):
    lower_text = text.lower()
    characters = {}
    for char in lower_text:
        if not char.isalpha():
            continue
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_characters_by_frequency(char_dict):
    return sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    