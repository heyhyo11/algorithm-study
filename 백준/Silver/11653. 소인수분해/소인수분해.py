import sys

N = int(sys.stdin.readline().rstrip())
num_list = []
cnt = 2

while N >= cnt:
  if N % cnt == 0:
    num_list.append(cnt)
    N = N / cnt
  else:
    cnt += 1
    
print(*num_list, sep='\n')