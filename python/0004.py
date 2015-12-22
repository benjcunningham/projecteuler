# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit
# numbers.

import eutils.strings as strings
import time
start = time.time()

digits = 3

ans = 0
for m in range(10 ** (digits - 1), 10 ** digits):
    for n in range(m, 10 ** digits):
        x = m * n
        if (x > ans) and (strings.is_palindrome(x)):
            ans = x

end = time.time()
print("The answer to Problem 4 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))