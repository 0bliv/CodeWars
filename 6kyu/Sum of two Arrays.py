def sum_arrays(array1, array2):
    if not array1 and not array2:
        return []

    # Convert the arrays to integers
    num1 = int(''.join(map(str, array1))) if array1 else 0
    num2 = int(''.join(map(str, array2))) if array2 else 0

    # Calculate the sum
    result = num1 + num2

    # Convert the result to a list of digits
    result_digits = [int(digit) for digit in str(abs(result))]

    # Handle the case where the result is negative
    if result < 0:
        result_digits[0] *= -1

    return result_digits
