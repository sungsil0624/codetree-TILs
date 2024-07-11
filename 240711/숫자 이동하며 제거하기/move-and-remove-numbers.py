import sys
from collections import deque

n = int(sys.stdin.readline().strip())

nums = list(map(int, sys.stdin.readline().strip().split()))

q = deque(nums)

sol = []

while q:

    x = q.popleft()



    if x > 0:
        q.rotate(-(x-1))
    elif x == -1:
        q.rotate(-1)
    else:
        q.rotate(x)

    sol.append(x)

for i in sol:
    print(i, end=" ")