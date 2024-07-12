import sys


def check_bingo():
    cnt = 0

    for i in range(5):
        if 0 not in visited[i]:
            cnt += 1

    for i in range(5):
        temp = True
        for j in range(5):
            if visited[j][i] == 0:
                temp = False
        if temp:
            cnt += 1

    check_cross1 = True

    for i in range(5):
        if visited[i][i] == 0:
            check_cross1 = False

    if check_cross1:
        cnt += 1

    check_cross2 = True

    for i in range(5):
        if visited[4 - i][i] == 0:
            check_cross2 = False
    if check_cross2:
        cnt += 1

    if cnt >= 3:
        return 1

    return 0


bingo = []

visited = [[0 for _ in range(5)] for _ in range(5)]

for _ in range(5):
    bingo.append(list(map(int, sys.stdin.readline().strip().split())))

num_list = list(map(int, sys.stdin.readline().strip().split()))
sol = 0

while True:

    number = num_list.pop(0)

    for i in range(5):
        for j in range(5):
            if number == bingo[i][j]:
                visited[i][j] = 1

    sol += 1

    if check_bingo():
        print(sol)
        exit()