import sys

chance = int(sys.stdin.readline().rstrip())

for i in range(chance):
  a, b = sys.stdin.readline().rstrip().split()
  a = int(a)
  b = int(b)
  print(a+b)