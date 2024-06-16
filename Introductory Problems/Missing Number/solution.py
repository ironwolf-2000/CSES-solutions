import sys


def read_numbers():
    return map(int, sys.stdin.readline().split())


n = int(sys.stdin.readline())
print((1 + n) * n // 2 - sum(read_numbers()))
