# Problem 50
#
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime
# below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to
# a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

import eutils.primes as primes
import eutils.vectorize as vec
import time
start = time.time()

ceil = 1000000

p = [2] + [n for n in list(range(3, ceil, 2)) if primes.is_prime(n)]

max = [0, 0]
for i in range(0, len(p)):
    j = i + 1 + max[1]
    ssum = vec.v_sum(p[i:j])
    while j <= len(p) and ssum < ceil:
        if primes.is_prime(ssum):
            max = [ssum, len(p[i:j])]
        j += 1
        ssum = vec.v_sum(p[i:j])

ans = max[0]

end = time.time()
print("The answer to Problem 50 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))