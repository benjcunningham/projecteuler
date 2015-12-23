# Problem 14
#
# The following iterative sequence is defined for the set of positive
# integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following
# sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz
# Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one
# million.

import time
start = time.time()

max = [13, 10]
disc = {13:10, 40:9, 20:8, 10:7, 5:6, 16:5, 8:4, 4:3, 2:2, 1:1}

for m in range(1, 1000000):

    chain = 0
    n = m

    while n != 1:
        if n in disc:
            chain += disc[n]
            n = 1
        else:
            chain += 1
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1

    disc[m] = chain
    if chain > max[1]:
        max = [m, chain]

ans = max[0]

end = time.time()
print("The answer to Problem 14 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))