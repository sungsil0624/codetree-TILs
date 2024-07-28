import math
import sys


def is_prime(x):
    temp = True

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            temp = False

    return temp


sol = []

a, b = map(int, sys.stdin.readline().strip().split())

for i in range(a, b + 1):
    if i == 1:
        continue
    if is_prime(i):
        sol.append(i)

if not sol:
    print(-1)
else:
    print(sum(sol))
    print(min(sol))