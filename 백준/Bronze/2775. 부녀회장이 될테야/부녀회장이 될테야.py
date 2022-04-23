## 참고: https://ooyoung.tistory.com/89

import sys


# 1. 입력 받기
T = int(sys.stdin.readline().rstrip())
num_list = []


# 2. 반복문으로 호실 구하기
for _ in range(T):
  k = int(sys.stdin.readline()) # 층
  n = int(sys.stdin.readline()) # 호
  f0 = [x for x in range(1, n+1)] # 0층 리스트  
  
  for k in range(k): # 층 수만큼 반복
    for i in range(1, n): # 1~n-1 (인덱스로 사용)
      f0[i] += f0[i-1]
  print(f0[-1])