# Problem 42
#
# The nth term of the sequence of triangle numbers is given by, tn = 1/2
# n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the
# word value is a triangle number then we shall call the word a triangle
# word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text
# file containing nearly two-thousand common English words, how many are
# triangle words?

import eutils.strings as strings
import eutils.vectorize as vec
import re
import time
start = time.time()

tri = dict(zip([int(0.5 * n * (n + 1)) for n in list(range(1, 25))],
                list(range(1, 25))))

val = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), list(range(1, 27))))

f = open('../data/words.txt', 'r')

n = ""
for line in f:
    n += line.rstrip()
f.close()

words = [re.sub("[^A-Z]", "", x) for x in n.split(",")]
wvals = [vec.v_sum(strings.map_vals(x, val)) for x in words]

ans = len([x for x in wvals if x in tri])

end = time.time()
print("The answer to Problem 42 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))