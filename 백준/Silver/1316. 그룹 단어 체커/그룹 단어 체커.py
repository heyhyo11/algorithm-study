import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
  str_list = list(sys.stdin.readline().rstrip())
  for j in range(len(str_list)-1):
    if str_list[j] == str_list[j+1]:
      continue
    elif str_list[j] in str_list[j+1:]:
      N -= 1
      break
    
print(N)