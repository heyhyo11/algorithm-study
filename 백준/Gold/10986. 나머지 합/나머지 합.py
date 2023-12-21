import sys
input = sys.stdin.readline

# n: 수열의 개수, m: 나누어 떨어져야 하는 수
# A: 원본 수열 저장 리스트
# S: 합 배열
# C: 같은 나머지 인덱스를 카운트하는 리스트

n, m = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * n
C = [0] * m
answer = 0
S[0] = A[0] # 합 배열 첫 번째 값 넣어주기

# 합 배열 저장
for i in range(1, n):
    S[i] = S[i-1] + A[i]
    
for i in range(n):
    reminder = S[i] % m
    if reminder == 0: # 나머지가 0이면 그 자체만으로도 카운트
        answer += 1
    C[reminder] += 1 # 해당하는 나머지 인덱스 카운트
    
for i in range(m):
    if C[i] > 1:
        # C[i] 개수에서 2가지 뽑는 경우의 수 정답에 더하기
        answer += (C[i] *(C[i]-1) // 2)
        
print(answer)