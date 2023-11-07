import math

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n > 12:
        raise ValueError("Input is too large, maximum supported value is 12")
    
    return math.factorial(n)