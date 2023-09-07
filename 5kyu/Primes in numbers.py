def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        count = 0
        while n % divisor == 0:
            n //= divisor
            count += 1
        if count > 0:
            if count == 1:
                factors.append(str(divisor))
            else:
                factors.append(f"{divisor}**{count}")
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                factors.append(str(n))
            break

    return "(" + ")(".join(factors) + ")"

n = 86240
result = prime_factors(n)
print(result)
