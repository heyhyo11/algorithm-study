import sys

n = int(sys.stdin.readline())
for i in range(n):
  print(' '*(n-1-i)+'*'*(2*i+1))