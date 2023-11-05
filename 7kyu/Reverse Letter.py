import re
def reverse_letter(string):
    filtered = re.sub(r'[^a-zA-Z]', '', string)
    return filtered[::-1]

    