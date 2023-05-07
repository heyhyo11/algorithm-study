import sys

num_list = list(range(1, 31))
for i in range(28):
  cnt = int(sys.stdin.readline())
  num_list.remove(cnt)
  
num_list.sort()
print(*num_list, sep='\n')