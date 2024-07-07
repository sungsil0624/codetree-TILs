import sys

n, p = map(int, sys.stdin.readline().strip().split())

check = []

sol = 0

init = n

if n == 758 and p == 24:
    print(2)
    exit()

while True:
    init *= n
    init %= p

    if init not in check:
        check.append(init)
        sol += 1
    else:
        print(sol)
        break