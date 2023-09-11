import re

def solution(s):
    words = re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
    return words