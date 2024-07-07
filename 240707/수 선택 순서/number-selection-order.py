import sys
from collections import deque

n, x = map(int, sys.stdin.readline().strip().split())

nums = list(map(int, sys.stdin.readline().strip().split()))

q = deque(nums)

sol = 0

while q:
    front = q.popleft()

    max_value = max(q)

    if max_value > front:
        q.append(front)
        continue
    else:
        sol += 1
        if front == nums[x]:
            print(sol)
            break