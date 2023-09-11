def is_pangram(sentence):
    seen_letters = set()
    for char in sentence:
        
        char = char.lower()  
        if char.isalpha():
            seen_letters.add(char)

    return len(seen_letters) == 26
