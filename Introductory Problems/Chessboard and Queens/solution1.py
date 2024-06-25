import sys


n = 8


def readline():
    return sys.stdin.readline().rstrip()


def backtrack(queens, r):
    if r == n:
        return 1

    res = 0

    for c in range(n):
        if M[r][c] == "." and all(c != c0 and r - c != r0 - c0 and r + c != r0 + c0 for r0, c0 in queens):
            queens.append((r, c))
            res += backtrack(queens, r + 1)
            queens.pop()

    return res


M = [readline() for _ in range(n)]
print(backtrack([], 0))
