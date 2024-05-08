import sys

input = sys.stdin.readline

n = int(input())
velocity = list(map(int, input().split()))
limit_velocity = 1
ans = limit_velocity

for i in range(n-1):
    limit_velocity = min([velocity[-i-2], limit_velocity+1])
    ans += limit_velocity

print(ans)