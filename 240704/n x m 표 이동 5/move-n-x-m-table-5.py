import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and map1[nx][ny] == 1:
                    visited[nx][ny] = visited[a][b] + 1
                    q.append((nx, ny))


n, m = map(int, sys.stdin.readline().strip().split())

map1 = []

for _ in range(n):
    map1.append(list(map(int, sys.stdin.readline().strip().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]

bfs(0, 0)

print(visited[n - 1][m - 1])