import sys

n, m, k = map(int, sys.stdin.readline().strip().split())

for _ in range(n):
    map1 = sys.stdin.readline().strip()

    for a in range(k):
        for i in map1:
            for j in range(k):
                print(i, end="")
        print()