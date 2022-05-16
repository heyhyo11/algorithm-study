import sys

N = int(sys.stdin.readline())
N_list = []

for _ in range(N):
  num = int(sys.stdin.readline())
  N_list.append(num)
  
N_list.sort()
print(*N_list, sep="\n")