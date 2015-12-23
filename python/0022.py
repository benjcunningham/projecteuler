# Problem 22
#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text
# file containing over five-thousand first names, begin by sorting it
# into alphabetical order. Then working out the alphabetical value for
# each name, multiply this value by its alphabetical position in the
# list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN,
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
# list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

import eutils.strings as strings
import eutils.vectorize as vec
import re
import time
start = time.time()

val = dict(zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), list(range(1, 27))))

f = open('../data/names.txt', 'r')

n = ""
for line in f:
    n += line.rstrip()
f.close()

names = [re.sub("[^A-Z]", "", x) for x in n.split(',')]
names.sort()

ans = vec.v_sum([vec.v_sum(strings.map_vals(x, val)) * (i + 1)
                 for i, x in enumerate(names)])

end = time.time()
print("The answer to Problem 22 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))