def flick_switch(lst):
    result = []
    switch = True  

    for item in lst:
        if item == 'flick':
            switch = not switch 
        result.append(switch)

    return result
