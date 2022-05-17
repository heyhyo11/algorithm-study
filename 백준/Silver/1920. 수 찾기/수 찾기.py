import sys


# 입력하기
N = int(sys.stdin.readline())
A_list = [i for i in map(int, sys.stdin.readline().rstrip().split())]
A_list.sort()

M = int(sys.stdin.readline())
X_list = [i for i in map(int, sys.stdin.readline().rstrip().split())]



# 각 원소별로 이분탐색
for X in X_list:
  left, right = 0, N-1
  isExist = False
  
  # 이분탐색 시작
  while left <= right:
    mid = (left + right) // 2
    if X == A_list[mid]:
      isExist = True
      print(1)
      break
    elif X > A_list[mid]:
      left = mid + 1
    else:
      right = mid - 1
  
  # 찾지 못한 경우
  if not isExist:
    print(0)
  