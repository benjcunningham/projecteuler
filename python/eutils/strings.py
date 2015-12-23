def is_palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

def map_vals(x, dval):
    return [dval[y] for y in list(x)]