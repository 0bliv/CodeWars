def nb_dig(n, d):  
    c = 0
    for k in range(n+1):
        op = str(k**2)
        c += str.count(str(d))
    return c