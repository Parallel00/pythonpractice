def find_greater_numbers(nums):
    count = 0
    
    for r in range(len(nums)):
        for s in range(r + 1, len(nums)):
            if nums[s] > nums[r]:
                count += 1
               

    return count