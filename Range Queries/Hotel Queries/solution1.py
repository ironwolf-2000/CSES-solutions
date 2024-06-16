from math import ceil, log2
import sys


def read_numbers():
    return map(int, sys.stdin.readline().split())


class SegmentTree:
    def __init__(self, A: "list[int]") -> None:
        self.n = 2 ** ceil(log2(len(A)))
        self.tree = [{"index": 0, "value": 0} for _ in range(self.n * 2)]

        for k, x in enumerate(A):
            self.set(k, x)

    def set(self, k: int, x: int) -> None:
        k += self.n

        self.tree[k] = {"index": k - self.n + 1, "value": x}
        k //= 2

        while k >= 1:
            if self.tree[k * 2]["value"] >= self.tree[k * 2 + 1]["value"]:
                self.tree[k] = self.tree[k * 2]
            else:
                self.tree[k] = self.tree[k * 2 + 1]

            k //= 2

    def first_available_index(self, value: int) -> int:
        if self.tree[1]["value"] < value:
            return 0

        k = 1

        while k * 2 < len(self.tree):
            if value <= self.tree[k * 2]["value"]:
                k = k * 2
            else:
                k = k * 2 + 1

        self.set(k - self.n, self.tree[k]["value"] - value)

        return self.tree[k]["index"]


n, m = read_numbers()
hotels = list(read_numbers())

tree = SegmentTree(hotels)

for value in read_numbers():
    print(tree.first_available_index(value), end=" ")
