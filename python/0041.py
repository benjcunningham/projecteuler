# Problem 41
#
# We shall say that an n-digit number is pandigital if it makes use of
# all the digits 1 to n exactly once. For example, 2143 is a 4-digit
# pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

import eutils.primes as primes
import eutils.strings as strings
import time
start = time.time()

m = 9
found = False
while not found:
    digits = list(range(m-1, 0, -1))
    perms = [int(str(m) + x) for x in
             strings.l_collapse(strings.l_permute(digits))]
    p = [x for x in perms if primes.is_prime(x)]
    if len(p):
        found = True
    m -= 1


ans = p[0]

end = time.time()
print("The answer to Problem 41 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))