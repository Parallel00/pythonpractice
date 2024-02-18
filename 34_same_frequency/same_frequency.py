def fr_cn(cl):
    cts = {}
    
    for i in cl:
        cts[i] = cts.get(i, 0) + 1
        
    return cts

def same_frequency(num1, num2):
   return fr_cn(str(num1)) == fr_cn(str(num2))