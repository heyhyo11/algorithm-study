import sys

n_list = list(map(int, sys.stdin.readline().rstrip().split()))

ascending = [i for i in range(1, 9)]
descending = [i for i in range(8, 0, -1)]

if n_list == ascending:
  print('ascending')
elif n_list == descending:
  print('descending')
else:
  print('mixed')