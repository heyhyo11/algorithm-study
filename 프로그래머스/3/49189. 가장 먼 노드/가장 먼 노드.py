from collections import deque

def solution(n, edge):
    A = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)
    answer = 0
    
    for line in edge:
        A[line[0]].append(line[1])
        A[line[1]].append(line[0])
        
    queue = deque()
    queue.append(1)
    
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if visited[i] == -1:
                visited[i] = visited[now_node] + 1
                queue.append(i)

    visited[1] = 0
    distance = max(visited)
    for i in visited:
        if i == distance:
            answer += 1
                
    return answer