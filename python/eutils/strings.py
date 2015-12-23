def is_palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

def map_vals(x, dval):
    return [dval[y] for y in list(x)]

def l_permute(x):
    if len(x) < 1:
        return [[]]
    else:
        return [[y] + p for y in x
                for p in l_permute([z for z in x if z != y])]