def is_odd_string(word):
    df = ord("a") - 1
    
    ttl = sum((ord (c) - df) for c in word.lower())
    
    return ttl % 2 == 1