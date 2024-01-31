from itertools import product
import sys

# 사용자 입력 받기
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

# 1 ~ N까지의 숫자를 리스트로 만들기
N_list = [i for i in range(1, N+1)]

# 모든 경우의 수 구하기
answer = list(product(N_list, repeat=M))

# answer 출력
for i in answer:
  print(*i)