def high_and_low(numbers):
    result = list(map(int,numbers.split()))
    max_n = max(result)
    min_n = min(result)
    
    return f"{max_n} {min_n}"
