## 참고사이트: https://velog.io/@jeongdopark/Algorithm-python-%EB%B0%B1%EC%A4%80-2798%EB%B2%88

## 방법 1: 브루트 포스
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))

l = len(num)
ans = 0

for i in range(l-2):
  for j in range(i+1, l-1):
    for k in range(j+1, l):
      if (num[i] + num[j] + num[k] > M):
        continue
      else:
        ans = max(ans, num[i] + num[j] + num[k])
        
print(ans)    
        

## 방법2: 파이썬 itertools 라이브러리 이용해서 구현

# from itertools import permutations
# import sys

# N, M = map(int, sys.stdin.readline().rstrip().split())
# num = list(map(int, sys.stdin.readline().rstrip().split()))

# permutationArray = permutations(num, 3)
# ans = 0

# for i in permutationArray:
#   if (M+1 > sum(i)):
#     ans = max(ans, sum(i))
    
# print(ans)