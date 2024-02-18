def flip_case(phrase, to_swap):
    to_swap = to_swap.lower()
    
    fx = [
        (char.swapcase() if char.lower() == to_swap else char)
        for char in phrase
    ]
    
    return "".join(fx)
