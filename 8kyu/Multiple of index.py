def multiple_of_index(arr):
    resp = []
    if arr[0] == 0:
            resp.append(0)
    for i in range(1,len(arr)):
        if arr[i] % i == 0:
            resp.append(arr[i])
    return resp