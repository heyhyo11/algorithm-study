import sys


# 1. 입력 받기
A, B, C = map(int, sys.stdin.readline().rstrip().split())
x = 0


# 2. 손익분기점 체크 (A + Bx < Cx), (x > A/(C-B))
if B >= C:
  print(-1)
else:
  print(int(A/(C-B) + 1))