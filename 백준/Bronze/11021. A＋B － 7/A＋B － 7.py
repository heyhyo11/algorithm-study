import sys

num = int(sys.stdin.readline().rstrip())

for i in range(1, num+1):
  num = map(int, sys.stdin.readline().split())
  print(f"Case #{i}:", sum(num))