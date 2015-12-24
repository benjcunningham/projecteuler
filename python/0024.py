# Problem 24
#
# A permutation is an ordered arrangement of objects. For example, 3124
# is one possible permutation of the digits 1, 2, 3 and 4. If all of the
# permutations are listed numerically or alphabetically, we call it
# lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2,
# 3, 4, 5, 6, 7, 8 and 9?

import eutils.strings as strings
import time
start = time.time()

n = 1000000
digits = list('0123456789')

ans = int(strings.l_collapse([strings.l_permute(digits)[n - 1]])[0])

end = time.time()
print("The answer to Problem 24 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))