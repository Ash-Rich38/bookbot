def get_character_count(text):
    text = text.lower()
    char_count = {}
    for char in text: # For each character in the text
        if char in char_count: # If character is in the dict char_count
            char_count[char] += 1 # Use the character e.g. a: and assign it a value base on total amount
        else:
            char_count[char] = 1

    organize_characters(char_count)

# Print the total count of words in the novel/book
def count_words(text):
    words = text.split()
    count = len(words)
    print(f"{count} words found in the document")
    return count

def organize_characters(char_count):
    bad_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '\n']
    
    for char, value in char_count.items():
        if char in bad_list:
            continue
        else:    
            print(f"The '{char}' character was found {value} times")   

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    print(f"--- Begin report of {book_path} ---")
    total_words = count_words(file_contents)
    character_count = get_character_count(file_contents)
    print(f"--- End report ---")

main()
