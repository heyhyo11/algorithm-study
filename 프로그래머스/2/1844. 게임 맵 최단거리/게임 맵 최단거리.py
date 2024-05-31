from collections import deque

def solution(maps):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    maps_rows = len(maps)
    maps_cols = len(maps[0])
    visited = [[False] * maps_cols for _ in range(maps_rows)]
    
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x >= 0 and y >= 0 and x < maps_rows and y < maps_cols:
                if maps[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    maps[x][y] = maps[now[0]][now[1]] + 1
                    queue.append((x, y))
    
    
    answer = maps[maps_rows-1][maps_cols-1]
    if answer == 1:
        return -1
    return answer