from math import inf
import sys


n = int(sys.stdin.readline())
res = inf

for x0 in 2, 5:
    cur = 0
    x = x0

    while x <= n:
        cur += n // x
        x *= x0

    res = min(res, cur)

print(res)
