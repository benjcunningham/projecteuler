# Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?

import eutils.factors as factors
import eutils.primes as primes
import time
start = time.time()

ans = None
fac = factors.l_factors(600851475143)

i = len(fac) - 2
while ans is None:
    if primes.is_prime(fac[i]):
        ans = fac[i]
    i -= 1

end = time.time()
print("The answer to Problem 3 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))