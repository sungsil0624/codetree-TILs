import sys
from collections import deque


def bfs():
    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if map1[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[a][b] + 1
                    q.append((nx, ny))


def check():
    temp = True

    for i in range(n):
        for j in range(m):
            if map1[i][j] == 0 and visited[i][j] == 0:
                temp = False

    return temp


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().strip().split())

map1 = []

for _ in range(n):
    map1.append(list(map(int, sys.stdin.readline().strip().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if map1[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1

bfs()

if check():
    print(max(map(max, visited)) - 1)
else:
    print(-1)