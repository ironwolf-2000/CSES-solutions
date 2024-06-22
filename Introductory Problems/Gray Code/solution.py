import sys


n = int(sys.stdin.readline())
res = ["0", "1"]

for _ in range(n - 1):
    res = ["0" + x for x in res[::-1]] + ["1" + x for x in res]

print(*res, sep="\n")
