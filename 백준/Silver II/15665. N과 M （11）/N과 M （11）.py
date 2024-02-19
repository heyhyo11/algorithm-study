import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0] * n
ans = []

def dfs():
    check = 0
    if len(ans) == m:
        print(*ans)
        return

    for i in range(n):
        if check != arr[i]:
            ans.append(arr[i])
            check = arr[i]
            dfs()
            ans.pop()

dfs()