import sys
from collections import deque
 
input = sys.stdin.readline

graph = []
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
ans = 0

n = int(input().rstrip())

for _ in range(n):
    I = int(input().rstrip())
    graph = [[0] * I for _ in range(I)]
    current_x, current_y = map(int, input().rstrip().split())
    goal_x, goal_y = map(int, input().rstrip().split())
    q = deque([(0, current_x, current_y)])

    while q:
        cnt, x, y = q.popleft()

        # 목적지 도착하면 탈출
        if x == goal_x and y == goal_y:
            ans = cnt
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<I and 0<=ny<I and graph[nx][ny] != 1:
                graph[nx][ny] = 1
                q.append((cnt+1, nx, ny))

    print(ans)