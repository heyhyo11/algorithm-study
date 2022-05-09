from itertools import combinations
import sys

# 사용자 입력 받기
N, M = map(int, sys.stdin.readline().rstrip().split())

# 1 ~ N까지의 숫자를 리스트로 만들기
N_list = [i for i in range(1, N+1)]

# 모든 경우의 수 구하기
answer = list(combinations(N_list, M))

# answer 출력
for i in answer:
  print(*i)