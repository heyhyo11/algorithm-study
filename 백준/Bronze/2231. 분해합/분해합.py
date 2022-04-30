## 참고사이트: https://yongku.tistory.com/787

import sys


N = int(sys.stdin.readline().rstrip())
result = 0


for i in range(1, N+1):
  num = list(map(int, str(i)))
  result = i + sum(num)
  if result == N:
    print(i)
    break
  if i == N:
    print(0)