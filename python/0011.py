# Problem 11
#
# In the 20×20 grid below, four numbers along a diagonal line have been
# marked in red.
#
# [See 0011.txt]
#
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
#
# What is the greatest product of four adjacent numbers in the same
# direction (up, down, left, right, or diagonally) in the 20×20 grid?

import eutils.vectorize as vec
import time
start = time.time()

f = open('../data/0011.txt', 'r')

mat = []
for line in f:
    mat.append([int(x) for x in line.split(" ")])

f.close()

ans = 0

# Horizontal
for r in range(0, len(mat)):
    for c in range(0, len(mat[0]) - 3):
        prod = vec.v_prod(mat[r][c:c + 4])
        if prod > ans:
            ans = prod

# Vertical
for r in range(0, len(mat) - 3):
    for c in range(0, len(mat[0])):
        prod = vec.v_prod([x[c] for x in mat[r:r + 4]])
        if prod > ans:
            ans = prod

# Diagonal Down
for r in range(0, len(mat) - 3):
    for c in range(0, len(mat[0]) - 3):
        prod = vec.v_prod([mat[r + x][c + x] for x in range(0, 4)])
        if prod > ans:
            ans = prod

# Diagonal Up
for r in range(3, len(mat)):
    for c in range(0, len(mat[0]) - 3):
        prod = vec.v_prod([mat[r - x][c + x] for x in range(0, 4)])
        if prod > ans:
            ans = prod

end = time.time()
print("The answer to Problem 11 is: %s" % ans)
print("<< Returned in %s seconds >>" % (end - start))