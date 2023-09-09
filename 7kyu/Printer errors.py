def printer_error(s):
    count = 0
    for i in range(len(s)):
        if s[i] > 'm':
            count+=1
    return str(count)+"/"+str(len(s))