import math

def solution(a):
    common_divisor = a[0]
    for element in a[1:]:
        common_divisor = math.gcd(common_divisor, element)
    return len(a) * common_divisor
