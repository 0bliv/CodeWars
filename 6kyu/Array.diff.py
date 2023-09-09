import numpy as np
def array_diff(a, b):
    #your code here
    x = np.array(a)
    y = np.array(b)
    result = np.setdiff1d(a,b,assume_unique = True)
    return result.tolist()