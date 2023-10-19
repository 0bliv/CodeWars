def shortcut( s ):
    remove = "aeiou"
    resp = ''.join([i for i in s if i not in remove])
    return resp
