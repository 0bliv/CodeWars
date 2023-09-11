def sum_array(arr):
    if not arr or len(arr) == 1:
        return 0
    else:
        a = min(arr)
        b = max(arr)
        result = sum(arr) - b - a
        return result
