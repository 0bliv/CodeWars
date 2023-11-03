def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    
    resp = 0
    current = begin_number
    
    while current <= end_number:   
        resp+=current
        current+=step
        
    return resp