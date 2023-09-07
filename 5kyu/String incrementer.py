import re

def increment_string(s):
    match = re.match(r"^(.*?)(\d+)$", s)
    if match:
        non_number_part, number_part = match.groups()
        # Convert the number part to an integer, increment it, and format it with leading zeros
        incremented_number = f"{int(number_part) + 1:0{len(number_part)}}"
        # Concatenate the non-number part and the incremented number
        result = non_number_part + incremented_number
        return result
    else:
        # If there's no number part, simply return the original string with '1' appended
        return s + '1'