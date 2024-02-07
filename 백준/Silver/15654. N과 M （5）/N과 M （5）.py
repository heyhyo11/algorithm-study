import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
ans = []

def dfs(x):
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(len(num_list)):
        if num_list[i] not in ans:
            ans.append(num_list[i])
            dfs(num_list[i])
            ans.pop()

dfs(num_list[0])