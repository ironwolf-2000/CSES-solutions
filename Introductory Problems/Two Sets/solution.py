import sys


n = int(sys.stdin.readline())
total = (1 + n) * n // 2

if total % 2:
    print("NO")
else:
    print("YES")

    target = total // 2
    s1, s2 = set(), set()
    cur = 0

    for x in range(n, 0, -1):
        if cur + x <= target:
            cur += x
            s1.add(x)
        else:
            s2.add(x)

    print(len(s1))
    print(*s1)
    print(len(s2))
    print(*s2)
