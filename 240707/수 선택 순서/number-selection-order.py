import sys
from collections import deque

n, x = map(int, sys.stdin.readline().strip().split())

nums = list(map(int, sys.stdin.readline().strip().split()))

q = deque()

for i in range(n):
    q.append((i, nums[i]))

sol = 0

while q:
    index, front = q.popleft()

    max_value = 0

    for num in q:
        max_value = max(max_value, num[1])

    if max_value > front:
        q.append((index, front))
        continue
    else:
        sol += 1
        if index == x:
            print(sol)
            break