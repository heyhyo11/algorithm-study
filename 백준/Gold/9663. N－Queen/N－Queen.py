# 풀이 참고

def dfs(n):
    global ans
    if n==N:    # 마지막 N행까지 진행하면 
        ans+=1
        return

    for j in range(N): # 모든 행을 돌린다
        if v1[j]==v2[n+j]==v3[n-j]==0:  # 같은 열, 대각선에 없을 경우에만 진행
            # v1: 열, v2: 우측 대각선, v3: 좌측 대각선
            v1[j] = v2[n + j] = v3[n - j] = 1 # 방문 표시
            dfs(n+1) # 다음 행으로 진행
            v1[j] = v2[n + j] = v3[n - j] = 0 # 원래대로 되돌리기

N = int(input())
ans = 0
v1 = [0]*N
v2 = [0]*(2*N)
v3 = [0]*(2*N)
dfs(0)
print(ans)