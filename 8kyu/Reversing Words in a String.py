def reverse(st):
    words = [word for word in st.split()if word]
    resp = " ".join(reversed(words))
    return resp