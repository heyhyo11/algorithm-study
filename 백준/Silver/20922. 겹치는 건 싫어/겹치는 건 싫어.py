import sys

input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
check = [0] * (max(nums) + 1)
start, end, ans = 0, 0, 0

while end < n:
    if check[nums[end]] < k:
        check[nums[end]] += 1
        end += 1
    else:
        check[nums[start]] -= 1
        start += 1
    ans = max(ans, end-start)

print(ans)