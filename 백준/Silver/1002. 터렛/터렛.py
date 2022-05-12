import sys, math

# 1. 접점 2개: r'-r < d < r'+r
# 2. 접점 1개: r'+r = d or r'-r = d
# 3. 접점 무한: x, y, r 전부 일치

T = int(sys.stdin.readline())

for _ in range(T):
  x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
  d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
  
  # 접점 무한
  if d == 0 and r1 == r2:
    print(-1)
  
  # 접점 1개  
  elif r2 + r1 == d or abs(r2-r1) == d:
    print(1)
  
  # 접점 2개
  elif abs(r2-r1) < d < (r2 + r1):
    print(2)
  
  # 접점 0개  
  else:
    print(0)