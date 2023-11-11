def remove(s):
    if s == "":
        return ""
    if s[-1] != "!":
        return s
    else:
        return s[:-1]
    