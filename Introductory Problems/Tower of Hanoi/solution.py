import sys


def hanoi(k, stack1, stack3):
    if k == 0:
        return

    stack2 = 6 - stack1 - stack3

    hanoi(k - 1, stack1, stack2)
    print(stack1, stack3)
    hanoi(k - 1, stack2, stack3)


n = int(sys.stdin.readline())

# Number of moves:
# f(n) = 2f(n - 1) + 1 = 2 * (2 * (f(n - 2) + 1) + 1 = 2^2 * f(n - 2) + 2^2 - 1
# ...
# f(n) = 2^n * f(0) + 2^n - 1 = 2^n - 1

print(2**n - 1)
hanoi(n, 1, 3)
