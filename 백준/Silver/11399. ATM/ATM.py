import sys

input = sys.stdin.readline
n = int(input())
nums = sorted(map(int, input().split()))
ans = 0

for num in nums:
  ans += num * n
  n -= 1
  
print(ans)