import sys


n = int(sys.stdin.readline())


def fast_pow(x, n, m):
    if n == 0:
        return 1

    if n % 2:
        return x * fast_pow(x, n - 1, m) % m

    return fast_pow(x * x % m, n // 2, m) % m


print(fast_pow(2, n, 10**9 + 7))
