from itertools import permutations
import sys


s = sys.stdin.readline().rstrip()
res = sorted("".join(perm) for perm in set(permutations(s)))

print(len(res))
print(*res, sep="\n")
