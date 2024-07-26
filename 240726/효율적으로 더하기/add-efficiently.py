import sys

n = int(sys.stdin.readline().strip())

nums = list(map(int,sys.stdin.readline().strip().split()))

nums.sort()

num_sum = 0

for i in range(1,n+1):
    num_sum += sum(nums[:i])

print(num_sum)