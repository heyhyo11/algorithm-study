import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
distance = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
answer = []

# 그래프 입력
while True:
    s, e = map(int, input().split())
    
    if s == -1 and e == -1: # 탈출
        break

    distance[s][e] = 1
    distance[e][s] = 1


# 인접 행렬 초기화
for i in range(1, n+1):
    distance[i][i] = 0


# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1, n+1):
    answer.append(max(distance[i][1:]))

# 점수, 후보 수 출력
minval = min(answer)
print(minval, answer.count(minval))

# 모든 후보 출력
for i in range(n):
    if answer[i] == minval:
        print(i+1, end=' ')