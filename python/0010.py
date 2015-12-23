# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import eutils.primes as primes
import time
start = time.time()

ans = 2
for n in range(3, 2000000, 2):
    if primes.is_prime(n):
        ans += n

end = time.time()
print("The answer to Problem 10 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))