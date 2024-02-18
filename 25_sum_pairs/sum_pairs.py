def sum_pairs(nums, goal):
    visit_before = set()
    
    for numb in nums:
        difference = goal - numb
        
        if difference in visit_before:
            return (difference, numb)
        
        visit_before.add(numb)
    
    return ()