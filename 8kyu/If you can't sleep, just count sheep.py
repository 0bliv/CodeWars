def count_sheep(n):
    resp = ""
    if n == 0:
        return resp
    else:
        resp = "".join(f"{i} sheep..."for i in range(1,n+1))
        return resp