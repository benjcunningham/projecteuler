# Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import eutils.primes as primes
import time
start = time.time()

count = 1
n = 3
while count < 10001:
    if primes.is_prime(n):
        ans = n
        count += 1
    n += 2

end = time.time()
print("The answer to Problem 7 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))