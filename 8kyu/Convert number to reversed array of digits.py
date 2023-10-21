def digitize(n):
    string = str(n)[::-1]
    resp = [int(char) for char in string]
    return resp