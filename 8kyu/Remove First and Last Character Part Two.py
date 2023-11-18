def array(string):
    if string == "" or len(string) <= 2:
        return None
    else:
        string2 = string.split(",")
        resp = ' '.join(string2[1:-1])
        if resp == "":
            return None
        else:
            return resp