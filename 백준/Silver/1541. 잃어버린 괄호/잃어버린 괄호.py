import sys

input = sys.stdin.readline
mark = input().strip().split('-')
nums = []


for i in mark:
    cnt = 0
    plus = list(map(int, i.split('+')))
    cnt += sum(plus)
    nums.append(cnt)

num = nums[0]

for i in range(1, len(nums)):
    num -= nums[i]

print(num)