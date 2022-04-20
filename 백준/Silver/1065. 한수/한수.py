import sys

N = int(sys.stdin.readline().rstrip())
num_list = []

for i in range(1, N+1):
  if i < 100:
    num_list.append(i)
  
  else:
    a = i // 100
    b = i // 10 - a*10
    c = i % 10
    if (a-b) == (b-c):
      num_list.append(i)
   

print(len(num_list))