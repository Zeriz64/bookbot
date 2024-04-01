def main():
    book_path = ("books/frankenstein.txt")
    text = get_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    sorted_list = get_sorted_count(character_count)
    print(f"--- Report on Frankenstein---\n\nWord Count: {word_count}")
    for dict in sorted_list:
        print(f"Amount of {dict["character"]}: {dict["amount"]}")

def get_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(string):
    return len(string.split())

def get_character_count(text):
    lowercase = text.lower()
    characters = {}
    for character in lowercase:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def get_sorted_count(dict):
    sorted_list = []
    for character in dict:
        if character.isalpha():
            sorted_list.append({"character": character, "amount": dict[character]})
    sorted_list.sort(reverse=True, key=sort)
    return sorted_list

def sort(dict):
    return dict["amount"]
main()