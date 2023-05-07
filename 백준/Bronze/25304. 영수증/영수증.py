import sys

total = 0
x = int(sys.stdin.readline())
n = int(sys.stdin.readline())

for i in range(n):
  cost, cnt = map(int, sys.stdin.readline().split())
  total += cost * cnt
  
if total == x:
  print('Yes')
else:
  print('No')