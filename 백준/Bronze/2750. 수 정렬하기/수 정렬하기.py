import sys

N = int(sys.stdin.readline().rstrip())
num_list = []

for _ in range(N):
  n = int(sys.stdin.readline().rstrip())
  num_list.append(n)
  
num_list.sort() 

print(*num_list, sep='\n')