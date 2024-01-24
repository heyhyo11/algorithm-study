# 참고한 링크: https://jennnn.tistory.com/61

import sys
from collections import deque
 
input = sys.stdin.readline

def bfs(x,y):
    q.append((x,y))
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))

n = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(n)]
q = deque()

# 적록색약 아닌 경우
visited = [[0] * n for _ in range(n)]
ans1 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            ans1 += 1

# 'G'를 모두 'R'로 변경하기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

# 적록색약인 경우
visited = [[0] * n for _ in range(n)]
ans2 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            ans2 += 1

print(ans1, ans2)