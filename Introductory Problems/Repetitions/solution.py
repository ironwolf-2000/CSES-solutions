import sys


def readline():
    return sys.stdin.readline().rstrip()


s = readline()
cur, res = 1, 1

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        cur = 0

    cur += 1
    res = max(res, cur)

print(res)
