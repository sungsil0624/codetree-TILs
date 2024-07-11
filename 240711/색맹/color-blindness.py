import copy
import sys
from collections import deque


def bfs(x, y, visited, map_list):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and map_list[nx][ny] == map_list[a][b]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

n = int(sys.stdin.readline().strip())

map1 = []

for _ in range(n):
    map1.append(list(sys.stdin.readline().strip()))

visited1 = [[0 for _ in range(n)] for _ in range(n)]
visited2 = [[0 for _ in range(n)] for _ in range(n)]

map2 = copy.deepcopy(map1)

for i in range(n):
    for j in range(n):
        if map2[i][j] == 'R':
            map2[i][j] = 'G'

sol1 = 0
sol2 = 0

for i in range(n):
    for j in range(n):
        if visited1[i][j] == 0:
            bfs(i, j, visited1, map1)
            sol1 += 1

for i in range(n):
    for j in range(n):
        if visited2[i][j] == 0:
            bfs(i, j, visited2, map2)
            sol2 += 1

print(sol1, sol2)