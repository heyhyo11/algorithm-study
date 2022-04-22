import sys

T = int(sys.stdin.readline().rstrip()) 

for i in range(T):
  S = list(sys.stdin.readline().rstrip().split(' '))
  ans_list = []
  for j in S[1]:
    j = j * int(S[0])
    ans_list.append(j)
  print(*ans_list, sep='')
