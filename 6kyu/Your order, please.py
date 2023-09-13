def order(sentence):
    sorted_words = sorted(sentence.split(), key=lambda word: int(''.join(filter(str.isdigit, word))))
    result = ' '.join(sorted_words)
    
    return result
