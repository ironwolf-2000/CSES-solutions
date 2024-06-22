import sys


n = int(sys.stdin.readline())


def fast_pow(x, n, m):
    res = 1

    while n:
        if n % 2:
            res = res * x % m
            n -= 1
        else:
            x = x * x % m
            n //= 2

    return res


print(fast_pow(2, n, 10**9 + 7))
