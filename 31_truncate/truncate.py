def truncate(phrase, n):
    if n < 3:
        return "Must be longer than 3 letters"
    
    if n > len(phrase) + 2:
        return phrase
        
    return phrase[:n - 3] + "..."