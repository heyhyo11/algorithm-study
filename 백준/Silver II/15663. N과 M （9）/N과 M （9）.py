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
        if check != arr[i] and visited[i] == 0:
            ans.append(arr[i])
            visited[i] = 1
            check = arr[i]
            dfs()
            ans.pop()
            visited[i] = 0

dfs()