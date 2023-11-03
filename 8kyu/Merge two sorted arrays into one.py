def merge_arrays(arr1, arr2):
    arr1.extend(arr2)
    resp = []
    for i in arr1:
        if i not in resp:
            resp.append(i)
    return sorted(resp)