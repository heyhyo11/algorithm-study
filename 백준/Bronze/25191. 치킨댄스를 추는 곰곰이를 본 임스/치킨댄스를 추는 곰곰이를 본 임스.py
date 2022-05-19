import sys

N = int(sys.stdin.readline())
A, B = map(int, sys.stdin.readline().split())

total_chicken = A // 2 + B
if N < total_chicken:
  print(N)
else:
  print(total_chicken)