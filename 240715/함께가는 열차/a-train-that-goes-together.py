import sys

n = int(sys.stdin.readline().strip())

sol = 1

train = []

temp = 0

for _ in range(n):
    train.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(n - 1, -1, -1):
    if i == n-1:
        temp = train[i][1]
        continue

    if train[i][1] <= temp:
        temp = train[i][1]
        sol += 1

print(sol)