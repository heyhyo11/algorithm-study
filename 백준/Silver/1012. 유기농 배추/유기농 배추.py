import sys
from collections import deque

sys.setrecursionlimit(10**7) 
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
 
def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
 
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))


t = int(input().rstrip()) # 테스트 케이스 개수
for _ in range(t):
    m, n, k = map(int, input().rstrip().split()) # m: 가로, n: 세로, k: 위치 개수
    graph = [[0]*m for _ in range(n)] # 주어진 배추밭

    for i in range(k): # 배추밭 생성
        x, y = map(int, input().rstrip().split())
        graph[y][x] = 1

    cnt = 0 # 연결요소 개수
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1 # bfs 끝날 때마다 +1

    print(cnt)