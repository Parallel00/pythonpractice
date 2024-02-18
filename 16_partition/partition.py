def partition(lst, fn):
    list_of_truths = []
    list_of_falses = []
    
    for value in lst:
        if fn(value):
            list_of_truths.append(val)
        else:
            list_of_falses.append(val)
            
    return [list_of_truths, list_of_falses]