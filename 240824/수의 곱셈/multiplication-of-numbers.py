import sys

num = list(map(int,sys.stdin.readline().strip().split()))

sol = 1

for i in num:
    if i % 2 == 1:
        sol *= i
if sol == 1:
    print(max(num))
else:
    print(sol)