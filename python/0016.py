# Problem 16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

import eutils.vectorize as vec
import time
start = time.time()

ans = vec.v_sum([int(x) for x in list(str(2 ** 1000))])

end = time.time()
print("The answer to Problem 16 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))