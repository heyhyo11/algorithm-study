# 참고 블로그: https://hei-jayden.tistory.com/103

from collections import deque

n = int(input())
connect = int(input())

# graph: n대의 컴퓨터가 각 연결된 컴퓨터를 확인할 수 있음
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
cnt = 0

for i in range(connect):
    s, e = map(int, input().split())
    # 네트워크 상 연결 : 양방향
    graph[s].append(e)
    graph[e].append(s)

def bfs(graph, v):
    global cnt
    # bfs는 deque 안의 리스트 사용
    queue = deque([v])

    # bfs는 deque 안이 전부 사라질 때까지 반복
    while queue:
        # 가장 왼쪽의 요소부터 pop() 진행
        pop = queue.popleft()
        visited[pop] = True

        for i in graph[pop]:
            if visited[i]==False:
                visited[i] = True
                # 방문한 컴퓨터와 연결된 부분을 큐 안에 추가
                queue.append(i)
                cnt += 1 
    print(cnt)

bfs(graph, 1)