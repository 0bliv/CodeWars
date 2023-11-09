def enough(cap, on, wait):
    resp = cap - on - wait
    if resp > 0:
        return 0
    else:
        return abs(resp)