# 참고 링크: https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-4179-%EB%B6%88-BFS

import sys
from collections import deque
 
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 'IMPOSSIBLE'


# R x C 미로 크기 입력, 지훈 초기 위치 찾기
for i in range(r):
    graph.append(list(input().rstrip()))
    if 'J' in graph[i]:
        q = deque([(0, i, graph[i].index('J'))])
        

# 불 초기 위치 찾기
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            q.append((-1, i, j))


while q:
    time, x, y = q.popleft()

    # 지훈 탈출
    if time > -1 and graph[x][y] != 'F' and (x==0 or y==0 or x==r-1 or y==c-1):
        ans = time + 1
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<r and 0<=ny<c and graph[nx][ny] != '#':

            # 지훈 이동
            if time > -1 and graph[nx][ny] == '.':
                graph[nx][ny] = '_'
                q.append((time+1, nx, ny))

            # 불 이동
            elif time == -1 and graph[nx][ny] != 'F':
                graph[nx][ny] = 'F'
                q.append((-1, nx, ny))

print(ans)