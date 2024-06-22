from collections import Counter
import sys


def solve(s):
    count = Counter(s)
    odd_char = ""
    res = []

    for ch in count:
        if count[ch] % 2:
            if odd_char:
                return "NO SOLUTION"

            odd_char = ch * count[ch]
        else:
            res.append(ch * (count[ch] // 2))

    return "".join(res) + odd_char + "".join(res[::-1])


s = sys.stdin.readline().rstrip()
print(solve(s))
