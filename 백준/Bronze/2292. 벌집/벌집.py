import sys


# 1. 입력 받기
N = int(sys.stdin.readline().rstrip()) # 사용자 입력
n = 1 # 벌집 개수 (1인 경우 거르기)

# 2. 방 개수 찾기
while N > 1:
  N -= (6*n)
  n += 1
  
print(n)