import math
import sys


def is_prime(x):
    temp = True

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            temp = False

    return temp


sol = 0

n = int(sys.stdin.readline().strip())

for i in range(2,n+1):
    if is_prime(i):
        sol += 1

print(sol)