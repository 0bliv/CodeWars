def series_sum(n):
    sum = 0
    denominator = 1
    
    for _ in range(n):
        sum += 1 / denominator
        denominator += 3
    
    return "{:.2f}".format(sum)
