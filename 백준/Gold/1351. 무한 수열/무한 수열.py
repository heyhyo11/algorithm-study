# 풀이 참고
import sys

input = sys.stdin.readline

n, p, q = map(int, input().split())
arr = {}
arr[0] = 1

def dfs(n):
    if n in arr:
        return arr[n]
    else:
        arr[n] = dfs(n//p) + dfs(n//q)
        return arr[n]

print(dfs(n))