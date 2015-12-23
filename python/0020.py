# Problem 20
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of
# the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

import eutils.lists as lists
import eutils.vectorize as vec
import math
import time
start = time.time()

ans = vec.v_sum(lists.l_digits(math.factorial(100)))

end = time.time()
print("The answer to Problem 20 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))