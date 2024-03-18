import sys

input = sys.stdin.readline
n = int(input())
ans = []
k = 2

for i in range(n):
    ans.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(k):
        if j == 0:
            ans[i][j] = ans[i][j] + ans[i-1][j]
        elif i == j:
            ans[i][j] = ans[i][j] + ans[i-1][j-1]
        else:
            ans[i][j] = max(ans[i-1][j-1], ans[i-1][j]) + ans[i][j]
    k += 1
    
print(max(ans[n-1]))