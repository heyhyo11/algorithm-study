import sys


# 1. 입력 받기
N = int(sys.stdin.readline().rstrip()) # 사용자 입력
n = 1

# 2. 분모, 분자 찾기 (홀, 짝수에 따라 오름차순 순서 다름)
while N > n:
  N -= n
  n += 1

if n % 2 == 0:
  print(f'{N}/{n-N+1}')
else:
  print(f'{n-N+1}/{N}')