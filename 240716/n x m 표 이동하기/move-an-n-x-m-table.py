import sys

n, m = map(int, sys.stdin.readline().strip().split())

map1 = []

for _ in range(n):
    map1.append(list(map(int, sys.stdin.readline().strip().split())))

dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = map1[i][j]
        elif i == 0 and j != 0:
            dp[i][j] = dp[i][j-1] + map1[i][j]
        elif i != 0 and j == 0:
            dp[i][j] = dp[i-1][j] + map1[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + map1[i][j]

print(dp[-1][-1])