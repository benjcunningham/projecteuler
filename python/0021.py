# Problem 21
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less
# than n which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable
# pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
# 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284
# are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import eutils.factors as factors
import eutils.primes as primes
import eutils.vectorize as vec
import math
import time
start = time.time()

ans = 0
for a in range(1, 10000):
    if not (primes.is_prime(a)):
        b = vec.v_sum(factors.l_factors(a)[:-1])
        if (a != b) and (a == vec.v_sum(factors.l_factors(b)[:-1])):
            ans += a

end = time.time()
print("The answer to Problem 21 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))