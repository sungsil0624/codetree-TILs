import sys
from collections import deque

q = deque()

input_str = sys.stdin.readline().strip()

check = True

for i in input_str:
    if i == "(" or i == "[":
        q.append(i)
    elif i == ")" or i == "]":
        if not q:
            check = False
            break
        x = q.pop()
        if i == ")" and not x == "(":
            check = False
            break
        if i == "]" and not x == "[":
            check = False
            break

if not q and check:
    print(1)
else:
    print(0)