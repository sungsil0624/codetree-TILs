import sys

n = int(sys.stdin.readline().strip())

dict1 = {}

for _ in range(n):
    combi = list(sys.stdin.readline().strip().split())
    combi.sort()

    new_combi = ""

    for i in combi:
        new_combi += i

    if new_combi not in dict1.keys():
        dict1[new_combi] = 1
    else:
        dict1[new_combi] += 1

print(max(dict1.values()))