import sys

# num = list(map(int, sys.stdin.readline().strip().split()))
#
# sol = 1
#
# num.sort()
#
# for i in range(2,-1,-1):
#     if i == 2:
#         sol = num[i]
#     else:
#         if num[i] % 2 == 1:
#             sol *= num[i]
#
# print(sol)

n = int(sys.stdin.readline().strip())

if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print(1)
else:
    print(0)