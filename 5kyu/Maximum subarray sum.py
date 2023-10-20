def max_sequence(arr):
    if not arr:
        return 0
    c_max = g_max = arr[0]
    for i in arr[1:]:
        c_max = max(i,c_max + i)
        g_max = max(c_max,g_max)
    
    if g_max < 0:
        return 0
    else:
        return g_max
        
