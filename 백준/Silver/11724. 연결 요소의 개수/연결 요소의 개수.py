import sys
from collections import deque
 
input = sys.stdin.readline


def bfs(graph, x, visited):
    queue = deque()
    queue.append(x)
    visited[x] = 1
    
    while queue:
        current = queue.popleft()
        for i in graph[current]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
        

n, m = map(int, input().rstrip().split()) # n: 정점 개수, m: 간선 개수
graph = [[] for _ in range(n+1)] # 인접 노드 넣는 리스트
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v) # 양방향으로 넣어야 함
    graph[v].append(u)

cnt = 0
visited = [0] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1 # bfs 끝나면 +1

print(cnt)