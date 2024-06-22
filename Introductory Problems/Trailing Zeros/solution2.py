import sys


n = int(sys.stdin.readline())
res = 0
x = 5

while x <= n:
    res += n // x
    x *= 5

print(res)
