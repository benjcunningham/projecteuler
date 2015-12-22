import math

def l_factors(x):

    [ll, lh] = [[], []]

    for f in range(1, int(math.sqrt(x)) + 1):
        if x % f == 0:
            ll.append(f)
            fp = x / f
            if fp != f:
                lh.append(int(fp))

    return ll + list(reversed(lh))