# Problem 13
#
# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.
#
# [See 0013.txt]

import eutils.vectorize as vec
import time
start = time.time()

f = open('../data/0013.txt', 'r')
mat = [int(x) for x in f]
f.close()

ans = int(str(vec.v_sum(mat))[0:10])

end = time.time()
print("The answer to Problem 13 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))