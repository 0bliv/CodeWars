def gimme(input_array):
    resp = sum(input_array) - max(input_array) - min(input_array)
    
    tolerance = 1e-10
    for i, x in enumerate(input_array):
        if abs(x - resp) < tolerance:
            return i
    

