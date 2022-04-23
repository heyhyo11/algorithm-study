import sys, math


# 1. 입력 받기
T = int(sys.stdin.readline().rstrip())

# 2. 반복문으로 호실 구하기
for i in range(T):
  H, W, N = map(int, sys.stdin.readline().rstrip().split()) # 사용자 입력
  YY = N % H # 층수
  XX = math.ceil(N / H) # 호실

  if YY == 0:
    YY = H
  
  if XX < 10:
    print(f'{YY}0{XX}')
  else:
    print(f'{YY}{XX}')