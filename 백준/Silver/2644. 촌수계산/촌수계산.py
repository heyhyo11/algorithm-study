import sys
from collections import deque
 
input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    visited = [0] * (n+1)

    queue.append(x)
    visited[x] = 1
    
    while queue:
        current = queue.popleft()
        if current == y: 
            return visited[y] - 1

        for j in graph[current]:
            if not visited[j]:
                queue.append(j)
                visited[j] = visited[current] + 1
        
    return -1


n = int(input().rstrip()) # 전체 사람 수
start, end = map(int, input().rstrip().split()) # 촌수 계산해야하는 두 사람
m = int(input().rstrip()) # 부모 자식의 관계 개수
graph = [[] for _ in range(n+1)] # 인접 노드 넣는 리스트
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y) # 양방향으로 넣어야 함
    graph[y].append(x)

ans = bfs(start, end)
print(ans)