from collections import deque
import queue
import sys

col, row = map(int, sys.stdin.readline().split())
tomas = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
days = 0

for i in range(row):
  for j in range(col):
    if tomas[i][j] == 1:
      queue.append([i, j])

def bfs():
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = dx[i] + x, dy[i] + y
      if (0 <= nx < row) and (0 <= ny < col) and tomas[nx][ny] == 0:
        tomas[nx][ny] = tomas[x][y] + 1
        queue.append([nx, ny])

        
bfs()
for row in tomas:
  for elem in row:
    if elem == 0:
      print(-1)
      exit(0)
  days = max(days, max(row))
print(days-1)