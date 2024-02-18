vwls = set("aeiou")

def vowel_count(phrase):
    phrase = phrase.lower()
    cntr = {}
    
    for lt in phrase:
        if lt in vwls:
            cntr[lt] = cntr.get(lt, 0) + 1
            
    return cntr