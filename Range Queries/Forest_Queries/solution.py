import sys


def read_numbers():
    return map(int, sys.stdin.readline().split())


def readline():
    return sys.stdin.readline().rstrip()


n, q = read_numbers()
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j, ch in enumerate(readline(), 1):
        dp[i][j] = 1 if ch == "*" else 0
        dp[i][j] += dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

for _ in range(q):
    r1, c1, r2, c2 = read_numbers()
    print(dp[r2][c2] - dp[r1 - 1][c2] - dp[r2][c1 - 1] + dp[r1 - 1][c1 - 1])
