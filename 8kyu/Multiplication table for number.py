def multi_table(number):
    table = []
    for i in range(1, 11):
        result = i * number
        table.append(f"{i} * {number} = {result}")
    return '\n'.join(table)