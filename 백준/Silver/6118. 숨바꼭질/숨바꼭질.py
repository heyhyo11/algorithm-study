import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)


# 그래프 입력
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


# bfs
def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = 1
    
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = visited[node] + 1
                queue.append(i)

bfs(1)

maxval = max(visited)
print(visited.index(maxval), maxval-1, visited.count(maxval))