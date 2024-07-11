import sys
from collections import deque

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

q = deque((num, i) for i, num in enumerate(nums))

sol = []

current_pos = 0

while q:
    num, idx = q[current_pos]
    sol.append(num)
    q.remove((num, idx))

    if not q:
        break

    if num > 0:
        current_pos = (current_pos + (num - 1)) % len(q)
    else:
        current_pos = (current_pos + num) % len(q)

for i in sol:
    print(i, end=" ")