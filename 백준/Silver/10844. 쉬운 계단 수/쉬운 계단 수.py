# 풀이 참고

import sys

input = sys.stdin.readline
n = int(input())
dp = [[0]*12 for _ in range(n+1)] # 양 옆에 패딩
dp[1][2:11] = [1]*9 # 길이 1인 경우 모두 1임

# dp 테이블 돌면서 규칙 적용
for i in range(2, n+1):
    for j in range(1, 11):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

ans = sum(dp[n])
print(ans%1000000000)