# 참고 블로그: https://hidemasa.tistory.com/179

import sys

input = sys.stdin.readline

# n * n의 n 입력
n = int(input().rstrip())

# paper: n * n 전체 입력
paper = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 출력할 -1, 0, +1의 개수
cnt_plus = 0
cnt_zero = 0
cnt_minus = 0

def search(x, y, k): # x: x좌표, y: y좌표, k: n
    global cnt_plus, cnt_zero, cnt_minus
    visited=paper[x][y] # 시작 좌표를 방문
    for i in range(x, x+k): # 모든 좌표를 이동하면서
        for j in range(y, y+k):
            if paper[i][j] != visited: # 시작 좌표와 일치하지 않으면
                for a in range(3): # 9개의 사각형으로 분리한다.
                    for b in range(3):
                        search(x+a*k//3, y+b*k//3, k//3) # 예) x+a*9//3, y+b*9//3, 9//3
                return
            
    if visited==-1:
        cnt_minus+=1
    elif visited==0:
        cnt_zero+=1
    elif visited==1:
        cnt_plus+=1

# 함수 시작
search(0,0,n)

# 정답 출력
print(cnt_minus, cnt_zero, cnt_plus, sep='\n')