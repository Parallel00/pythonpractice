def two_list_dictionary(keys, values):
    output = {}
    
    for idx, val in enumerate(keys):
        output[val] = values[idx] if idx < len(values) else None
        
    return output