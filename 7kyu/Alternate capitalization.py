def capitalize(s):
    resp = ""
    resp2 = ""
    for i in range(len(s)):
        if i % 2 == 0:
            resp  += s[i].upper()
            resp2 += s[i]
        else:
            resp  += s[i]
            resp2 += s[i].upper()
    return [resp,resp2]
            
        