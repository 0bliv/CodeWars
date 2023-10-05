def count_positives_sum_negatives(arr):
    
    if arr == [] or arr is None:
        return []  
    else: 
        negative = sum(x for x in arr if x < 0)
        positive = sum(1 for x in arr if x > 0)
        return [positive, negative]