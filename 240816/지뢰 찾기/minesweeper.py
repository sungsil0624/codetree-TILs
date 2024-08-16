import sys

n = int(sys.stdin.readline().strip())

map1 = []
map2 = []

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(n):
    map1.append(list(sys.stdin.readline().strip()))

for _ in range(n):
    map2.append(list(sys.stdin.readline().strip()))

for i in range(n):
    for j in range(n):
        if map2[i][j] == "x":
            cnt = 0

            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < n and 0 <= ny < n:
                    if map1[nx][ny] == "*":
                        cnt += 1

            map2[i][j] = cnt

for i in map2:
    for j in i:
        print(j,end = "")
    print()