import sys

n = int(sys.stdin.readline().strip())

nums = list(map(int, sys.stdin.readline().strip().split()))

nums.sort()

sol = 0

while len(nums) > 1:
    a = nums.pop()
    b = nums.pop()

    a += b / 2

    nums.append(a)

print(round(nums[0],1))