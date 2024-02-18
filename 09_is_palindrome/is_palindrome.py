def is_palindrome(phrase):
    nrmiz = phrase.lower().replace(' ', '')
    return nrmiz == nrmiz[::-1]
