geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    resp = []
    for i in birds:
        if i not in geese:
            resp.append(i)
    return resp