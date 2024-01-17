import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(a, b, h):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and graph[nx][ny]>h:
                queue.append((nx, ny))
                visited[nx][ny] = 1

n = int(input().rstrip())
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip().split())))

ans = [] # 연결요소 개수
for h in range(100):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] > h:
                bfs(i, j ,h)
                cnt += 1
    ans.append(cnt)

print(max(ans))