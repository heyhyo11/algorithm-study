import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
A = [[] for _ in range(n+1)]
ans = []
visited = [-1] * (n+1)

def bfs(v):
    queue = deque()
    queue.append(v) # 시작 노드
    visited[v] += 1 # 현재 노드 방문 기록
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]: # 큐에서 노드 데이터 가져오기
            if visited[i] == -1: # 미방문 노드
                visited[i] = visited[now_node] + 1
                queue.append(i)

for _ in range(m): # 그래프 데이터 저장
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

bfs(1)

for i in range(n+1): # 방문거리가 1 또는 2인 경우 정답 리스트에 추가
    if visited[i] == 1 or visited[i] == 2:
        ans.append(i)

print(len(ans))