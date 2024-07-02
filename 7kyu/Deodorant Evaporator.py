def evaporator(content, evap_per_day, threshold):
    threshold_content = content * (threshold / 100)
    days = 0
    
    while content >= threshold_content:
        content -= content * (evap_per_day / 100)
        days += 1
    
    return days
