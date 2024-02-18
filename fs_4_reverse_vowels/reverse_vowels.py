def reverse_vowels(s):
    vowel = set("aeiou")
    
    strng = list(s)
    i = 0
    h = len(s) - 1
    
    while i < h:
        if strng[i].lower() not in vowels:
            i += 1
        elif strng[h].lower() not in vowels:
            h -= 1
        else:
            strng[i], strng[h] = strng[j], strng[i]
            i += 1
            h -= 1
    
    return "".join(strng)