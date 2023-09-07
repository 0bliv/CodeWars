def is_triangle(a, b, c):
    return all(x > 0 for x in (a, b, c)) and a < b + c and b < a + c and c < a + b
