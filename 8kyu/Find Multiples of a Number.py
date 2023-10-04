def find_multiples(integer, limit):
    
    resp = []
    x = 0
    i = 1
    
    while x <= limit:
        x = (i * integer)
        if x <= limit:
            resp.append(x)
            i+=1
        
    return resp