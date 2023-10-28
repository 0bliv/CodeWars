def bmi(weight, height):
    # Calculate BMI
    bmi_value = weight / (height ** 2)
    
    # Define BMI categories and their ranges
    bmi_categories = {
        (0, 18.5): "Underweight",
        (18.5, 25.0): "Normal",
        (25.0, 30.0): "Overweight",
        (30.0, float('inf')): "Obese"
    }

    # Determine the BMI category
    for (lower, upper), category in bmi_categories.items():
        if lower <= bmi_value < upper:
            return category