import sys

n, m = map(int, sys.stdin.readline().split())
while n != 0 and m != 0:
  if n > m:
    print('Yes')
  else:
    print('No')
  n, m = map(int, sys.stdin.readline().split())