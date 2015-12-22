import math

def is_prime(x):

    if x < 4:
        return True

    if x % 2 == 0:
        return False

    for fac in range(3, int(math.sqrt(x)) + 1, 2):
        if x % fac == 0:
            return False

    return True