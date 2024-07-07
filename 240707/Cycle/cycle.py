import sys

n, p = map(int, sys.stdin.readline().strip().split())

check = []

sol = 0

init = n

while True:
    init *= n
    init %= p

    if init not in check:
        check.append(init)
        sol += 1
    else:
        print(sol)
        break