def fake_bin(x):
    return ''.join(['0' if int(char) < 5 else '1' for char in x])