def list_check(lst):
    for it in lst:
        if not isinstance(it, list):
            return False
    
    return True
