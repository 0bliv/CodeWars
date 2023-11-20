def words_to_marks(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    value = sum(alphabet.index(c) + 1 for c in s)
    return value
    