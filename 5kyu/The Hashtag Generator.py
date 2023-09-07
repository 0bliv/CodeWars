def generate_hashtag(s):
    result = '#' + ''.join(word.capitalize() for word in s.split())
    return result if 1 < len(result) <= 140 else False
