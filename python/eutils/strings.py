def is_palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False