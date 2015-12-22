# Problem 8
#
# The four adjacent digits in the 1000-digit number that have the
# greatest product are 9 × 9 × 8 × 9 = 5832.
#
# [See 0008.txt]
#
# Find the thirteen adjacent digits in the 1000-digit number that have
# the greatest product. What is the value of this product?

import functools
import operator
import time
start = time.time()

f = open('../data/0008.txt', 'r')

n = ""
for line in f:
    n += line.rstrip()
f.close()

adj = 13
ans = 0
n = [int(x) for x in list(n)]
for i in range(0, len(n) - adj):
    prod = functools.reduce(operator.mul, n[i:i + adj])
    if prod > ans:
        ans = prod

end = time.time()
print("The answer to Problem 8 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))