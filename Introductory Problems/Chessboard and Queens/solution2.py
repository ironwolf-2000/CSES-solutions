import sys


n = 8


def readline():
    return sys.stdin.readline().rstrip()


def backtrack(r, col, diag1, diag2):
    if r == n:
        return 1

    res = 0

    for c in range(n):
        if M[r][c] == "." and c not in col and r + c not in diag1 and r - c not in diag2:
            col.add(c)
            diag1.add(r + c)
            diag2.add(r - c)

            res += backtrack(r + 1, col, diag1, diag2)

            col.remove(c)
            diag1.remove(r + c)
            diag2.remove(r - c)

    return res


M = [readline() for _ in range(n)]
print(backtrack(0, set(), set(), set()))
