
def is_palindrome(str1):
    str1 = str1.lower()
    return str1 == str1[::-1]

def is_alpha(str1):
    return str1.isalpha()