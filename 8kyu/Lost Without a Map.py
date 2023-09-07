def sum_mix(arr):
    resp = [int(x) if isinstance(x, str) else x for x in arr]
    return sum(resp)