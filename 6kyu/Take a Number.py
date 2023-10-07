def sum_dig_pow(a, b):
    result = []
    for num in range(a, b + 1):
        # Convert the number to a string to access individual digits
        digits = [int(digit) for digit in str(num)]
        
        # Calculate the sum of digits raised to their own powers
        digit_power_sum = sum(digit ** (index + 1) for index, digit in enumerate(digits))
        
        # Check if the sum is equal to the original number
        if digit_power_sum == num:
            result.append(num)
    
    return result