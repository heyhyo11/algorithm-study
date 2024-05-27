# 풀이 참고

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
cnt = 0 # 테스트 케이스 번호


def dfs(node, parent):

    # 이미 방문한 경우 (사이클 존재)
    if visited[node]:
        return False
    
    visited[node] = True

    for now in tree[node]:
        if now != parent:
            if not dfs(now, node):
                return False
    return True


while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0: # 탈출
        break

    visited = [False] * (n+1) # 방문 체크
    tree = [[] for _ in range(n+1)] # 트리
    cnt += 1 # 테스트 케이스 번호
    answer = 0 # 트리 개수
    

    # 트리 입력
    for _ in range(1, m+1):
        n1, n2 = map(int, input().split())
        tree[n1].append(n2)
        tree[n2].append(n1)

    for i in range(1, n+1):

        # 이미 같은 트리 내의 노드라면 패스
        if visited[i]:
            continue

        # 사이클이 있는지 판별
        if dfs(i, 0):
            answer += 1

    # 출력
    if answer == 0:
        print(f'Case {cnt}: No trees.')
    elif answer == 1:
        print(f'Case {cnt}: There is one tree.')
    else:
        print(f'Case {cnt}: A forest of {answer} trees.')
    