import sys


def read_numbers():
    return map(int, sys.stdin.readline().split())


t = int(sys.stdin.readline())

for _ in range(t):
    r, c = read_numbers()

    if r > c:
        if r % 2 != 0:
            res = (r - 1) ** 2 + c
        else:
            res = r**2 - c + 1
    else:
        if c % 2 == 0:
            res = (c - 1) ** 2 + r
        else:
            res = c**2 - r + 1

    print(res)
