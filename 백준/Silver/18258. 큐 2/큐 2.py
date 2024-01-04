import sys

N = int(sys.stdin.readline())
num_list = []
cnt = 0

for _ in range(N):
  S = sys.stdin.readline().split()
  
  # push
  if S[0] == 'push':
    num_list.append(S[1])
  
  # pop
  elif S[0] == 'pop':
    if len(num_list) - cnt == 0:
      print(-1)
    else:
      print(num_list[cnt])
      cnt += 1
      
  # size
  elif S[0] == 'size':
    print(len(num_list)-cnt)
  
  # empty
  elif S[0] == 'empty':
    if len(num_list) - cnt == 0:
      print(1)
    else:
      print(0)  
  
  # front
  elif S[0] == 'front':
    if len(num_list) - cnt == 0:
      print(-1)
    else:
      print(num_list[cnt])
  
  # back
  elif S[0] == 'back':
    if len(num_list) - cnt == 0:
      print(-1)
    else:
      print(num_list[-1])