from collections import Counter
import sys


def backtrack(count, cur):
    if len(cur) == len(s):
        return [cur]

    res = []

    for ch in count:
        if count[ch]:
            count[ch] -= 1
            res += backtrack(count, cur + ch)
            count[ch] += 1

    return res


s = sys.stdin.readline().rstrip()
res = sorted(backtrack(Counter(s), ""))

print(len(res))
print(*res, sep="\n")
