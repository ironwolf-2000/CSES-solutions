import sys


def read_numbers():
    return map(int, sys.stdin.readline().split())


n = int(sys.stdin.readline())
A = list(read_numbers())
res = 0

for i in range(1, n):
    if A[i] < A[i - 1]:
        res += A[i - 1] - A[i]
        A[i] = A[i - 1]

print(res)
