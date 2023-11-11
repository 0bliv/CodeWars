def square_digits(num):
    resp = ""
    x = 0
    for i in str(num):
        x = int(i)* int(i)
        resp+= str(x)
    return int(resp)
        
        