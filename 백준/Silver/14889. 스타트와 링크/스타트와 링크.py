# 풀이 참고

import sys

input = sys.stdin.readline

def dfs(n, alst, blst):
    global ans

    # 종료 조건
    if n==N:
        # 같은 인원수로 팀을 구성했을 때 점수 계산 시작
        if len(alst)==len(blst):
            asm = bsm = 0 # 초기화
            # 모든 경우의 점수 구한다
            for i in range(M):
                for j in range(M):
                    asm += arr[alst[i]][alst[j]]
                    bsm += arr[blst[i]][blst[j]]
            ans = min(ans, abs(asm-bsm))
        return

    # 2개의 팀 각각 선택함
    dfs(n+1, alst+[n], blst)
    dfs(n+1, alst, blst+[n])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

M = N//2 # 절반만 해도 된다
ans = 100 * M * M
dfs(0, [], []) # 초기에는 비어있음
print(ans)