# 풀이 참고

import sys

input = sys.stdin.readline

# 북(-1, 0), 동(0, 1), 남(1, 0), 서(0, -1)
di = [-1,  0,  1,  0]
dj = [ 0,  1,  0, -1]

def solve(ci, cj, dr):
    cnt = 0 # 청소 공간 수
    while 1: # 청소기 움직일 수 있을 때까지 진행
        
        # 형재 위치 방문 표시
        arr[ci][cj] = 2
        cnt+=1

        # 왼쪽방향으로 순서대로 탐색. 미청소 영역이 있는경우 이동/방향설정, 없으면 후진
        flag = 1
        
        while flag==1:
            # 왼쪽부터 네방향중 미청소 영역 있는 경우
            for nd in ((dr+3)%4, (dr+2)%4, (dr+1)%4, dr):
                ni, nj = ci+di[nd], cj+dj[nd]
                if arr[ni][nj]==0:  # 청소 X
                    ci,cj,dr = ni,nj,nd
                    flag=0
                    break
            else: # 모든 방향을 청소했을 경우 후진
                bi, bj = ci-di[dr], cj-dj[dr] # 후진 위치 계산
                if arr[bi][bj]==1: # 벽 만나면 종료
                    return cnt
                else:
                    ci, cj = bi, bj

n, m = map(int, input().split())
si, sj, dr = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = solve(si, sj, dr)
print(ans)