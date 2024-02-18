def find_factors(num):
    fcto = []
    
    while(n <= num):
        if num % n == 0:
            fcto.append(n)
        n += 1
        
    return fcto