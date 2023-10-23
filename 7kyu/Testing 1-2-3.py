def number(lines):
    numbered_lines = [f"{i+1}: {line}" for i, line in enumerate(lines, start=0)]
    return numbered_lines
    
    