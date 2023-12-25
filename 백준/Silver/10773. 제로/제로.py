import sys


K = int(sys.stdin.readline().rstrip())
num_list = []


for i in range(K):
  N = int(sys.stdin.readline().rstrip())
  if N == 0:
    num_list.pop()
  else:
    num_list.append(N)

print(sum(num_list))