# 참고한 사이트: https://happylsm76.tistory.com/entry/%EB%B0%B1%EC%A4%80-2630%EB%B2%88%EC%83%89%EC%A2%85%EC%9D%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0-with-Python

import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []

def solution(x, y, N):
  color = paper[x][y]
  for i in range(x, x+N):
    for j in range(y, y+N):
      if color != paper[i][j]:
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if color == 0:
    result.append(0)
  else:
    result.append(1)
    
solution(0, 0, N)
print(result.count(0))
print(result.count(1))


  

  



