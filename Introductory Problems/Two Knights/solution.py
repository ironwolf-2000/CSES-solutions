import sys


n = int(sys.stdin.readline())

for k in range(1, n + 1):
    s = k * k
    res = s * (s - 1) // 2 - (k - 1) * (k - 2) * 4

    print(res)
