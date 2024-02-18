def multiply_even_numbers(nums):
    prd = 1
    
    for number in nums:
        if number % 2 == 0:
            prd = prd * number
    
    return prd