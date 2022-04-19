import sys

chance = int(sys.stdin.readline())

for i in range(1, chance+1):
  print(' '*(chance-i)+'*'*i)