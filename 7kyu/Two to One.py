def longest(a1, a2):
    unique = set(a1+a2)
    return ''.join(sorted(unique))