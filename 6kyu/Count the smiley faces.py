def count_smileys(arr):
    count = 0
    find = [":)", ":D", ";)", ";D", ":-)", ":-D", ";-)", ";-D", ":~)", ":~D", ";~)", ";~D"]
    
    if len(arr) == 0:
        return 0
    
    for char in arr:
        if char in find:
            count+= 1
    return count