# Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?

import time
start = time.time()

check = [11, 13, 14, 16, 17, 18, 19, 20]

ans = 2520
while not (all(ans % f == 0 for f in check)):
    ans += 2

end = time.time()
print("The answer to Problem 5 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))