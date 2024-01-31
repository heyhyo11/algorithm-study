import sys

input = sys.stdin.readline

# n * n의 n 입력
n = int(input().rstrip())

# paper: n * n 전체 입력
paper = [list(input().rstrip()) for _ in range(n)]
ans = []

def search(x, y, k): # x: x좌표, y: y좌표, k: n
    global ans
    visited=paper[x][y] # 시작 좌표를 방문

    for i in range(x, x+k): # 모든 좌표를 이동하면서
        for j in range(y, y+k):
            if paper[i][j] != visited: # 시작 좌표와 일치하지 않으면
                ans.append('(')
                for a in range(2): # 4개의 사각형으로 분리한다.
                    for b in range(2):
                        search(x+a*k//2, y+b*k//2, k//2)
                ans.append(')')
                return ans
            
    if visited=='0':
        ans.append('0')

    elif visited=='1':
        ans.append('1')


# 함수 시작
search(0,0,n)

# 정답 출력
print(''.join(ans))