def find_the_duplicate(nums):
    sn = set()
    
    for numbs in nums:
        if numbs in sn:
            return numbs
        sn.add(numbs)