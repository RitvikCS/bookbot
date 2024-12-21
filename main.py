def sort_on(item):
    return item[1]

def main():    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(text)} words found in document\n")

    char_count = character_count(text)
    sorted_char_count = sorted(char_count.items(), key=sort_on, reverse=True)

    for key, values in sorted_char_count:
        print(f"The {repr(key)} character was found {values} times")
    print("--- End report ---")

def word_count(text):
    word_list = text.split()
    return len(word_list)

def character_count(text):
    count = {}
    for i in text.lower():
        if i.isalpha():
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
    return count

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()