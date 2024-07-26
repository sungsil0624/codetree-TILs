import sys
from collections import deque

n = int(sys.stdin.readline().strip())

q = deque()

for _ in range(n):
    command = list(sys.stdin.readline().strip().split())

    if command[0] == "push":
        q.append(int(command[1]))
    elif command[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    else:
        if not q:
            print(-1)
        else:
            print(q[-1])