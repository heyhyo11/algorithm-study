import sys

# 입력하기
N = int(sys.stdin.readline())
user_list = []

# 입력 리스트 받기
for _ in range(N):
  user_list.append(list(sys.stdin.readline().split()))
  
# 문제 기준에 따라 정렬하기
user_list.sort(key = lambda x: int(x[0]))

# 답 출력하기
for i in range(len(user_list)):
  print(*user_list[i])