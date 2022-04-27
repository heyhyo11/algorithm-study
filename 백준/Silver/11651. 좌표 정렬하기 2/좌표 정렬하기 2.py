import sys

N = int(sys.stdin.readline().rstrip())
num_list = []

for i in range(N):
  xy = list(map(int, sys.stdin.readline().rstrip().split()))
  num_list.append(xy)
  
num_list.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
  print(*num_list[i])