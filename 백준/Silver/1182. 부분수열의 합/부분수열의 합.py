import sys

input = sys.stdin.readline

n, s = map(int, input().split())
num_list = list(map(int, input().split()))
ans = []
cnt = 0

def dfs(x):
    global cnt
    if sum(ans) == s and len(ans) > 0:
        cnt += 1
  
    for i in range(x, n):
        ans.append(num_list[i])
        dfs(i+1)
        ans.pop()

dfs(0)
print(cnt)