import sys

times = list(sys.stdin.readline().strip().split())

times_trans = []

for time in times:
    total = 0
    x = time.split(":")

    total += int(x[0]) * 60
    total += int(x[1])

    times_trans.append(total)

n = int(sys.stdin.readline().strip())

sol = 0

dict1 = {}

for _ in range(n):
    command = sys.stdin.readline().strip().split()

    time_total = 0

    x = command[0].split(":")
    time_total += int(x[0]) * 60
    time_total += int(x[1])

    if command[1] not in dict1.keys():
        if time_total <= times_trans[0]:
            dict1[command[1]] = 1
    elif dict1[command[1]] == 1:
        if times_trans[1] <= time_total <= times_trans[2]:
            dict1[command[1]] = 2

for value in dict1.values():
    if value == 2:
        sol += 1

print(sol)