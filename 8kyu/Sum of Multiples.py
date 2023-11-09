def sum_mul(n, m):
    resp = 0
    if m <= 0 or n <= 0:
        return 'INVALID'
    else:
        for i in range(1,m):
            if i % n == 0:
                resp+=i
    return resp