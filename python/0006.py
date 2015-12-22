# Problem 6
#
# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

import time
start = time.time()

nn = 100

ssq = sum([n ** 2 for n in range(1, nn + 1)])
sqs = sum([n for n in range(1, nn + 1)]) ** 2

ans = sqs - ssq

end = time.time()
print("The answer to Problem 6 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))