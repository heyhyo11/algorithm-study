import sys

a, b = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

for i in range(a):
  if num_list[i] < b:
    print(num_list[i], end=' ')