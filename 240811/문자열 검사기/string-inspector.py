import sys
from collections import deque

q = deque()

input_str = sys.stdin.readline().strip()

for i in input_str:
    if i == "(":
        q.append(i)
    elif q and i == ")" and q[-1] == "(":\
        q.pop()
    elif i == "[":
        q.append(i)
    elif q and q[-1] == "[":
        q.pop()

if not q:
    print(1)
else:
    print(0)