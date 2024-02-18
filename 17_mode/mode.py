def mode(nums):
    count = []
    
    for number in nums:
        count[number] = count.get(number, 0) + 1
    
    max_value = max(count.values())
    
    for (number, freq) in count.items():
        if freq == max_value:
            return number
