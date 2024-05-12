# 풀이 참고
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
A = [list(map(int, input().split())) for _ in range(n)]
ans = []
visited = [[0 for _ in range(n)] for _ in range(n)]

def bfs(v):
    queue = deque()
    queue.append(v) 
    check = [0 for _ in range(n)]

    while queue:
        now_node = queue.popleft()

        for i in range(n):
            if check[i] == 0 and A[now_node][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[v][i] = 1

for i in range(0, n):
    bfs(i)

for i in visited:
    print(*i)