import sys, math

# 1. 소수 구하는 함수 만들기
def prime_number(n):
  if n == 1:
    return False
  else:
    for i in range(2, int(math.sqrt(n))+1):
      if n % i == 0:
        return False
    return True

# 2. 사용자로부터 입력 받기
M, N = map(int, sys.stdin.readline().rstrip().split())

# 3. 소수 출력
for i in range(M, N+1):
  if prime_number(i):
    print(i)