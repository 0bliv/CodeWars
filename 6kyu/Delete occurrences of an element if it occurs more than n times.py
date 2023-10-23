def delete_nth(order, max_e):
    result = []
    count = {}
    
    for num in order:
        if num not in count:
            count[num] = 1
            result.append(num)
        elif count[num] < max_e:
            count[num] += 1
            result.append(num)
    
    return result
