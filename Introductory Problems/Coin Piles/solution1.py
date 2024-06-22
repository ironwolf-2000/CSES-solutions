import sys


def read_numbers():
    return map(int, sys.stdin.readline().split())


t = int(sys.stdin.readline())

for _ in range(t):
    a, b = read_numbers()

    # 2x + y = a
    # x + 2y = b

    x = (2 * a - b) / 3
    y = (2 * b - a) / 3

    if x >= 0 and y >= 0 and x == int(x) and y == int(y):
        print("YES")
    else:
        print("NO")
