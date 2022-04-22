import sys

S = list(sys.stdin.readline().rstrip())
ans_list = [-1 for i in range(26)]

for i in range(len(S)):
  index = ord(S[i])-97
  if ans_list[index] == -1:
    ans_list[index] = i
  else:
    continue
  
print(*ans_list)