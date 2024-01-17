import sys
from collections import deque

input = sys.stdin.readline

def bfs(a, b):
    queue = deque()
    queue.append(a)
    visited = [0] * 200001
    visited[a] = 1

    while queue:
        current = queue.popleft()
        if current == b:
            return visited[b] - 1
        for n in (current-1, current+1, current*2):
            if 0<=n<200000 and visited[n] == 0:
                queue.append(n)
                visited[n] = visited[current] + 1

n, k = map(int, input().rstrip().split())
ans = bfs(n, k)
print(ans)