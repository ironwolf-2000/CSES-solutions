import sys


def read_numbers():
    return map(int, sys.stdin.readline().split())


t = int(sys.stdin.readline())

for _ in range(t):
    a, b = read_numbers()

    if a > b:
        a, b = b, a

    if a * 2 >= b and (a + b) % 3 == 0:
        print("YES")
    else:
        print("NO")
