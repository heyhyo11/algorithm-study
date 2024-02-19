import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []


def dfs():
    if len(ans) == m:
        print(*ans)
        return

    for i in range(n):
        ans.append(arr[i])
        dfs()
        ans.pop()

dfs()