# 풀이 참고

import sys

input = sys.stdin.readline
n = int(input())
ans = end = 0

# 정렬: (1) 끝나는 시간 기준으로 오름차순, (2) 시작하는 시간 기준으로 오름차순
time = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))

for s, e in time:
    if s >= end:
        ans += 1
        end = e

print(ans)