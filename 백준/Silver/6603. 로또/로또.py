import sys

input = sys.stdin.readline

def dfs(x):
    if len(ans) == 6:
        print(*ans)
        return
  
    for i in range(x, k):
        if s[i] not in ans:
            ans.append(s[i])
            dfs(i)
            ans.pop()

while True:
    num_list = list(map(int, input().split()))
    k = num_list[0]
    s = num_list[1:]
    
    if k == 0:
        break
    
    ans = []
    dfs(0)
    print()