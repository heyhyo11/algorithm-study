import sys
from collections import deque
 
input = sys.stdin.readline
n = int(input().rstrip())
graph = []

# N x N 지도 크기 입력 
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
 
def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1
 
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count
 
apt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            apt.append(bfs(graph, i, j))
 
apt.sort()
print(len(apt))
print(*apt, sep='\n')