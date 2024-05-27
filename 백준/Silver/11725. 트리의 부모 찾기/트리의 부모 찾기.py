import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input()) # 노드 개수
visited = [False] * (n+1) # 방문 기록
tree = [[] for _ in range(n+1)] # 그래프
answer = [0] * (n+1) # 부모 노드

# 트리 데이터 저장
for _ in range(n-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

# dfs 구현
def dfs(num):
    visited[num] = True
    for i in tree[num]:
        if not visited[i]:
            answer[i] = num
            dfs(i)

# 1번 노드부터 실행
dfs(1)

print(*answer[2:], sep='\n')