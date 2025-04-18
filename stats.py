# Fcion que va al camino del archivo, lo lee y llena la variable string data mientras .rstrip
# remueve cualquier espacio al final del string
# la primera en la linea 17

# Fcion que trae el texto, corta el string cuando hay un espacio y luego la cuenta
"""def count_words(text):
    words = text.split()
    return len(words)"""

# Trae el texto del libro
"""libro = get_book_text()"""

# Cuenta las palabras de la funcion
"""num_words = count_words(libro)"""

def get_book_text():
    with open('books/frankenstein.txt', 'r') as file:
        data = file.read().rstrip()
    return data

textobajo = get_book_text().lower() 

freq = {}

for letra in textobajo:
    if letra in freq:
        freq[letra] += 1
    else:
        freq[letra] = 1


def sort_character_counts(freq):
    char_list = []
    for char, count in freq.items():
        char_list.append({"character": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def count_words(text):
    # Split the text into words and count them
    words = text.split()
    return len(words)

def count_letters(text):
    # Convert to lowercase and count each letter
    text = text.lower()
    freq = {}
    for letter in text:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1
    return freq