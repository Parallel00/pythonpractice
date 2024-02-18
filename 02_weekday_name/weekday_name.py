def weekday_name(day_of_week):
    DAY = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY",]
    
    if day_of_week < 1 or day_of_week > 7:
        return None
    
    return DAY[day_of_week - 1]