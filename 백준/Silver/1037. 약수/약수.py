import sys

N = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

num_list.sort()

if N == 1:
  print(num_list[0]**2)
else:
  print(num_list[0]*num_list[-1])