import sys
n, m = map(int, input().split())
distance = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]
answer = []

for i in range(1, n+1):
    distance[i][i] = 0

for i in range(m):
    s, e = map(int, input().split())
    distance[s][e] = 1
    distance[e][s] = 1

# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        if distance[i][j] == sys.maxsize:
            continue
        else:
            temp += distance[i][j]
    answer.append(temp)

print(answer.index(min(answer)) + 1)