import sys


def findKthDigit(k):
    t, i = 9, 1
    while k - t * i > 0:
        k -= t * i
        t *= 10
        i += 1

    res = 0
    b = 10 ** (i - 1)
    d = 1

    while b:
        while k - b * i > 0:
            k -= b * i
            d += 1

        res = res * 10 + d
        b //= 10
        d = 0

    return int(str(res)[k - 1])


q = int(sys.stdin.readline())

for _ in range(q):
    k = int(sys.stdin.readline())
    print(findKthDigit(k))
