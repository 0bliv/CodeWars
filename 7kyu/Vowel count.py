def get_count(sentence):
    v = set("aeiou") 
    return sum(1 for x in sentence if x in v)