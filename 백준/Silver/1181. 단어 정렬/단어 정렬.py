import sys

N = int(sys.stdin.readline())
N_list = []

for _ in range(N):
  str = sys.stdin.readline().rstrip()
  N_list.append(str)
  
N_list = list(set(N_list))
N_list.sort(key=lambda x:(len(x), x))

print(*N_list, sep="\n")