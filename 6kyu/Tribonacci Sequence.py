def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <= len(signature):
        return signature[:n]

    result = signature.copy() 
    
    while len(result) < n:
        next_term = sum(result[-len(signature):])  
        result.append(next_term)

    return result