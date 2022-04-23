import sys

# 1. 피타고라스 정리 이용해서 구하기
while True:
  num_list = list(map(int, sys.stdin.readline().rstrip().split()))
  num_list.sort()
  
  if sum(num_list) == 0:
    break
  
  if (num_list[0]**2 + num_list[1]**2) == (num_list[2]**2):
    print('right')
  else:
    print('wrong')