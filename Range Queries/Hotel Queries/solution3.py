from math import ceil, log2
import sys


def read_numbers():
    return map(int, sys.stdin.readline().split())


class SegmentTree:
    def __init__(self, n: int) -> None:
        self.n = 2 ** ceil(log2(n))
        self.tree = [0] * (self.n * 2)

        for k, x in enumerate(read_numbers()):
            self.set(k, x)

    def set(self, k: int, x: int) -> None:
        k += self.n

        self.tree[k] = x
        k //= 2

        while k >= 1:
            self.tree[k] = max(self.tree[k * 2], self.tree[k * 2 + 1])
            k //= 2

    def first_available_index(self, value: int) -> int:
        if self.tree[1] < value:
            return 0

        k = 1

        while k * 2 < len(self.tree):
            if value <= self.tree[k * 2]:
                k = k * 2
            else:
                k = k * 2 + 1

        self.set(k - self.n, self.tree[k] - value)

        return k - self.n + 1


n, m = read_numbers()
tree = SegmentTree(n)

for value in read_numbers():
    print(tree.first_available_index(value), end=" ")
