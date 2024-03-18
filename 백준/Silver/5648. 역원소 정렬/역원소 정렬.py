import sys

arr = sys.stdin.readlines()
ans = []

for nums in arr:
    for num in nums.split():
        ans.append(int(num[::-1]))
        
ans = ans[1:]
ans.sort()
print("\n".join(map(str, ans)))