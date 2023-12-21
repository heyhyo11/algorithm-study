import sys
input = sys.stdin.readline

# n: 리스트 크기, m: 질의 수
# A: 원본 리스트, D: 합 배열

# 원본 리스트 데이터 저장
n, m = map(int, input().split())
A = [[0] * (n+1)]
D = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

# 합 배열 미리 만들어두기
for i in range(1, n+1):
    for j in range(1, n+1):
        # 중복되는 부분 제거하여 계산
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
        
# 질의에 대한 결과 계산 및 출력   
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)