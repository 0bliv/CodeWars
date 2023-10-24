def remove_smallest(numbers):
    if not numbers:
        return []
    else:
        min_v = min(numbers)
        new_numbers = numbers[:]
        new_numbers.remove(min_v)
        return new_numbers
