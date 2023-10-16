def alphabet_position(text):
    result = ""
    for char in text:
        if char.isalpha():
            # Convert the character to its position in the alphabet
            position = ord(char.lower()) - ord('a') + 1
            result += str(position) + " "
    # Remove the trailing space and return the result
    return result.strip()