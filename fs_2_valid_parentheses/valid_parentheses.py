def valid_parentheses(parens):
    count = 0
    
    for par in parens:
        if par == '(':
            count += 1
        elif par == ')':
            count -= 1
        
        if count < 0:
            return False
            
    
    return count == 0