import sys


def read_numbers():
    return map(int, sys.stdin.readline().split())


n = int(sys.stdin.readline())
A = list(read_numbers())

total = sum(A)
res = total

for mask in range(1 << n):
    cur = 0

    for i in range(n):
        if mask & 1 << i:
            cur += A[i]

    res = min(res, abs(cur - (total - cur)))

print(res)
