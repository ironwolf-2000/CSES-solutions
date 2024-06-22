import sys


def backtrack(available, cur):
    if len(cur) == len(s):
        return [cur]

    res = []

    for i in range(len(available)):
        if i == 0 or available[i] != available[i - 1]:
            res += backtrack(available[:i] + available[i + 1 :], cur + available[i])

    return res


s = sys.stdin.readline().rstrip()
res = backtrack(sorted(s), "")

print(len(res))
print(*res, sep="\n")
