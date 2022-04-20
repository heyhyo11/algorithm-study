import sys

N = int(sys.stdin.readline().rstrip())


for _ in range(N):
  num_sum = 0
  num_list = list(sys.stdin.readline().rstrip().split("X"))
  for i in range(len(num_list)):
    num_len = len(num_list[i])
    for j in range(1, num_len + 1):
      num_sum += j
  print(num_sum)