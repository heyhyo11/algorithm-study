import sys

input = sys.stdin.readline
n, m = map(int, input().split())

ans = [i for i in range(1, n+1)]

for i in range(m):
    a, b = map(int, input().split())
    temp = ans[a-1:b]
    temp.reverse()
    ans[a-1:b] = temp

print(*ans)