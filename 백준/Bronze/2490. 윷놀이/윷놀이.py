import sys

for i in range(3):
  n = sum(list(map(int, sys.stdin.readline().split())))
  if n == 0:
    print('D')
  elif n == 1:
    print('C')
  elif n == 2:
    print('B')
  elif n == 3:
    print('A')
  elif n == 4:
    print('E')