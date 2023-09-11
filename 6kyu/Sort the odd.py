def sort_array(arr):
    odd_nums = sorted((x for x in arr if x % 2), reverse=False)
    return [odd_nums.pop(0) if x % 2 else x for x in arr]
