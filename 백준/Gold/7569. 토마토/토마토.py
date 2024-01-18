import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    queue = deque()
    visited = [[[0] * M for _ in range(N)] for _ in range(H) ]
    cnt = 0 # 안 익은 토마토 개수

    # 전체 순환
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if graph[h][i][j] == 1: # 익음
                    queue.append((h, i, j))
                    visited[h][i][j]=1
                elif graph[h][i][j] == 0: # 안익음
                    cnt += 1

    while queue:
        ch, ci, cj = queue.popleft()
        for dh, di, dj in ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)):
            nh, ni, nj = ch + dh, ci + di, cj + dj
            if 0<=nh<H and 0<=ni<N and 0<=nj<M and visited[nh][ni][nj]==0 and graph[nh][ni][nj]==0:
                queue.append((nh, ni, nj))
                visited[nh][ni][nj] = visited[ch][ci][cj] + 1
                cnt -= 1 # 익은 토마토 1개 추가됨

    if cnt == 0:
        return visited[ch][ci][cj] - 1
    else:
        return -1

M, N, H = map(int, input().rstrip().split()) # m: 가로, n: 세로, h: 높이
graph = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]
ans = bfs()
print(ans)