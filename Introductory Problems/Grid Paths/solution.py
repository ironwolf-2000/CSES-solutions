import sys


n = 7
dirs = {"L": [(0, -1)], "R": [(0, 1)], "U": [(-1, 0)], "D": [(1, 0)], "?": [(0, -1), (0, 1), (-1, 0), (1, 0)]}


def dfs(r0, c0, i, visited):
    if i == len(path):
        return int(r0 == n - 1 and c0 == 0)

    if (r0, c0) in visited:
        return 0

    if r0 == n - 1 and c0 == 0:
        return 0

    if (r0 - 1, c0) not in visited and (r0 + 1, c0) not in visited and (r0, c0 - 1) in visited and (r0, c0 + 1) in visited:
        return 0

    if (r0 - 1, c0) in visited and (r0 + 1, c0) in visited and (r0, c0 - 1) not in visited and (r0, c0 + 1) not in visited:
        return 0

    for dr, dc in (-1, -1), (-1, 1), (1, -1), (1, 1):
        if (r0 + dr, c0 + dc) in visited and (r0 + dr, c0) not in visited and (r0, c0 + dc) not in visited:
            return 0

    visited.add((r0, c0))
    res = 0

    for dr, dc in dirs[path[i]]:
        r, c = r0 + dr, c0 + dc
        res += dfs(r, c, i + 1, visited)

    visited.remove((r0, c0))

    return res


path = sys.stdin.readline().rstrip()
visited = {(-1, -1), (n, -1), (-1, n), (n, n)}

for i in range(n):
    visited |= {(-1, i), (n, i), (i, -1), (i, n)}

print(dfs(0, 0, 0, visited))
