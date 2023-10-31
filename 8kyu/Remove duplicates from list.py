def distinct(seq):
    
    seen = set()
    resp = []
    
    for i in seq:
        if i not in seen:
            resp.append(i)
            seen.add(i)
            
    return resp